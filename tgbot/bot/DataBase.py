import os

from psycopg_pool import ConnectionPool


class DBQueries:
    def __init__(self):
        self.name = os.getenv('name')
        self.user = os.getenv('user')
        self.pool = ConnectionPool("dbname=casinobot user=postgres")

    def create_table(self):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                             CREATE TABLE IF NOT EXISTS 
                             users (
                                id serial PRIMARY KEY,
                                cash integer) 
                            """)

    def register_user(self, user_id):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id FROM users WHERE id = '%s'" % user_id)
                if cur.fetchone() is None:
                    cur.execute(
                        "INSERT INTO users (id, cash) VALUES (%s, %s)",
                        (user_id, 1000))

    def the_richest(self):
        top = []
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users")
