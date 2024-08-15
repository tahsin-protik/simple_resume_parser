from pydantic import BaseModel

class Education(BaseModel):
    degree: str
    major: str
    school: str
    year: int

class ATS_Response(BaseModel):
    name: str
    email: str
    skills: list[str]
    education: list[Education]