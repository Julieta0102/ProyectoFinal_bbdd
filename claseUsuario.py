from conexion import conexionbbdd,cursor
from main import busqueda

class Usuarios():
    def __init__(self,dni,nombre,telefono,direccion,contrasenia):
        self.__dni = dni
        self.__nombre = nombre
        self.__telefono = telefono
        self.__direccion = direccion
        self.__situacion = "L"
        self.__contrasenia = contrasenia
        self.__codigo = None
        
    def get_dni(self):
        return self.__dni
    
    def set_dni(self,newdni):
        self.__dni = newdni
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,newnombre):
        self.__nombre = newnombre
        
    def get_telefono(self):
        return self.__telefono
    
    def set_telefono(self,newtelefono):
        self.__telefono = newtelefono
        
    def get_direccion(self):
        return self.__direccion
    
    def set_direccion(self,newdireccion):
        self.__direccion = newdireccion
        
    def get_situacion(self):
        return self.__situacion
    
    def set_situacion(self,newsituacion):
        self.__situacion = newsituacion

    def get_contrasenia(self):
        return self.__contrasenia
    
    def set_contrasenia(self,newcontrasenia):
        self.__contrasenia = newcontrasenia 
        
    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self,newcodigo):
        self.__codigo = newcodigo
        
    #MetodosPropios
    
    def verDatos(self):
        cursor.execute("select * from usuarios")
        result = cursor.fetchone()
        print(result)
        cursor.close()
    
    def modificarDatos(self,tipo,dato):
        if tipo == 1 : #telefono
            sql2 = f"update usuarios set telefono = {dato} where dni = {self.get_dni()}"
            cursor.execute(sql2)
            conexionbbdd.commit()
        else:
            sql3 = f"update usuarios set direccion = {dato} where dni = {self.get_dni()} "
            cursor.execute(sql3)
            conexionbbdd.commit()
    
    def darseDeAlta(self):
        valor1 = busqueda(self.get_dni())
        if valor1 == False:
            sql = "insert into usuarios (dni,nombre,telefono,direccion,situacion,codigo_peli) VALUES (%s , %s ,%s ,%s ,%s ,%s)"
            val = (self.get_dni(),self.get_nombre(),self.get_telefono(),self.get_direccion(),self.get_situacion(),self.get_codigo())
            cursor.execute(sql,val)
            conexionbbdd.commit()
        else:
            print("Ya esta resgistrado en la bbdd")
    
    def darseDeBaja(self):
        cursor.execute(f"select situacion from usuarios where {self.get_dni()} ")
        sit = cursor.fetchall()
        valor = 1
        for i in sit:
            valor = i
            break
        sitstr = str(valor[0])
        if sitstr == "L":
            sql = f"update usuarios set situacion = 'B' where dni = {self.get_dni()} "
            cursor.execute(sql)
            conexionbbdd.commit()
        elif sitstr == "A":
            print("No puede darse de baja, tiene una pelicula Alquilada")
        elif sitstr == "B":
            print("Ya esta dado de baja")
        else:
            None
    

    #Metodos sobre Peliculas
    
    def verTodas (self):
        print("Listado de Peliculas:")
        cursor.execute("select nombre,genero from peliculas")
        result = cursor.fetchall()
        for i in result:
            print(i)
    
    def verDisponibles(self):
        print("Peliculas Disponibles:")
        cursor.execute("select nombre,genero from peliculas where situacion = 'L' ")
        result = cursor.fetchall()
        for i in result:
            print(i)
        
    def AlquilaryDevolverPeli(self,peli,tipo):
        #update tb usuarios column codigo_peli
        cursor.execute(f"select codigo_peli,id from peliculas where nombre = {peli}")
        resultado = cursor.fetchall()
        for i in resultado:
            print(i)
        resulint = int(i[0])
        print(resulint)
        if tipo == 1: #alquiler 
            sql = f"update usuarios set codigo_peli = {resulint}, situacion = 'A' where dni = {self.get_dni()}"
            cursor.execute(sql)
            conexionbbdd.commit()
        else: #devolucion
            sql = f"update usuarios set codigo_peli = NULL, situacion = 'L' where dni = {self.get_dni()}"
            cursor.execute(sql)
            conexionbbdd.commit()   
            
        #update tb peliculas column dni_usuario
        if tipo == 1: #alquiler
            sql2 = f"update peliculas set dni_usuario = {self.get_dni()} , situacion = 'A' where codigo_peli = {resulint}"
            cursor.execute(sql2)
            conexionbbdd.commit()
        else: #devolucion
            sql2 = f"update peliculas set dni_usuario = NULL , situacion = 'L' where codigo_peli = {resulint}"
            cursor.execute(sql2)
            conexionbbdd.commit()
        
        #update tb transacciones column usuario_id , pelicula_id , tipo "Alquiler"
        cursor.execute(f"select id from usuarios where dni = {self.get_dni()}")
        resultado2 = cursor.fetchone()
        resulint2 = int(resultado2[0])
        cursor.execute("select date_format(now(),'%Y-%m-%d %h:%i:%s %p' )")
        fecha = cursor.fetchone()
        formatfecha = str(fecha[0])
        print(formatfecha)
        if tipo == 1:
            sql3 = "insert into transacciones (fecha,tipo,usuario_id,pelicula_id) values (%s ,%s ,%s ,%s)"
            val = (formatfecha,"Alquiler", resulint2 ,int(i[1]))
            cursor.execute(sql3,val)
            conexionbbdd.commit()
        else:
            sql3 = "insert into transacciones (fecha,tipo,usuario_id,pelicula_id) values (%s ,%s ,%s ,%s)"
            val = (formatfecha,"Devolución", resulint2 ,int(i[1]))
            cursor.execute(sql3,val)
            conexionbbdd.commit()
        
    
user1 = Usuarios(39909651,"Julieta",1136241814,"Rivadavia 1500")
#user1.verTodas()
#user1.verDisponibles()
#user1.AlquilaryDevolver("'Caperucita Roja'",2)
#user1.verDatos()
""" ursor.execute("select date_format(now(),'%d-%m-%Y %h:%i:%s %p' )")
fecha = cursor.fetchone()
formatfecha = str(fecha[0])
print(formatfecha) """
#user1.modificarDatos(1,156165165)
#user1.darseDeBaja()
#user2 = Usuarios(96587465,"Roma",965815,"Olivieri 9653")
#user2.darseDeAlta()
user3 = Usuarios(78785,"Roma",965815,"Olivieri 9653")
user3.darseDeAlta()