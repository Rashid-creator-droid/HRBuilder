from enum import Enum


class PaymentMethod(str, Enum):
    first_payment = "100% за выход сотрудника"
    second_payment = "50% за выход + 50% по окончании испытательного срока"
    third_payment = "100% по окончании испытательного срока"


class RecruiterExperience(str, Enum):
    junior = "1-3 года"
    middle = "3-6 лет"
    senior = "От 6 лет"


class ResumeFormat(str, Enum):
    without_interview = "Резюме без предварительного собеседования"
    with_interview = "Резюме кандидатов, с которыми проведено интервью, с комментариями по кандидату"
