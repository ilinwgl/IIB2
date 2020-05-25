import mysql.connector
from mysql.connector import Error

def connectMyDatabase():
    try:
        connection = mysql.connector.connect(host='localhost',
                                 database='demonstrator',
                                 user='root',
                                 password='root')
        if connection.is_connected():
           db_Info = connection.get_server_info()
           print("Connected to MySQL database... MySQL Server version on ",db_Info)
           return connection
    except Error as e :
        print ("Error while connecting to MySQL", e)
        

def insertBauleiter(username, password):
    connection = connectMyDatabase()
    try:
        cursor = connection.cursor(prepared=True)
        sql_insert_query = """INSERT INTO bauleiter
                          (blt_name, blt_vorname, blt_username,blt_passwort ) VALUES ('testvor', 'testnach', %s,%s)""" # mehrzeilige
        insert_tuple = (username, password)
        result  = cursor.execute(sql_insert_query, insert_tuple)
        connection.commit()
        print ("Record inserted successfully into Bauteliter table")
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        #closing database connection
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def insertData(sql_insert,insert_tuple):
    connection = connectMyDatabase()
    try:
        cursor = connection.cursor()
        result  = cursor.execute(sql_insert, insert_tuple)
        connection.commit()
        print ("Record inserted successfully ")
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def getAll(sql_select_Query):
    mySQLconnection = connectMyDatabase()
    try:
        cursor = mySQLconnection .cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total number of rows in python_developers is - ", cursor.rowcount)
        print ("Printing each row's column values i.e.  developer record")
        cursor.close()
        if (mySQLconnection.is_connected()):
            mySQLconnection.close()
    except Error as e :
        print ("Error while reading from MySQL", e)
    finally:
        return records
        print("MySQL connection is closed")

def getOne(sql_select_Query):
    mySQLconnection = connectMyDatabase()
    try:
        cursor = mySQLconnection .cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchone()
        print("Total number of rows in python_developers is - ", cursor.rowcount)
        print ("Printing each row's column values i.e.  developer record")
        cursor.close()
        if (mySQLconnection.is_connected()):
            mySQLconnection.close()
    except Error as e :
        print ("Error while reading from MySQL", e)
    finally:
        return records
        print("MySQL connection is closed")

def getBauleiterDeteils(ID):
    mySQLconnection = connectMyDatabase()
    try:       
        cursor = mySQLconnection .cursor()
        sql_select_Query = "select * from bauleiter where blt_id = %s"
        cursor.execute(sql_select_Query, (ID,))
        records = cursor.fetchall()
        print ("Printing each row's column values i.e.  developer record")
        for row in records:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Vorname  = ", row[2])
            print("Username = ", row[3], "\n")
        cursor.close()
    except Error as e :
        print ("Error while reading from MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
            print("MySQL connection is closed")
            



def getBauleiterLogin(username):
    mySQLconnection = connectMyDatabase()
    try:       
        cursor = mySQLconnection .cursor()
        sql_select_Query = "select * from bauleiter where blt_username = %s"
        cursor.execute(sql_select_Query, (username,))
        record = cursor.fetchone()
        print ("Printing each row's column values i.e.  developer record")
      
        cursor.close()
        
    except Error as e :
        print ("Error while reading from MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
            print("MySQL connection is closed")
        return record
            


def insertGebaude( plz, strasse,hausnummer,guid,geb_ort):
    connection = connectMyDatabase()
    try:   
        cursor = connection.cursor(prepared=True)
        sql_insert_query = """INSERT INTO gebaeude
                          ( geb_plz, geb_strasse, geb_hausnummer, geb_guid, geb_ort) VALUES (%s,%s,%s,%s,%s)""" # mehrzeilige
        insert_tuple = ( plz, strasse,hausnummer,guid,geb_ort)
        result  = cursor.execute(sql_insert_query, insert_tuple)
        connection.commit()
        print ("Record inserted successfully into Bauteliter table")
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            


def updateTable( tablename, spalte , value , w_spalte , w_value ):
    connection = connectMyDatabase()
    try:   
        cursor = connection.cursor(prepared=True)
        sql_insert_query = "UPDATE "+ tablename + " SET " + spalte + "= %s WHERE "+w_spalte+" = %s"
        # table name can't be parameterizes in a prepared statement. 
        update_tuple = ( value , w_value) 
        result  = cursor.execute(sql_insert_query , update_tuple)
        connection.commit()
        print ("Record updates successfully ")
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to update MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            
updateTable (tablename = "gebaeude", spalte = "geb_blt_id",value = 1, w_spalte = "geb_id", w_value = 9)




def deletedata( tablename,  w_spalte , w_value ):
    connection = connectMyDatabase()
    try:   
        cursor = connection.cursor(prepared=True)
        """Delete from mobile where id = 3"""
        sql_insert_query = "DELETE FROM "+ tablename +  " WHERE "+ w_spalte +" = %s"
        # table name can't be parameterizes in a prepared statement. 
        update_tuple = (w_value,) 
        result  = cursor.execute(sql_insert_query , update_tuple)
        connection.commit()
        print ("Record updates successfully ")
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to update MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            



import datetime

def multiusingSelect(table = "multiusingbesp"):
    mySQLconnection = connectMyDatabase()
    try:
        timestamp1 = datetime.datetime.now()
        cursor = mySQLconnection.cursor()
        sql_select_Query = "select * from "+ table
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print ("Printing each row's column values i.e.  developer record")
        for row in records:
            print("Id = ", row[0] )
            print("Vorname = ", row[1])
            print("Nachname = ", row[3], "\n")  
        cursor.close()
    except Error as e :
        print ("Error while connecting to MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection .is_connected()):
            mySQLconnection.close()
            print("MySQL connection is closed")
            return timestamp1
    
    
def multiusingUpdate(ID, timestampSel, value_new = "Meliing"):
    mySQLconnection = connectMyDatabase()
    try:
        cursor = mySQLconnection.cursor(prepared=True)
        sql_insert_query = """UPDATE multiusingbesp SET
                          Vorname = %s WHERE ID = %s""" # mehrzeilige
        insert_tuple = ( value_new, ID)
        result  = cursor.execute(sql_insert_query, insert_tuple)
        cursor.execute("select Timestamp_vorname from multiusingbesp where ID = %s", (ID,))
        row_time_old = cursor.fetchone()
        print ("last edited at: ", row_time_old[0])
        if (timestampSel > row_time_old[0]):   
            timestamp2 = datetime.datetime.now()
            updatetimestamp = """UPDATE multiusingbesp SET
                          Timestamp_vorname = %s WHERE ID = %s""" # mehrzeilige
            cursor.execute(updatetimestamp, (timestamp2, ID)) 
            mySQLconnection.commit()
            print ("Record inserted successfully into python_users table at time " , timestamp2)
        else:
            print ("Database is being edited by others, please try again")
    except mysql.connector.Error as error :
        mySQLconnection.rollback()
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):          
            cursor.close()
            mySQLconnection.close()
            print("MySQL connection is closed")




