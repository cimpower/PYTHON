import  sqlite3

# connect to the database.
conn  =  sqlite3 . connect ( 'mydatabase.db' )
# defining a cursor
cursor  =  conn . cursor ()

# creating the table (schema) agent_master
cursor . execute ( """
CREATE TABLE agent_master(agent_code char(6),
agent_name char(40),working_area char(35),
commission decimal(10,2),phone_no char(15) NULL);
""" )
print("\nagent_master file has created.") 
# disconnecting ...
conn . close ()
print("\nThe SQLite connection is closed.")