# TODO

## Auth & Authorization

- [x] **Auth/AuthZ v1.0 (current implementation, baseline)**
  - Access token: JWT (short-lived, default 10 minutes), `sub=user_id`, `iss/aud` enforced, `kid` + multi-key verification.
  - Refresh token: opaque string + refresh rotation; server stores only sha256 hash in `AuthSession`.
  - Logout: revoke refresh session (access expires naturally).
  - Protected APIs: hero endpoints require authentication.
  - Security hardening: in-memory rate limiting with max-keys + LRU/TTL eviction; trusted-proxy client IP extraction.

- [ ] **Auth/AuthZ v1.1+ (future upgrades)**
  - Redis-based rate limiting (shared across pods) + metrics/observability.
  - Access immediate revocation option (session-bound access / blacklist) for “force logout” scenarios.
  - Migration/cleanup module for legacy tokens/data (pre-rollout job).
  - Add device_id support (optional header) and session management endpoints (list/revoke sessions).
  - JWT key rotation playbook (kid rollover + staged keyring changes).

