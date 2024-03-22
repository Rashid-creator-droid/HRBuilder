from sqlalchemy import BigInteger, String, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import TYPE_CHECKING

from models import Base
from enums import Experience, WorkFormat, EmploymentType, EmployeeRegistration

if TYPE_CHECKING:
    from models.application import Application


class Vacancy(Base):
    __tablename__ = "vacancies"

    job_title: Mapped[str]
    specialization: Mapped[str]
    skills: Mapped[list[str]] = mapped_column(ARRAY(String))
    responsibilities: Mapped[list[str]] = mapped_column(ARRAY(String))
    min_salary: Mapped[int] = mapped_column(BigInteger)
    max_salary: Mapped[int] = mapped_column(BigInteger)
    experience: Mapped[Experience]
    education: Mapped[list[str]] = mapped_column(ARRAY(String))
    business_trips: Mapped[bool | None]

    application: Mapped["Application"] = relationship(back_populates="vacancy")


class WorkingConditions(Base):
    __tablename__ = "working_conditions"

    work_place: Mapped[str]
    work_format: Mapped[WorkFormat]
    employment_type: Mapped[EmploymentType]
    employee_registration: Mapped[EmployeeRegistration | None]
    availability_dms: Mapped[bool | None]
    compensation: Mapped[list[str] | None] = mapped_column(ARRAY(String))
    driver_license: Mapped[bool | None]
    having_car: Mapped[bool | None]
    company_descriptions: Mapped[str | None] = mapped_column(
        Text,
        default="",
        server_default="",
    )

    application: Mapped["Application"] = relationship(
        back_populates="working_conditions"
    )
