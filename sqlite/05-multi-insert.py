
import sqlite3

with sqlite3.connect('app.db') as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Victor"),
        (3, "Manuel")
    ]
    cursor.executemany(
        "INSERT INTO usuarios VALUES (?,?)",
        usuarios,
    )
