from pydantic import BaseModel

class Patient(BaseModel):
    patientid: int
    pFirstName: str
    pLastName: str

    class Config:
        orm_mode = True
