from typing import List

from pydantic import BaseModel, field_validator
from datetime import date


class Vacancy(BaseModel):
    job_title: str | None
    specialization: str | None
    skills: List[str] | None
    responsibilities: List[str] | None
    min_salary: int | None
    max_salary: int | None
    hide_salary: bool | None
    experience: str | None
    education: List[str] | None
    business_trips: bool | None

    @field_validator("min_salary", "max_salary")
    def check_salary_range(cls, v, values):
        min_salary = values.get("min_salary")
        max_salary = values.get("max_salary")
        if (
            min_salary is not None
            and max_salary is not None
            and min_salary >= max_salary
        ):
            raise ValueError("min_salary должен быть меньше, чем max_salary")
        return v


class Conditions(BaseModel):
    work_place: str | None
    work_format: str | None
    employment_type: str | None
    employee_registration: str | None
    availability_DMS: bool | None
    compensation: List[str] | None
    driver_license: bool | None
    having_car: bool | None
    company_descriptions: str | None


class Payment(BaseModel):
    number_employees: int | None
    start_search: date | None
    end_search: date | None
    number_recruits: int | None
    payment_model: str | None
    reward: int | None


class Additionally(BaseModel):
    recruiter_experience: str | None
    recruiter_job: List[str] | None
    type_resume: str | None
    additional_requirements: str | None
    stoplist_companies: List[str] | None
    stoplist_employee: List[str] | None
