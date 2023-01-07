import sqlite3

def connect():
    con = sqlite3.connect("attendance.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS attendance (id INTEGER PRIMARY KEY,
        member,date,status)""")

    con.commit()
    con.close()

def Insert(member=' ',date=' ',status=' '):
    con = sqlite3.connect("attendance.db")
    cur= con.cursor()
    cur.execute("INSERT INTO attendance VALUES(NULL,?,?,?)",(member,date,status))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("attendance.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM attendance")
    row=cur.fetchall()
    return row

connect()