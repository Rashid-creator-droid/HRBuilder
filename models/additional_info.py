import os

from libcloud.storage.drivers.local import LocalStorageDriver
from sqlalchemy import Boolean, String, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy_file import FileField
from sqlalchemy_file.storage import StorageManager

from .base import Base
from .enums import RecruiterExperience, ResumeFormat


class AdditionalInfo(Base):
    recruiter_experience: Mapped[RecruiterExperience]
    recruiter_responsibilities: Mapped[list[str]] = mapped_column(
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
    blacklist_companies: Mapped[str | None] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    blacklist_employees: Mapped[str | None] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    additional_files: Mapped[FileField]


# Configure Storage
os.makedirs("./upload_dir/attachment", 0o777, exist_ok=True)
container = LocalStorageDriver("./upload_dir").get_container("attachment")
StorageManager.add_storage("default", container)
