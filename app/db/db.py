from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.environ.get("DATABASE_URL")
SUPABASE_KEY = os.environ.get("API_DATABASE")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

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
