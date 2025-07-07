from sqlalchemy import Column, Integer, String
from app.db.db import Base

class Patient(Base):
    __tablename__ = "patients"

    patientid = Column(Integer, primary_key=True, index=True)
    pFirstName = Column("pfirstname", String)  # ตรงนี้! map ไปที่ชื่อ column ใน DB
    pLastName = Column("plastname", String)