import datetime

from sqlalchemy import BigInteger, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base
from .enums import PaymentMethod


class Payment(Base):
    num_employees: Mapped[int] = mapped_column(Integer, default=1)
    start_date: Mapped[datetime.date]
    end_date: Mapped[datetime.date]
    num_recruiters: Mapped[int] = mapped_column(Integer, default=1)
    payment_method: Mapped[PaymentMethod]
    reward_per_employee: Mapped[int] = mapped_column(BigInteger)
