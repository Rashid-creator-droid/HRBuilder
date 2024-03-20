from fastapi import APIRouter
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from api.v1.specialization.repositories import (
    post_specialization,
    post_skill,
    get_specialization,
    specialization_by_id,
    post_responsibility,
)
from api.v1.specialization.schemas import (
    SpecializationCreate,
    Specialization,
    SkillCreate,
    Skill,
    SpecializationSkillResp,
    ResponsibilityCreate,
    Responsibility,
)
from core.db_helper import db_helper

router = APIRouter(prefix="/base", tags=["Специализации"])


@router.get(
    "/specialization/{specialization_id}/",
    response_model=SpecializationSkillResp,
    summary="Получить специализацию с id=",
)
async def get_dealer_price(
    specialization: Specialization = Depends(specialization_by_id),
):
    return specialization


@router.get(
    "/all-specializations",
    response_model=List[Specialization],
    summary="Специализации",
)
async def get_all_specialization(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    value = await get_specialization(session=session)
    return value


@router.post(
    "/specialization",
    response_model=Specialization,
    summary="Добавить специализацию",
)
async def specialization_create(
    mapped_in: SpecializationCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await post_specialization(
        session=session,
        mapped_in=mapped_in,
    )


@router.post(
    "/skills",
    response_model=Skill,
    summary="Добавить навык",
)
async def skill_create(
    mapped_in: SkillCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await post_skill(
        session=session,
        mapped_in=mapped_in,
    )


@router.post(
    "/responsibilities",
    response_model=Responsibility,
    summary="Добавить обязанность",
)
async def responsibility_create(
    mapped_in: ResponsibilityCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await post_responsibility(
        session=session,
        mapped_in=mapped_in,
    )
