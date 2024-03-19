import datetime

from sqlalchemy import Date, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base
from .enums import PaymentMethod


class Payment(Base):
    numb_employees: Mapped[int] = mapped_column(Integer)
    start_date: Mapped[datetime.date] = mapped_column(Date)
    end_date: Mapped[datetime.date] = mapped_column(Date)
    num_recruiters: Mapped[int] = mapped_column(Integer)
    payment_method: Mapped[PaymentMethod]
