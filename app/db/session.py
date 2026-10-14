import psycopg
from app.core.config import settings
def get_db_connection():
    return psycopg.connect(settings.database_url)
