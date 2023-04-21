
import sqlite3

with sqlite3.connect('app.db') as con:
    cursor = con.cursor()
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios
    (id INTERGER PRIMARY KEY, nombre VARCHAR(50));
    """
    )
