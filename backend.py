from mysql.connector import connect, Error


class Database:

    def __init__(self,host,user,passwd,db):
        conn = connect(host=host,user=user,password=passwd,database=db)
        print(conn)
        cur= conn.cursor()
        cur.execute(
                "CREATE TABLE IF NOT EXISTS studentd(regid INT NOT NULL AUTO_INCREMENT PRIMARY KEY, roll INT,name TEXT,dob DATE,"
                "gender TEXT)")
        conn.commit()
        conn.close()

    def insert(self, roll, name, dob, gender):
        conn = connect(user='zayerwali',host="localhost",passwd="Z@zayer7006", database='studentdb')
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO studentd(roll,name,dob,gender) VALUES( %s, %s, %s, %s)", (roll, name, dob, gender))
        conn.commit()
        conn.close()

    def view(self):
        conn = connect(user='zayerwali',host="localhost",passwd="Z@zayer7006", database='studentdb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM studentd")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(self, roll="", name="", dob="", gender=""):
        conn = connect(user='zayerwali',host="localhost",passwd="Z@zayer7006", database='studentdb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM studentd WHERE roll =%s OR name =%s OR dob =%s OR gender =%s", (roll, name, dob, gender))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(self, regid):
        conn = connect(user='zayerwali',host="localhost",passwd="Z@zayer7006", database='studentdb')
        cur = conn.cursor()
        cur.execute("DELETE FROM studentd where regid =%s", (regid,))
        conn.commit()
        conn.close()

    def update(self, regid, roll, name, dob, gender):
        conn = connect(user='zayerwali',host="localhost",passwd="Z@zayer7006", database='studentdb')
        cur = conn.cursor()
        cur.execute("UPDATE studentd SET roll =%s,name=%s,dob=%s,gender=%s WHERE regid=%s", (roll, name, dob, gender, regid))
        conn.commit()
        conn.close()

