"""
Client IP extraction with trusted proxy support.

Security baseline:
- Never trust X-Forwarded-For / X-Real-IP unless the immediate peer is a trusted proxy.
- When trusting proxy headers, strip trusted proxies from the right side of the chain.
"""

from __future__ import annotations

from ipaddress import ip_address, ip_network, IPv4Network, IPv6Network
from typing import Iterable

from fastapi import Request


def _parse_trusted_proxies(items: Iterable[str]) -> list[IPv4Network | IPv6Network]:
    networks: list[IPv4Network | IPv6Network] = []
    for raw in items:
        s = raw.strip()
        if not s:
            continue
        # Support both CIDR and single IP
        try:
            networks.append(ip_network(s, strict=False))
            continue
        except ValueError:
            pass
        try:
            ip = ip_address(s)
            networks.append(ip_network(f"{ip}/{ip.max_prefixlen}", strict=False))
        except ValueError:
            # ignore invalid entries
            continue
    return networks


def _is_trusted(ip_str: str, trusted: list[IPv4Network | IPv6Network]) -> bool:
    try:
        ip = ip_address(ip_str)
    except ValueError:
        return False
    return any(ip in net for net in trusted)


def get_client_ip(
    request: Request,
    *,
    trust_proxy_headers: bool,
    trusted_proxies: str,
) -> str:
    """
    Determine client IP address.

    Args:
        request: FastAPI Request
        trust_proxy_headers: Whether to trust X-Forwarded-For / X-Real-IP when peer is trusted.
        trusted_proxies: Comma-separated list of trusted proxy IPs/CIDRs.
            Example: "127.0.0.1,10.0.0.0/8,192.168.0.0/16"
    """
    remote_ip = request.client.host if request.client else None
    if not remote_ip:
        return "unknown"

    if not trust_proxy_headers:
        return remote_ip

    trusted = _parse_trusted_proxies(trusted_proxies.split(","))
    # Only trust headers if the immediate peer is trusted.
    if not _is_trusted(remote_ip, trusted):
        return remote_ip

    # Prefer X-Forwarded-For; format: client, proxy1, proxy2
    xff = request.headers.get("x-forwarded-for")
    if xff:
        parts = [p.strip() for p in xff.split(",") if p.strip()]
        chain = parts + [remote_ip]
        # Strip trusted proxies from the right side.
        while chain and _is_trusted(chain[-1], trusted):
            chain.pop()
        if chain:
            return chain[-1]

    # Fallback to X-Real-IP when peer is trusted.
    xri = request.headers.get("x-real-ip")
    if xri:
        xri = xri.strip()
        try:
            ip_address(xri)
            return xri
        except ValueError:
            pass

    return remote_ip

