
import sqlite3

with sqlite3.connect('app.db') as con:
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO usuarios VALUES (?,?)",
        (1, "Hola Mundo")
    )
