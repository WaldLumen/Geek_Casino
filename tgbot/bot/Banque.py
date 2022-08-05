import psycopg


class Banque:
    @staticmethod
    def create_table():
        with psycopg.connect("dbname=Geek_Casino user=silvia") as conn:
            with conn.cursor() as cur:
                cur.execute("""
                             CREATE TABLE IF NOT EXISTS 
                             users(
                                id serial PRIMARY KEY,
                                cash integer) 
                            """)
                conn.commit()
                conn.close()

    @staticmethod
    def drop_table():
        with psycopg.connect("dbname=Geek_Casino user=silvia") as conn:
            with conn.cursor() as cur:
                cur.execute("DROP TABLE users")
                conn.close()

    @staticmethod
    def register_user(user_id):
        with psycopg.connect("dbname=Geek_Casino user=silvia") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id FROM users WHERE ID = %s" % user_id)
                if cur.fetchone() is None:
                    cur.execute(
                        "INSERT INTO users (id, cash) VALUES (%s, %s)",
                        (user_id, 1000))
                    conn.commit()
                    conn.close()

    @staticmethod
    def show_cash(user_id) -> int:
        with psycopg.connect("dbname=Geek_Casino user=silvia") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT cash FROM users WHERE id = %s" % user_id)
                return cur.fetchone()[0]

    @staticmethod
    def replenishment(ball: int, user_id: int):
        with psycopg.connect("dbname=Geek_Casino user=silvia") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "Update users set cash = cash + %s WHERE id = %s" % (ball, user_id)
                )
                conn.commit()
                conn.close()

    @staticmethod
    def cash_withdrawal(ball: int, user_id: int):
        with psycopg.connect("dbname=Geek_Casino user=silvia") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "Update users set cash = cash - %s WHERE id = %s" % (ball, user_id)
                )
                conn.commit()
                conn.close()

    @staticmethod
    def start_transaction():
        with psycopg.connect("dbname=Geek_Casino user=silvia") as conn:
            with conn.cursor() as cur:
                cur.execute("BEGIN")

    @staticmethod
    def commit_transaction():
        with psycopg.connect("dbname=Geek_Casino user=silvia") as conn:
            with conn.cursor() as cur:
                cur.execute("COMMIT")
                conn.close()

    @staticmethod
    def select_cash_for_update(user_id):
        with psycopg.connect("dbname=Geek_Casino user=silvia") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT cash FROM users WHERE id = %s FOR UPDATE" % user_id)

