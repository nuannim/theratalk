from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.environ.get("DATABASE_URL")
SUPABASE_KEY = os.environ.get("API_DATABASE")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
