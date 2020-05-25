#!/usr/bin/env python
# coding: utf-8

# In[1]:


antwort = input("Was ist der Sinn des Lebens?")
if antwort =="42":
    print ("Falscher Film!")
else:
    print(antwort + "ist eine interessante Antwort.")


# In[2]:


antwort = input("Was ist der Sinn des Lebens?")
if antwort =="42":
    print ("Falscher Film!")
elif antwort == "Geld":
    print("Wenn Sie meinen.")


# In[3]:


antwort = input("Was ist der Sinn des Lebens ? ")
if antwort == "42" :
    print("Falscher Film!")
else:
    if antwort == "Geld" :
        print("Wenn Sie meinen.")  # Achtung: Eindrücken!!


# In[4]:


bsp = (1,("a","b"), "Spam")
for e in bsp:print (e * 3)


# In[5]:


bsp = [1,("a","b"), "Spam"]
for e in bsp:print (e * 3)


# In[6]:


def dividiere(x,y): return(x/y)
tests=((42,2),(3,1),(4,5))
try:
    for a,b in tests:
        print("Division"),
        print(a,b),
        print("mit Resultat"),
        print (dividiere(a,b))
except ZeroDivisionError:
    print("\n AUSNAHME: Bitte nicht durch 0 teilen.")
else: print("Alles unter Kontrolle")
    
print("\n Bye.")


# In[7]:


def dividiere(x,y): return(x/y)
tests=((42,2),(3,0),(4,5))
try:
    for a,b in tests:
        print("Division"),
        print(a,b),
        print("mit Resultat"),
        print (dividiere(a,b))
finally:
    print("\n Aufraeumen...")
    
print("\n Bye.")


# In[8]:


def TuNix():pass


# In[9]:


TuNix


# In[10]:


print (TuNix())


# In[11]:


def f1(x,y):
    "call by value"
    print("Parameter x :", x)
    print("Parameter y :", y)
    x = x*3
    y = y*3
    print("Neuer Parameter x :", x)
    print("Neuer Parameter y :", y)
    
x = 1
y = 2
f1(x,y)
print ("x = ",x, " y = ", y)


# In[12]:


def f2(x,y):
    "veraenderliche Datentypen"
    print("Parameter x :", x)
    print("Parameter y :", y)
    x[0] = "Hoppla"
    y.append (42)
    print("Neuer Parameter x :", x)
    print("Neuer Parameter y :", y)
    print ("x_id funktion : ",id(x))
    print ("y_id funktion : ",id(y))
    
x = [1,2,3]
y = [11,12,13]
print ("x_id main : ",id(x))
print ("y_id main : ",id(y))
f2(x,y)
print ("x = ",x, " y = ", y)
print ("x_id main_2 : ",id(x))
print ("y_id main_2 : ",id(y))


# In[13]:


def f(x):
    a = 2
    return (x+a)

print(f(1))
print(a)


# In[14]:


a = 42
def f(x):
    a = 2
    return (x+a)

print(f(1))
print(a)


# In[15]:


def f(antwort = 42): print(antwort)
    
f()
f("Kein Plan!")


# In[16]:


def verkette (a, b = []):
    b.append("Spam")
    print (id(b))
    return a+b
print ("verkette id: " , id (verkette([1])))
print(verkette([1]))
print(verkette([1]))
print ("verkette id: " , id (verkette([1])))


# In[17]:


def verkette (a, b = None):
    if b==None:
        b=[]
    b.append("Spam")
    return a+b

print(verkette([1]))
print(verkette([1]))


# In[18]:


def f(*parameter): print(parameter)

f(1,2,3)


# In[19]:


f("IIB2","SoSe2019")


# In[20]:


f(("IIB2","SoSe2019"))


# In[21]:


def f(**schluesselworte): print(schluesselworte)

f(fruehstueck = "nutella")


# In[22]:


f(fruehstueck = "nutella", mittag = "spagetti")


# In[23]:


f(x=23, y= 42, dessert = (10, "spagettieis"))


# In[24]:


class Foo:
    variable = "Klasse"
    def __init__(self, name = "NN"):
        self.variable = name
    def zeigeVariable(self):
        print("Klasse: ", Foo.variable),
        print("Instanz: ", self.variable)


# In[25]:


instanz = Foo("Spam")
Foo.variable


# In[26]:


instanz.variable


# In[27]:


instanz.zeigeVariable()


# In[28]:


class Stack:
    def __init__(self): # Konstruktor
        self.liste =[]
    def isEmpty(self):
        return len(self.liste) ==0
    def push(self,element):
        self.liste.append(element)
    def pop(self):
        if not self.isEmpty():
            del self.liste[-1] # del Element loeschen 
    def top(self):
        if not self.isEmpty():
            return self.liste[-1]


# In[29]:


Stack() #Klasse


# In[30]:


s = Stack() #Instanz
print(s.isEmpty())


# In[31]:


s.push(42)
s.top()


# In[32]:


print(s.isEmpty())


# In[33]:


s.pop()
s.top()
print (s.isEmpty())


# In[34]:


class PeepingStack(Stack):
    def peep(self,i):
        return self.liste[i]
    
pstack = PeepingStack()
pstack.push(1)
pstack.push(2)

print(pstack.peep(0))
print(pstack.peep(1))


# In[35]:


class PeepingStack(Stack):
    def peep(self,i):
        return self.liste[i]
class Spam:
    def top(self): print("Spam!")
class Mehrfach(PeepingStack, Spam):
    pass
class MehrdachX(Spam,PeepingStack):
    pass

a = Mehrfach()
a.push(42)
a.top()
    


# In[36]:


