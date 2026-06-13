import sqlite3

class DatabaseManager:

    def create_database(
        self
    ):

        conn = sqlite3.connect(
            "sales.db"
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS sales(

                Date TEXT,

                Product TEXT,

                Quantity INTEGER,

                Sales REAL
            )
            """
        )

        conn.commit()

        conn.close()

    def insert_data(
        self,
        data
    ):

        conn = sqlite3.connect(
            "sales.db"
        )

        data.to_sql(

            "sales",

            conn,

            if_exists="replace",

            index=False
        )

        conn.close()

    def record_count(
        self
    ):

        conn = sqlite3.connect(
            "sales.db"
        )

        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM sales"
        )

        count = cursor.fetchone()[0]

        conn.close()

        return count

    def fetch_data(
        self
    ):

        conn = sqlite3.connect(
            "sales.db"
        )

        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM sales"
        )

        rows = cursor.fetchall()

        conn.close()

        return rows