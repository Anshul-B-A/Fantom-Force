# utils/supabase_client.py
from supabase import create_client, Client

SUPABASE_URL = "https://ixcpxraktziqeatwjvta.supabase.co"  
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml4Y3B4cmFrdHppcWVhdHdqdnRhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQzNjA2MjUsImV4cCI6MjA1OTkzNjYyNX0.fvAz1KxiOGTFxvIiKBGx-wwjrKlQ9YhN2S0HnNnnC2s"             

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
