import mysql.connector
conexionbbdd = mysql.connector.connect(host="localhost",user="root",password="" , database = "videoclub")
cursor = conexionbbdd.cursor(buffered=True)
if conexionbbdd:
    print("Conectado con Base de Datos")