import mysql.connector
from mysql.connector import Error
import datetime 

def connectMyDatabase():
    try:
        connection = mysql.connector.connect(host='localhost',
                                 database='IIB2_HUE1_Gruppe6',
                                 user='root',
                                 password='9999')
        if connection.is_connected():
           db_Info = connection.get_server_info()
           print("Connected to MySQL database... MySQL Server version on ",db_Info)
           return connection
    except Error as e :
        print ("Error while connecting to MySQL", e)

        
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


def updateTable(tablename, spalte , value , w_spalte , w_value ):
    connection = connectMyDatabase()
    try:   
        cursor = connection.cursor()
        sql_insert_query = "UPDATE "+ tablename + " SET " + spalte + " = %s WHERE "+w_spalte+" = %s"
        # table name can't be parameterizes in a prepared statement. 
        update_tuple = (value , w_value) 
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


def deletedata( tablename,  w_spalte , w_value ):
    connection = connectMyDatabase()
    try:   
        cursor = connection.cursor()
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
            

def insertPersonen(name, vorname, username, password, beruf):
    connection = connectMyDatabase()
    try:
        cursor = connection.cursor()
        sql_insert_query = """INSERT INTO Personen (per_name, per_vorname, per_username, per_passwort, per_beruf) VALUES (%s,%s,%s,%s,%s)""" # mehrzeilige
        insert_tuple = (name, vorname, username, password, beruf)
        result  = cursor.execute(sql_insert_query, insert_tuple)
        connection.commit()
        print ("Record inserted successfully into Personen table")
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        #closing database connection
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def getPersonenDeteils(ID):
    mySQLconnection = connectMyDatabase()
    try:       
        cursor = mySQLconnection .cursor()
        sql_select_Query = "select * from  personen where per_id = %s"
        cursor.execute(sql_select_Query, (ID,))
        records = cursor.fetchall()
        print ("Printing each row's column values i.e.  developer record")
        for row in records:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Vorname  = ", row[2])
            print("Username = ", row[3])
            print("Beruf = ", row[5], "\n")
        cursor.close()
    except Error as e :
        print ("Error while reading from MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
            print("MySQL connection is closed")
            

def getPersonenLogin(username):
    mySQLconnection = connectMyDatabase()
    try:       
        cursor = mySQLconnection.cursor()
        sql_select_Query = "select * from personen where per_username = %s"
        cursor.execute(sql_select_Query, (username,))
        record = cursor.fetchone()
        cursor.close()
        
    except Error as e :
        print ("Error while reading from MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
            print("MySQL connection is closed")
        return record
            

def insertGebaude(name, ort, plz, strasse, hausnummer, guid):
    connection = connectMyDatabase()
    try:   
        cursor = connection.cursor(prepared=True)
        sql_insert_query = """INSERT INTO gebaeude
                          ( ge_name, ge_ort, ge_plz, ge_strasse, ge_hausnummer, ge_ifc_guid) VALUES (%s,%s,%s,%s,%s,%s)""" # mehrzeilige
        insert_tuple = (name, ort, plz, strasse, hausnummer, guid)
        result  = cursor.execute(sql_insert_query, insert_tuple)
        connection.commit()
        print ("Record inserted successfully into Gebäude table")
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
 

def multiusingSelect(table):
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
    
    
def multiusingUpdate(ID, timestampSel, value_new_vor, value_new_nach):
    mySQLconnection = connectMyDatabase()
    try:
        cursor = mySQLconnection.cursor()
        sql_insert_query = """UPDATE multiusing SET
                          mul_vorname = %s, mul_name = %s WHERE mul_id = %s""" # mehrzeilige
        insert_tuple1 = ( value_new_vor, value_new_nach, ID)
        result  = cursor.execute(sql_insert_query, insert_tuple1)
        cursor.execute("select mul_timestamp_vorname from multiusing where mul_id = %s", (ID,))
        row_time_old = cursor.fetchone()

        if(row_time_old == None):
            timestamp1 = datetime.datetime.now()
            sql_query = "insert into multiusing (mul_id, mul_vorname, mul_timestamp_vorname, mul_name) values (%s,%s,%s,%s)"
            insert_tuple2 = (ID, value_new_vor, timestamp1, value_new_nach)
            cursor.execute(sql_query, insert_tuple2)
            mySQLconnection.commit()
        elif (timestampSel > row_time_old[0]):   
            timestamp2 = datetime.datetime.now()
            updatetimestamp = """UPDATE multiusing SET
                          mul_timestamp_vorname = %s WHERE mul_id = %s""" # mehrzeilige
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
