import sqlite3

connection = sqlite3.connect("data/app.db")
cursor = connection.cursor()


def initialize_database():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        sentiment TEXT
    )
    """)

    connection.commit()


def save_news(title, sentiment):

    cursor.execute(
        "INSERT INTO news(title, sentiment) VALUES(?, ?)",
        (title, sentiment)
    )

    connection.commit()