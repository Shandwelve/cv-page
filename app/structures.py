from typing import TypedDict


class PersonalData(TypedDict):
    name: str
    email: str
    phone: str
    position: str


class ExperienceData(TypedDict):
    title: str
    company: str
    location: str


class EducationData(TypedDict):
    degree: str
    school: str
    location: str
    graduation_date: str


class LanguageData(TypedDict):
    name: str
    understanding: str
    speaking: str
    writing: str


class CVData(TypedDict):
    personal: PersonalData
    experience: list[ExperienceData]
    education: list[EducationData]
    languages: list[LanguageData]
