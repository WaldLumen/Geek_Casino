from psycopg_pool import ConnectionPool


class Banque:
    def __init__(self):
        self.pool = ConnectionPool("dbname=Geek_Casino user=silvia")

    def create_table(self):
        with self.pool.connection() as conn:
            request = """
                        CREATE TABLE IF NOT EXISTS 
                             users(
                                id serial PRIMARY KEY,
                                cash integer
                                ) 
                      """

            conn.execute(request)
            conn.commit()

    def register_user(self, user_id):
        with self.pool.connection() as conn:
            conn.execute("SELECT id FROM users WHERE ID = %s" % user_id)
            if conn.fetchone() is None:
                conn.execute(
                    "INSERT INTO users (id, cash) VALUES (%s, %s)",
                    (user_id, 1000))
                conn.commit()

    def drop_table(self):
        with self.pool.connection() as conn:
            conn.execute("DROP TABLE users")

    def show_cash(self, user_id) -> int:
        with self.pool.connection() as conn:
            conn.execute("SELECT cash FROM users WHERE id = %s" % user_id)
            return conn.fetchone()[0]

    def replenishment(self, ball: int, user_id: int):
        with self.pool.connection() as conn:
            conn.execute(
                "Update users set cash = cash + %s WHERE id = %s" % (ball, user_id)
            )
            conn.commit()

    def cash_withdrawal(self, ball: int, user_id: int):
        with self.pool.connection() as conn:
            conn.execute(
                "Update users set cash = cash - %s WHERE id = %s" % (ball, user_id)
            )
            conn.commit()

    def start_transaction(self):
        with self.pool.connection() as conn:
            conn.execute("BEGIN")

    def commit_transaction(self):
        with self.pool.connection() as conn:
            conn.execute("COMMIT")

    def select_cash_for_update(self, user_id):
        with self.pool.connection() as conn:
            conn.execute("SELECT cash FROM users WHERE id = %s FOR UPDATE" % user_id)