b= MehrdachX()
b.push(42)
b.top()


# In[37]:


import mysql.connector


# In[38]:


mydb = mysql.connector.connect(
    host="localhost",
    user="root", # dein Benutzername
    passwd="root", # dein Passwort
    database="test"
)

print(mydb)


# In[39]:


mydb = mysql.connector.connect(
    host="localhost",
    user="root", # dein Benutzername
    passwd="root", # dein Passwort
    database="test"
)

print(mydb)


# In[40]:


import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                             database='test',
                             user='root',
                             password='root')
    if connection.is_connected():
       db_Info = connection.get_server_info()
       print("Connected to MySQL database... MySQL Server version on ",db_Info)
       cursor = connection.cursor()
       cursor.execute("select database();")
       record = cursor.fetchone()
       print ("Your connected to - ", record)
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


# In[41]:


try:
    mySQLconnection = mysql.connector.connect(host='localhost',
                             database='demonstrator',
                             user='root',
                             password='root')
    sql_select_Query = "select * from bauleiter"
    cursor = mySQLconnection .cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in python_developers is - ", cursor.rowcount)
    print ("Printing each row's column values i.e.  developer record")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Vorname  = ", row[2])
        print("Username = ", row[3], "\n")
    cursor.close()
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(mySQLconnection .is_connected()):
        connection.close()
        print("MySQL connection is closed")


# In[42]:


def getBauleiterDeteils(ID):
    try:
        mySQLconnection = mysql.connector.connect(host='localhost',
                                 database='demonstrator',
                                 user='root',
                                 password='root')
       
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
        print ("Error while connecting to MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection .is_connected()):
            connection.close()
            print("MySQL connection is closed")
            
getBauleiterDeteils(ID = 1)


# In[43]:


def insertPythonVaribleInTable( Name, vorname, username):
    try:
        connection = mysql.connector.connect(host='localhost',
                                 database='demonstrator',
                                 user='root',
                                 password='root')
        cursor = connection.cursor(prepared=True)
        sql_insert_query = """INSERT INTO bauleiter
                          ( blt_name, blt_vorname, blt_username) VALUES (%s,%s,%s)""" # mehrzeilige
        insert_tuple = ( Name, vorname, username)
        result  = cursor.execute(sql_insert_query, insert_tuple)
        connection.commit()
        print ("Record inserted successfully into python_users table")
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            
insertPythonVaribleInTable("Bach", "Johann", "JSBach" )


# In[44]:


import mysql.connector
from mysql.connector import Error
import datetime

def multiusingSelect(database = "multiusingbesp", mySQLconnection = None):
    try:
        timestamp1 = datetime.datetime.now()
        cursor = mySQLconnection.cursor()
        sql_select_Query = "select * from "+ database
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
            connection.close()
            print("MySQL connection is closed")
            return timestamp1
    
    
def multiusingUpdate(ID, connection , timestampSel, value_new = "Meliing"):
    try:
        
        cursor = connection.cursor(prepared=True)
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
            connection.commit()
            print ("Record inserted successfully into python_users table at time " , timestamp2)
        else:
            print ("Database is being edited by others, please try again")
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):          
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def connecting():
    connection = mysql.connector.connect(host='localhost',
                                 database='demonstrator',
                                 user='root',
                                 password='root')

    return connection


# In[45]:


timestampSelect2 = multiusingSelect("multiusingbesp",connecting())


# In[46]:


timestampSelect1 = multiusingSelect("multiusingbesp",connecting())


# In[47]:


multiusingUpdate (1,connecting(), timestampSelect1, value_new = "tata2")


# In[48]:


multiusingUpdate (1,connecting(), timestampSelect2, value_new = "tata1")


# In[49]:


try:
    conn =  mysql.connector.connect(host='localhost',
                                 database='demonstrator',
                                 user='root',
                                 password='root')
    cursor = conn.cursor(prepared=True)
    # Delete record now
    sql_Delete_query = """Delete from bauleiter where blt_id = %s"""
    records_to_be_deleted = [(4,),(6,)]
    cursor.executemany(sql_Delete_query,records_to_be_deleted)
    conn.commit()
    print("\n ", cursor.rowcount, "Record Deleted successfully ")
except mysql.connector.Error as error:
    print("Failed to Delete records from database table: {}".format(error))
finally:
    # closing database connection.
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("MySQL connection is closed")


# In[50]:


wort = "IIB2isAwesome!"
print("Indexing:", wort[0])
print("Slicing:", wort[:4], wort[4:6], wort[6:])
print (len(wort))


# In[51]:


liste = [1,2,3]
liste.insert(2, "vier")
print (liste)
liste.append(1)
print (liste)
liste.remove(1)
print (liste)
liste.remove(4)


# In[52]:


de2eng = {}
de2eng["eins"] = "one"
de2eng["drei"] = "three"
de2eng[2] = "two"
de2eng


# In[53]:


print(de2eng["eins"])
del de2eng[2]
print(de2eng)
de2eng["drei"] = 3
print(de2eng)


# In[54]:


print(de2eng.keys())
print(de2eng.values())
print(de2eng.items())


# In[55]:


import keyword
keyword.kwlist


# In[56]:


def changea(a):
    print ("id2:", id(a))
    a+=" world!"
    print ("id3:", id(a))
    print (a)
a = "hello"   
print("id1:", id(a))
changea(a)
print(a)
print ("id4:", id(a))


# In[57]:


def changeliste(c):
    c.append(5)
    print ("lokal c:", c)
c = [1,2]
d =[3,4]
changeliste(d)
print ("globale c:", c)

print (d)


# In[58]:


i = 1
i++

