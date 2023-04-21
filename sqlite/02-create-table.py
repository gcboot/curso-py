
import sqlite3

con = sqlite3.connect('app.db')
cursor = con.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios
    (id INTERGER PRIMARY KEY, nombre VARCHAR(50));
    """
)
con.commit()
con.close()
