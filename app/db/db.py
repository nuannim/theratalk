from supabase import create_client, Client
import os
from dotenv import load_dotenv

# SQLAlchemy imports
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()

SUPABASE_URL = os.environ.get("DATABASE_URL")
SUPABASE_KEY = os.environ.get("API_DATABASE")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# DATABASE_URL = os.environ.get("POSTGRES_URL")

# engine = create_engine(DATABASE_URL)
# # SessionLocal = sessionmaker(bind=engine)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     print('📍📍📍📍📍📍 lllllllllllllll')
#     try:
#         yield db
#         print('📍📍📍📍📍📍 fjewafewafewijfewjiofoaeiw')
#     finally:
#         db.close()

# # SQLAlchemy connection string (แก้ไข user, password, host, port, dbname ให้ตรงกับของคุณ)
# POSTGRES_URL = os.environ.get("POSTGRES_URL")  # ตัวอย่าง: "postgresql+asyncpg://user:password@host:5432/dbname"

# engine = create_async_engine(POSTGRES_URL, echo=True)
# AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# async def get_async_db():
#     async with AsyncSessionLocal() as session:
#         yield session

# def get_user(username: str, password: str, role: str):
#     table = "patients" if role == "patient" else "slp"
#     result = supabase.table(table).select("*").eq(f"{role}Username", username).eq(f"{role}Password", password).execute()

#     if result.data:
#         return result.data[0]
#     return None

def get_user(username: str, password: str):
    # ลองเช็คใน patients
    patient = supabase.table("patients").select("*")\
        .eq("pusername", username).eq("ppassword", password).execute()
    if patient.data:
        return {"role": "patient", "user": patient.data[0]}

    # ลองเช็คใน slp
    slp = supabase.table("slp").select("*")\
        .eq("slpusername", username).eq("slppassword", password).execute()
    if slp.data:
        return {"role": "slp", "user": slp.data[0]}

    return None
