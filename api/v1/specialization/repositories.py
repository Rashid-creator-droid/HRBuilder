from typing import Sequence, Annotated
from fastapi import Depends, Path
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from api.v1.specialization.schemas import (
    SpecializationBase,
    SkillCreate,
)
from core.db_helper import db_helper
from models import Specialization, Skill


async def post_specialization(
    session: AsyncSession,
    mapped_in: SpecializationBase,
):
    specialization = Specialization(**mapped_in.dict())
    session.add(specialization)
    await session.commit()
    return specialization


async def post_skill(session: AsyncSession, mapped_in: SkillCreate):
    skill = Skill(**mapped_in.dict())
    session.add(skill)
    await session.commit()
    return skill


async def get_specialization(
    session: AsyncSession,
) -> Sequence[Specialization]:
    stmt = select(Specialization)
    result = await session.execute(stmt)
    all_specialization = result.scalars().all()
    await session.close()
    return all_specialization


async def specialization_by_id(
    specialization_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    stmt = (
        select(Specialization)
        .where(Specialization.id == specialization_id)
        .options(joinedload(Specialization.skills))
    )
    result = await session.execute(stmt)
    specialization = result.scalar()
    print(specialization)
    await session.close()
    return specialization
