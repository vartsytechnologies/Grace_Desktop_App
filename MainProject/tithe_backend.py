import sqlite3

def connect():
    con = sqlite3.connect("tithe.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS finan (id INTEGER PRIMARY KEY,
    mem_id,name,month,amt,date )""")

    con.commit()
    con.close()

def Insert(mem_id=' ',name=' ',month=' ',amt=' ',date=' '):
    con = sqlite3.connect("tithe.db")
    cur= con.cursor()
    cur.execute("INSERT INTO finan VALUES(NULL,?,?,?,?,?)",(mem_id,name,month,amt,date))
    con.commit()
    con.close()


def search(mem_id="",name="",month="",amt="",date=""):
    con = sqlite3.connect('tithe.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM finan WHERE mem_id = ? OR name = ? OR month = ? OR amt = ? OR date = ?',(mem_id,name,month,amt,date))
    row = cur.fetchall()
    return row
    con.close()


def update(id,mem_id="",name="",month="",amt="",date=""):
    con = sqlite3.connect('tithe.db')
    cur = con.cursor()

    cur.execute('UPDATE finan SET mem_id = ? OR name = ? OR month = ? OR amt = ? OR date = ?',(mem_id,name,month,amt,date))
    con.commit()
    con.close()


def view():
    con = sqlite3.connect("tithe.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM finan")
    row=cur.fetchall()
    return row

def delete(id):
    con = sqlite3.connect("tithe.db")
    cur = con.cursor()
    cur.execute("DELETE FROM finan WHERE id=?", (id,))
    con.commit()
    con.close()

connect()
