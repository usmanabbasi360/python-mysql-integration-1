import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='your database name',
                                         user='root',
                                         password='******')

    #here we are creating a table
    mySql_Create_Table_Query = """CREATE TABLE laptop ( 
                             id int NOT NULL,
                             name varchar(250) NOT NULL,
                             price float NOT NULL,
                             PRIMARY KEY (id)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
