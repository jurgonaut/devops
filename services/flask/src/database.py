import psycopg2
import os


def get_db_connection():
    conn = psycopg2.connect(host=os.environ["DATABASE_HOST"],
                            database=os.environ["DATABASE_SCHEMA"],
                            user=os.environ["DATABASE_USER"],
                            password=os.environ["DATABASE_PASS"])
    return conn
