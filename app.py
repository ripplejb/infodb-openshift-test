import os

import psycopg2
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return 'Hello World!'


@app.route('/init')
def init():  # put application's code here
    conn = psycopg2.connect(
        host=os.environ["APP_DB_HOST_PORT"],
        database=os.environ["APP_DB_NAME"],
        user=os.environ["APP_DB_USER"],
        password=os.environ["APP_DB_PASSWORD"]
    )
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS profile (
                ID INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL
            )
        """)
    finally:
        if conn is not None:
            conn.close()
    return 'Successfully created a table!!!'


if __name__ == '__main__':
    app.run()
