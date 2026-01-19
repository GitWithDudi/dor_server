from src.Utils.DB_conect import get_db_connection
from datetime import date
import psycopg2.extras

def fetch_all_customer_requests():
    with get_db_connection() as conn:
        cur = conn.cursor( cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""SELECT
            customer_requests.id,
            customer_requests.name,
            customer_requests.phone,
            customer_requests.email,
            customer_requests.category,
            customer_requests.message,
            customer_requests.created_at
            FROM dor_lawyer_portfolio.customer_requests
            """)
        customer_requests = cur.fetchall()
        return (customer_requests)
    
    

def fetch_customer_request_by_date(from_date: date):
    with get_db_connection() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("""
                SELECT
                    customer_requests.id,
                    customer_requests.name,
                    customer_requests.phone,
                    customer_requests.email,
                    customer_requests.category,
                    customer_requests.message,
                    customer_requests.created_at
                FROM dor_lawyer_portfolio.customer_requests
                WHERE customer_requests.created_at >= %s
                ORDER BY customer_requests.created_at DESC
            """, (from_date,))
        requests = cur.fetchall()
        return (requests)
    
    
    

def add_new_customer_request(name: str,
                            phone: str,
                            email: str,
                            message: str,
                            category: str | None = None):
    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO dor_lawyer_portfolio.customer_requests
            (name, phone, email, category, message)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
        """, (name, phone, email, category, message))
        new_request_id: int = cur.fetchone()[0]
        conn.commit()
        return new_request_id