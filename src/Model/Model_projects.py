from src.Utils.DB_conect import get_db_connection
import psycopg2.extras


def fetch_all_projects():
    with get_db_connection() as conn:
        cur = conn.cursor( cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""SELECT
            projects.id,
            projects.project_name,
            projects.description,
            projects.image,
            categories.category_name
            FROM dor_lawyer_portfolio.projects
            INNER JOIN dor_lawyer_portfolio.categories
            ON projects.category_id = categories.id 
            """)
        projects = cur.fetchall()
        return (projects)



def fetch_project_by_category_id(category_id: int):
    with get_db_connection() as conn:
        cur = conn.cursor( cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""SELECT
            projects.id,
            projects.project_name,
            projects.description,
            projects.image,
            categories.category_name
            FROM dor_lawyer_portfolio.projects
            INNER JOIN dor_lawyer_portfolio.categories
            ON projects.category_id = categories.id 
            WHERE categories.id = %s""", (category_id,))
        projects = cur.fetchall()
        return (projects)
    
    
def add_new_project(project_name: str,
                    description: str,
                    category_id: int,
                    image: str | None = None
                    ):
    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO dor_lawyer_portfolio.projects
            (project_name, description, image, category_id)
            VALUES (%s, %s, %s, %s)
            RETURNING id
        """, (project_name, description, image, category_id))
        new_project_id: int = cur.fetchone()[0]
        conn.commit()
        return new_project_id