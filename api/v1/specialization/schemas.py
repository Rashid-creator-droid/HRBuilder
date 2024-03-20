from pydantic import BaseModel


class SpecializationBase(BaseModel):
    name: str | None


class Specialization(SpecializationBase):
    id: int | None


class SpecializationCreate(SpecializationBase):
    pass


class SkillBase(BaseModel):
    name: str | None


class Skill(SkillBase):
    id: int | None


class SkillCreate(SkillBase):
    specialization_id: int | None


class SpecializationSkill(Specialization):
    skills: list[Skill] | None
