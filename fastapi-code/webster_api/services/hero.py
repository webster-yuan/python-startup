from sqlmodel import Session

from webster_api.crud.hero import delete_hero_by_id, create_hero, select_heros, select_hero_by_id
from webster_api.models import Hero
from webster_api.schemas.hero import HeroCreate, HeroRead


def delete_hero_service(session: Session, hero_id: int) -> None:
    """
    Service 层职责：
    - 业务流程
    - 事务边界
    """

    # 1️⃣ 数据库操作
    delete_hero_by_id(session, hero_id)

    # 2️⃣ 其他数据同步（你以后就往这里加）
    # delete_hero_cache(hero_id)
    # remove_hero_from_search_index(hero_id)
    # publish_hero_deleted_event(hero_id)

    # 3️⃣ 统一提交事务
    # 转移到 get_session() 的方法里面


def create_hero_service(session: Session, hero: HeroCreate) -> int:
    # 核心：Schema -> Model
    db_hero = Hero.model_validate(hero)
    # 数据库操作
    hero = create_hero(session, db_hero)
    # 其他同步逻辑

    return hero.id


def select_heros_service(session: Session, offset: int, limit: int) -> list[HeroRead]:
    """
    service 是“业务 + 接口之间的缓冲层”
    Hero 是数据库结构
    HeroRead 是对外契约
    """

    heros = select_heros(session, offset, limit)

    # Model -> Read Schema
    return [HeroRead.model_validate(hero) for hero in heros]


def select_hero_by_id_service(session: Session, hero_id: int) -> HeroRead:
    hero = select_hero_by_id(session, hero_id)
    return HeroRead.model_validate(hero)
