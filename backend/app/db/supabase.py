from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

class SupabaseClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SupabaseClient, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Initialize Supabase client with environment variables"""
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_SERVICE_KEY")
        
        if not supabase_url or not supabase_key:
            raise ValueError("Supabase URL and key must be set in environment variables")
        
        self.client: Client = create_client(supabase_url, supabase_key)

    def get_client(self) -> Client:
        """Get the Supabase client instance"""
        return self.client 