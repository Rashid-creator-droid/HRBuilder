from fastapi import APIRouter

from api.v1.application.schemas import (
    Vacancy,
    Conditions,
    Payment,
    Additionally,
)

router = APIRouter(prefix="/application", tags=["Создать заявку"])


@router.post(
    "/vacancy",
    response_model=Vacancy,
    summary="О вакансии",
)
async def vacancy_create():
    value = Vacancy
    return value


@router.post(
    "/conditions", response_model=Conditions, summary="Условия работы"
)
async def conditions_create():
    value = Conditions
    return value


@router.post("/payment", response_model=Payment, summary="Об оплате")
async def payment_create():
    value = Payment
    return value


@router.post(
    "/additionally", response_model=Additionally, summary="Дополнительно"
)
async def additionally_create():
    value = Additionally
    return value
