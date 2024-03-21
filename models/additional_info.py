from sqlalchemy import Boolean, String, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy_file import FileField
from typing import TYPE_CHECKING

from .base import Base
from .enums import RecruiterExperience, ResumeFormat

if TYPE_CHECKING:
    from models.application import Application


class AdditionalInfo(Base):
    __tablename__ = "additional_info"

    recruiter_experience: Mapped[RecruiterExperience]
    recruiter_responsibilities: Mapped[list[str] | None] = mapped_column(
        ARRAY(String)
    )
    resume_format: Mapped[ResumeFormat]
    additional_requirements: Mapped[str | None] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    legal_entity_only: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )
    blacklist_companies: Mapped[list[str] | None] = mapped_column(
        ARRAY(String)
    )
    blacklist_employees: Mapped[list[str] | None] = mapped_column(
        ARRAY(String)
    )
    additional_files: Mapped[FileField | None]

    application: Mapped["Application"] = relationship(
        back_populates="application"
    )
