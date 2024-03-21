from sqlalchemy import (
    String,
)
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from models.base import Base


class City(Base):
    name: Mapped[str] = mapped_column(String())

    def __repr__(self) -> str:
        return f"City(id={self.id!r}, name={self.name!r})"

    def __str__(self) -> str:
        return self.name
