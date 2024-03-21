import datetime

from sqlalchemy import BigInteger, Integer
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from typing import TYPE_CHECKING

from .base import Base
from .enums import PaymentMethod

if TYPE_CHECKING:
    from models.application import Application


class Payment(Base):
    num_employees: Mapped[int] = mapped_column(Integer, default=1)
    start_date: Mapped[datetime.date]
    end_date: Mapped[datetime.date]
    num_recruiters: Mapped[int] = mapped_column(Integer, default=1)
    payment_method: Mapped[PaymentMethod]
    reward_per_employee: Mapped[int] = mapped_column(BigInteger)

    application: Mapped["Application"] = relationship(
        back_populates="application"
    )
