import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "sslmode": "require"
    
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)


