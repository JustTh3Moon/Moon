import sqlite3 as sq

con = sq.connect("practice")
cur = con.cursor()

cur.execute("CREATE TABLE test()")

version = sq.sqlite_version()