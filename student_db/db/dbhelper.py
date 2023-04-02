from mysql.connector import connect

conn:object = None
cursor:object = None

def db_connect()->object:
    return connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="student"
    )
 
def getall(table:str)->list:
    data:list = []
    sql:str = f"SELECT * FROM `{table}`"
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    return data

def getrecord(table:str,*args)->dict: #args a list parameter to a func
    data:dict = {}
    sql:str = f"SELECT * FROM `{table}` WHERE `id`= %s"
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql,args[0])
    data = cursor.fetchone()
    cursor.close()
    return data

def addrecord(table:str,**kwargs)->bool: #**kwargs is a list of dictionary parameters
    ok:bool = False
    values:list = list(kwargs.values())
    keys:list = list(kwargs.keys())
    fields:str = "`,`".join(keys)
    data:str = "','".join(values)

    sql:str = f"INSERT INTO `{table}`(`{fields}`) VALUES('{data}')"

    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    if cursor.rowcount>0:
        ok = True
        conn.commit() #finally write the data to the table in the db
    cursor.close()

    return ok

def updaterecord(table:str,**kwargs)->bool:
    ok:bool = False
    values:list = list(kwargs.values())
    keys:list = list(kwargs.keys())
    flds:list = []
    for i in range(1,len(values)):
        flds.append("`"+keys[i]+"`='"+values[i]+"'")
    fields:str = ",".join(flds)
    sql:str = f"UPDATE `{table}` SET {fields} WHERE `id` = {values[0]}" 

    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    if cursor.rowcount>0:
        ok = True
        conn.commit() #finally write the data to the table in the db
    cursor.close()
    return ok

def deleterecord(table:str,*args)->bool:
    ok:bool = False
    sql:str = f"DELETE FROM `{table}` WHERE `id` = %s"
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(sql,args[0])
    if cursor.rowcount>0:
        ok = True
        conn.commit()
    cursor.close
    return ok


def main()->None:
    ok:bool = getall('student')
    print(ok)

if __name__ == "__main__":
    main()