"""
Auth session / refresh token storage.

Enterprise baseline:
- Never store refresh token plaintext in DB.
- Store a one-way hash (sha256) + metadata for rotation/revocation.
"""

from __future__ import annotations

from datetime import datetime

from sqlmodel import SQLModel, Field


class AuthSession(SQLModel, table=True):
    """Refresh token session (stored as hash)."""

    id: int | None = Field(default=None, primary_key=True)

    # Link to user
    user_id: int = Field(foreign_key="user.id", index=True)

    # sha256(refresh_token) hex string
    refresh_token_hash: str = Field(unique=True, index=True)

    created_at: datetime = Field(index=True)
    expires_at: datetime = Field(index=True)

    revoked_at: datetime | None = Field(default=None, index=True)
    replaced_by_hash: str | None = Field(default=None, index=True)

    last_used_at: datetime | None = Field(default=None, index=True)

    # Optional audit fields (no PII secrets)
    created_ip: str | None = None
    user_agent: str | None = None

