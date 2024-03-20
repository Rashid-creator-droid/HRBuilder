from sqlalchemy import (
    String,
    ForeignKey,
)
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from models.base import Base


class Specialization(Base):
    name: Mapped[str] = mapped_column(String())
    skills: Mapped[list["Skill"] | None] = relationship(
        back_populates="specialization"
    )
    responsibilities: Mapped[list["Responsibility"] | None] = relationship(
        back_populates="specialization"
    )

    def __repr__(self) -> str:
        return f"SpecializationBase(id={self.id!r}, name={self.name!r})"

    def __str__(self) -> str:
        return self.name


class Skill(Base):
    name: Mapped[str] = mapped_column(String())
    specialization_id: Mapped[int | None] = mapped_column(
        ForeignKey("specializations.id")
    )
    specialization: Mapped["Specialization"] = relationship(
        back_populates="skills"
    )

    def __repr__(self) -> str:
        return f"Skill(id={self.id!r}, name={self.name!r})"

    def __str__(self) -> str:
        return self.name


class Responsibility(Base):
    name: Mapped[str] = mapped_column(String())
    specialization_id: Mapped[int | None] = mapped_column(
        ForeignKey("specializations.id")
    )
    specialization: Mapped["Specialization"] = relationship(
        back_populates="responsibilities"
    )

    def __repr__(self) -> str:
        return f"Responsibilities(id={self.id!r}, name={self.name!r})"

    def __str__(self) -> str:
        return self.name
