import mysql.connector

def connect():

    return mysql.connector.connect(

        host="localhost",

        user="root",

        password="",

        database="network_monitor"

    )