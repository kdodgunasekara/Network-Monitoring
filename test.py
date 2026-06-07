import mysql.connector

db = mysql.connector.connect(

host="localhost",

user="root",

password="",

database="network_monitor"

)

print("Connected Successfully")