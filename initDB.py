import sqlite3
import csv

conn = sqlite3.connect("accounts.db")



def init_db():
    conn.execute("DROP TABLE ACCOUNT")
    conn.commit()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS ACCOUNT(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        ACCOUNT TEXT NOT NULL,
        PASSWORD TEXT NOT NULL
    )
    """)
    conn.commit()

    file = open("names.csv")
    name_reader = csv.reader(file)
    next(name_reader)
        
    for i in name_reader:
        conn.execute(f"INSERT INTO ACCOUNT(ACCOUNT,PASSWORD) VALUES('{i[0]}','{i[0]}')")
        conn.commit()

    flag = open("flag.txt","r").readline()
    conn.execute(f"INSERT INTO ACCOUNT(ACCOUNT, PASSWORD) VALUES('admin', '{flag}')")
    conn.commit()

if __name__ == "__main__":
    init_db()