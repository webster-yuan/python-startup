"""
AuthSession CRUD.
Only store refresh token hashes, never plaintext tokens.
"""

from __future__ import annotations

from datetime import datetime, timezone

from sqlmodel import Session, select

from webster_api.models.auth_session import AuthSession


def get_session_by_refresh_hash(session: Session, refresh_token_hash: str) -> AuthSession | None:
    statement = select(AuthSession).where(AuthSession.refresh_token_hash == refresh_token_hash)
    return session.exec(statement).first()


def create_auth_session(
    session: Session,
    *,
    user_id: int,
    refresh_token_hash: str,
    expires_at: datetime,
    created_ip: str | None = None,
    user_agent: str | None = None,
) -> AuthSession:
    now = datetime.now(timezone.utc)
    row = AuthSession(
        user_id=user_id,
        refresh_token_hash=refresh_token_hash,
        created_at=now,
        expires_at=expires_at,
        created_ip=created_ip,
        user_agent=user_agent,
    )
    session.add(row)
    session.flush()
    return row


def get_active_session_by_refresh_hash(session: Session, refresh_token_hash: str) -> AuthSession | None:
    now = datetime.now(timezone.utc)
    statement = (
        select(AuthSession)
        .where(AuthSession.refresh_token_hash == refresh_token_hash)
        .where(AuthSession.revoked_at.is_(None))
        .where(AuthSession.expires_at > now)
    )
    return session.exec(statement).first()


def revoke_session(
    session: Session,
    auth_session: AuthSession,
    *,
    replaced_by_hash: str | None = None,
) -> AuthSession:
    now = datetime.now(timezone.utc)
    if auth_session.revoked_at is None:
        auth_session.revoked_at = now
    # keep last replaced_by_hash if already set unless caller provides one
    if replaced_by_hash is not None:
        auth_session.replaced_by_hash = replaced_by_hash
    session.add(auth_session)
    session.flush()
    return auth_session


def touch_session_last_used(session: Session, auth_session: AuthSession) -> AuthSession:
    now = datetime.now(timezone.utc)
    auth_session.last_used_at = now
    session.add(auth_session)
    session.flush()
    return auth_session

