from src.Utils.DB_conect import get_db_connection
from datetime import date
import psycopg2.extras

def fetch_all_customer_requests():
    with get_db_connection() as conn:
        cur = conn.cursor( cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""SELECT
            customer_request.id,
            customer_request.name,
            customer_request.phone,
            customer_request.email,
            customer_request.category,
            customer_request.message,
            customer_request.status,
            customer_request.created_at
            FROM dor_lawyer_portfolio.customer_request
            """)
        requests = cur.fetchall()
        return (requests)
    
    

def fetch_customer_requests_by_date(from_date: date):
    with get_db_connection() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("""SELECT
                    customer_request.id,
                    customer_request.name,
                    customer_request.phone,
                    customer_request.email,
                    customer_request.category,
                    customer_request.message,
                    customer_request.status,
                    customer_request.created_at
                FROM dor_lawyer_portfolio.customer_request
                WHERE customer_request.created_at >= %s
                ORDER BY customer_request.created_at DESC
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
            INSERT INTO dor_lawyer_portfolio.customer_request
            (name, phone, email, category, message)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
        """, (name, phone, email, category, message))
        new_request_id: int = cur.fetchone()[0]
        conn.commit()
        return new_request_id