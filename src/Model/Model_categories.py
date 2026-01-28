from src.Utils.DB_conect import get_db_connection
import psycopg2.extras


def fetch_all_categories():
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""SELECT
            id,
            category_name
            FROM dor_lawyer_portfolio.categories
            ORDER BY category_name ASC
            """)
        categories = cur.fetchall()
        return categories
