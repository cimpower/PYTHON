import  sqlite3

conn  =  sqlite3 . connect ( 'mydatabase.db' )
cursor  =  conn.cursor ()
#create the salesman table 
cursor.execute("CREATE TABLE salesman_3(salesman_id n(5), name char(30), city char(35), commission decimal(7,2));")
# Insert records
rows = [(5001,'James Hoog', 'New York', 0.15),
         (5002,'Nail Knite', 'Paris', 0.25),
         (5003,'Pit Alex', 'London', 0.15),
         (5004,'Mc Lyon', 'Paris', 0.35),
         (5005,'Paul Adam', 'Rome', 0.45)]
                   
cursor . executemany ( """
INSERT INTO salesman_3 (salesman_id, name, city, commission)
VALUES (?,?,?,?)
""" , rows )
print ( 'Data entered successfully.' )
conn.commit ()
if (conn):
  conn.close()
  print("\nThe SQLite connection is closed.")