# from sqlalchemy.orm import mapped_column, Mapped, relationship
# from typing import TYPE_CHECKING
#
# from models import Base
#
# if TYPE_CHECKING:
#     from models.application import Application
#
#
# class User(Base):
#     email: Mapped[str] = mapped_column(unique=True)
#     username: Mapped[str] = mapped_column(unique=True)
#
#     applications: Mapped[list["Application"] | None] = relationship(
#         back_populates="client"
#     )
