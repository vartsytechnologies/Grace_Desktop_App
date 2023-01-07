import sqlite3

def connect():
    con = sqlite3.connect("grace1.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS member1 (id INTEGER PRIMARY KEY,
    mem_id,name,mem_type,POB,DOB,gender,department,telephone,address,email,m_stat,occupation,fax,emp,hometown,region,tithe,h_stat,how,comp_name,pst_add,e_contact,edu_level,institution)""")

    con.commit()
    con.close()

def Insert(mem_id=' ',name=' ',mem_type=' ',POB=' ',DOB=' ',gender=' ',department=' ',telephone=' ',address=' ',email=' ',m_stat=' ',occupation=' ',fax='' ,emp=' ',hometown=' ',region=' ',tithe=' ',h_stat=' ',how=' ',comp_name=' ',pst_add=' ',e_contact=' ',edu_level=' ',institution=' '):
    con = sqlite3.connect("grace1.db")
    cur= con.cursor()
    cur.execute("INSERT INTO member1 VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(mem_id,name,mem_type,POB,DOB,gender,department,telephone,address,email,m_stat,occupation,fax,emp,hometown,region,tithe,h_stat,how,comp_name,pst_add,e_contact,edu_level,institution))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("grace1.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM member1")
    row=cur.fetchall()
    return row

def delete(id):
    con = sqlite3.connect("grace1.db")
    cur = con.cursor()
    cur.execute("DELETE FROM member1 WHERE id=?", (id,))
    con.commit()
    con.close()

connect()
