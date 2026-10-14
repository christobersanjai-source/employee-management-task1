from app.db.session import get_db_connection
def init_db():
    query = """CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY, name VARCHAR(120) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL, department VARCHAR(100) NOT NULL,
        job_title VARCHAR(120) NOT NULL);"""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
