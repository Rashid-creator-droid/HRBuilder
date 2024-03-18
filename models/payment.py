import datetime
import enum

from sqlalchemy import Date, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base


class PaymentMethod(str, enum.Enum):
    FIRST_PAYMENT = "100% за выход сотрудника"
    SECOND_PAYMETN = "50% за выход + 50% по окончании испытательного срока"
    THIRD_PAYMENT = "100% по окончании испытательного срока"


class Payment(Base):
    numb_employees: Mapped[int] = mapped_column(Integer)
    start_date: Mapped[datetime.date] = mapped_column(Date)
    end_date: Mapped[datetime.date] = mapped_column(Date)
    num_recruiters: Mapped[int] = mapped_column(Integer)
    payment_method: Mapped[PaymentMethod]
