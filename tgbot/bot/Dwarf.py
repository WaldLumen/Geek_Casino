import os

from psycopg_pool import ConnectionPool


class Dwarf:
    def __init__(self):
        self.name = os.getenv('name')
        self.user = os.getenv('user')
        self.pool = ConnectionPool("dbname=Geek_Casino user=postgres")

    def create_table(self):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                             CREATE TABLE IF NOT EXISTS 
                             users (
                                id serial PRIMARY KEY,
                                cash integer) 
                            """)

    def dices(self, user_id):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT cash FROM users WHERE"
                            " id = %s FOR UPDATE" % user_id)
                return cur.fetchone()[0]

    def profile(self, user_id):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT cash FROM users WHERE id = %s" % user_id)
                return cur.fetchone()

    def register_user(self, user_id):

        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id FROM users WHERE ID = %s" % user_id)
                if cur.fetchone() is None:
                    cur.execute(
                        "INSERT INTO users (id, cash) VALUES (%s, %s)",
                        (user_id, 1000))
                    conn.commit()
                else:
                    pass

    def replenishment(self, ball: int, user_id: int):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id FROM users WHERE id = %s" % user_id)
                cur.execute(
                    "Update users set cash = cash + %s WHERE id = %s" % (ball, user_id)
                )

    def cash_withdrawal(self, ball: int, user_id: int):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id FROM users WHERE id = %s" % user_id)
                cur.execute(
                    "Update users set cash = cash - %s WHERE id = %s" % (ball, user_id)
                )

    def drop_table(self):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DROP TABLE users")
