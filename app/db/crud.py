from sqlalchemy.orm import Session
from . import models

def get_patients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Patient).offset(skip).limit(limit).all()
