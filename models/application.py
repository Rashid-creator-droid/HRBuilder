from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from typing import TYPE_CHECKING, Optional

from models.base import Base

if TYPE_CHECKING:
    # from models.users import User
    from models.vacancy import Vacancy, WorkingConditions
    from models.payment import Payment
    from models.additional_info import AdditionalInfo


class Application(Base):
    # user_id: Mapped[int] = mapped_column(
    #     ForeignKey("users.id", ondelete="CASCADE")
    # )
    # user: Mapped["User"] = relationship(back_populates="applications")

    vacancy_id: Mapped[int | None] = mapped_column(ForeignKey("vacancies.id"))
    vacancy: Mapped[Optional["Vacancy"]] = relationship(
        back_populates="application"
    )

    working_conditions_id: Mapped[int | None] = mapped_column(
        ForeignKey("working_conditions.id")
    )
    working_conditions: Mapped[Optional["WorkingConditions"]] = relationship(
        back_populates="application"
    )

    payment_id: Mapped[int | None] = mapped_column(ForeignKey("payments.id"))
    payment: Mapped[Optional["Payment"]] = relationship(
        back_populates="application"
    )

    additional_info_id: Mapped[int | None] = mapped_column(
        ForeignKey("additional_info.id")
    )
    additional_info: Mapped[Optional["AdditionalInfo"]] = relationship(
        back_populates="application"
    )

    is_published: Mapped[bool] = mapped_column(default=False)
