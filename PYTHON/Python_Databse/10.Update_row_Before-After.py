import sqlite3 
from sqlite3 import Error 

def sql_connection():
    try:
      conn = sqlite3.connect('mydatabase.db')
      return conn
    except Error:
      print(Error) 

def sql_table(conn):
    cursorObj = conn.cursor()
# Create the table
    cursorObj.execute("CREATE TABLE salesman_6(salesman_id n(5), name char(30), city char(35), commission decimal(7,2));")
# Insert records
    cursorObj.executescript("""
    INSERT INTO salesman_6 VALUES(5001,'James Hoog', 'New York', 0.15);
    INSERT INTO salesman_6 VALUES(5002,'Nail Knite', 'Paris', 0.25);
    INSERT INTO salesman_6 VALUES(5003,'Pit Alex', 'London', 0.15);
    INSERT INTO salesman_6 VALUES(5004,'Mc Lyon', 'Paris', 0.35);
    INSERT INTO salesman_6 VALUES(5005,'Paul Adam', 'Rome', 0.45);
    """)    
#Muestreo antes del UPDATE
    cursorObj.execute("SELECT * FROM salesman_6")
    rows = cursorObj.fetchall()
    print("Agent details:")
    for row in rows:
        print(row)

#UPDATE
    print("\nUpdate commission .15 to .45 where id is 5003:")
    sql_update_query = """Update salesman_6 set commission = .45 where salesman_id = 5003"""
    cursorObj.execute(sql_update_query)
    conn.commit()

#Muestreo después del UPDATE
    print("Record Updated successfully ")    
    cursorObj.execute("SELECT * FROM salesman_6")
    rows = cursorObj.fetchall()
    print("\nAfter updating Agent details:")
    for row in rows:
        print(row)

sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
  sqllite_conn.close()
  print("\nThe SQLite connection is closed.")