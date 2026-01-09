from typing import Sequence

from sqlmodel import Session, select

from webster_api.exception.hero import HeroNotFoundError
from webster_api.models import Hero


def get_hero_by_id(session: Session, hero_id: int) -> Hero:
    hero = session.exec(select(Hero).where(Hero.id == hero_id)).first()
    if not hero:
        raise HeroNotFoundError()

    return hero


def delete_hero_by_id(session: Session, hero_id: int) -> None:
    """
    CRUD 层职责：
    - 查
    - 删
    - 不 commit
    - 不关心 HTTP
    """
    hero = get_hero_by_id(session, hero_id)
    session.delete(hero)


def create_hero(session: Session, hero: Hero) -> Hero:
    session.add(hero)
    session.flush()
    return hero


def select_heros(
        session: Session,
        offset: int = 0,
        limit: int = 100
) -> Sequence[Hero]:
    statement = select(Hero).offset(offset).limit(limit)
    return session.exec(statement).all()


def select_hero_by_id(session: Session, hero_id: int) -> Hero:
    statement = select(Hero).where(Hero.id == hero_id)
    return session.exec(statement).first()
