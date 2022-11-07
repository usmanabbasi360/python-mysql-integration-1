import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='your database name',
                                         user='your user name - by default is "root"',
                                         password='*******')

    mySql_insert_query = """INSERT INTO laptop (id, name, price) VALUES (1, 'Lenovo', 786)"""

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
