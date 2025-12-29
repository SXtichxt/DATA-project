import sqlite3

connection = sqlite3.connect("SQlite/Practice.db")
print("connect to Database succeed\n")

cursor = connection.execute("SELECT Firstname, Lastname, Email FROM customers;")

for row in cursor:
    print("Customer ID :", row[0], row[1], row[2])
connection.close()
