import psycopg2
import psycopg2.extras
import sqlite3

hostname = 'localhost'
database = 'membershipdb'
username = 'postgres'
pwd = 'pgdata_0589'
port_id = 5432


def insert(memberId, memberName, memberType, placeofBirth, dateofBirth, gender, fax, employer, hometown, region, tither,
           healthStatus, department, telephone, address, email, maritalStatus, occupation, companyName, postAddress,
           emergencyContact, educationLevel, yearCompleted):
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            dbname=database,
            user=username,
            host=hostname,
            password=pwd,
            port=port_id
        )
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute('DROP TABLE IF EXISTS personal_info')
        create_script = """
                        CREATE TABLE IF NOT EXISTS personal_info
            (
                "memberId" character varying(50) PRIMARY KEY  NOT NULL,
                "memberName" character varying(100)  NOT NULL,
                "memberType" character varying(50)  NOT NULL,
                "placeofBirth" character varying(50)  NOT NULL,
                "dateofBirth" character varying(10) NOT NULL,
                gender character varying(20) NOT NULL,
                fax character varying(20),
                employer character varying(50) NOT NULL,
                hometown character varying(50) NOT NULL,
                region character varying(50) NOT NULL,
                tither character varying(4) NOT NULL,
                "healthStatus" character varying(100) NOT NULL,
                department character varying(50)  NOT NULL,
                telephone bigint NOT NULL,
                address character varying(50) NOT NULL,
                email character varying(50),
                "maritalStatus" character varying(20) NOT NULL,
                occupation character varying(50) NOT NULL,
                "companyName" character varying(50) NOT NULL,
                "postAddress" character varying(20) NOT NULL,
                "emergencyContact" bigint NOT NULL,
                "educationLevel" character varying(50) NOT NULL,
                "yearCompleted" integer
            )
        """
        cur.execute(create_script)
        insert_script = 'INSERT INTO personal_info ("memberId","memberName", "memberType", "placeofBirth", "dateofBirth",' \
                        'gender, fax,employer, hometown, region, tither,"healthStatus", department, telephone, ' \
                        'address, email,"maritalStatus", occupation,"companyName","postAddress","emergencyContact",' \
                        '"educationLevel","yearCompleted")' \
                        'VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        insert_values = (
            memberId, memberName, memberType, placeofBirth, dateofBirth, gender, fax, employer,
            hometown, region, tither, healthStatus, department, telephone, address, email,
            maritalStatus, occupation, companyName, postAddress, emergencyContact, educationLevel, yearCompleted)

        cur.execute(insert_script, insert_values)
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


# def connect():
#     con = sqlite3.connect("grace1.db")
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS member1 (id INTEGER PRIMARY KEY,
#     mem_id,name,mem_type,POB,DOB,gender,department,telephone,address,email,m_stat,occupation,fax,emp,hometown,region,tithe,h_stat,how,comp_name,pst_add,e_contact,edu_level,institution)""")
#
#     con.commit()
#     con.close()
#
# def Insert(mem_id=' ',name=' ',mem_type=' ',POB=' ',DOB=' ',gender=' ',department=' ',telephone=' ',address=' ',email=' ',m_stat=' ',occupation=' ',fax='' ,emp=' ',hometown=' ',region=' ',tithe=' ',h_stat=' ',how=' ',comp_name=' ',pst_add=' ',e_contact=' ',edu_level=' ',institution=' '):
#     con = sqlite3.connect("grace1.db")
#     cur= con.cursor()
#     cur.execute("INSERT INTO member1 VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(mem_id,name,mem_type,POB,DOB,gender,department,telephone,address,email,m_stat,occupation,fax,emp,hometown,region,tithe,h_stat,how,comp_name,pst_add,e_contact,edu_level,institution))
#     con.commit()
#     con.close()
#
# def view():
#     con = sqlite3.connect("grace1.db")
#     cur = con.cursor()
#     cur.execute("SELECT * FROM member1")
#     row=cur.fetchall()
#     return row
#
# def delete(id):
#     con = sqlite3.connect("grace1.db")
#     cur = con.cursor()
#     cur.execute("DELETE FROM member1 WHERE id=?", (id,))
#     con.commit()
#     con.close()
#
# connect()
