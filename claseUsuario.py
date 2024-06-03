from conexion import conexionbbdd,cursor
from claseVideoClub import VideoClub
import datetime 

class Usuarios():
    def __init__(self,dni,nombre,telefono,direccion):
        self.__dni = dni
        self.__nombre = nombre
        self.__telefono = telefono
        self.__direccion = direccion
        self.__situacion = "L"
        self.__codigo = " "
        
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
        
    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self,newcodigo):
        self.__codigo = newcodigo
        
    #MetodosPropios
    
    def verDatos(self):
        pass
    
    def modificarDatos(self):
        pass
    
    def darseDeAlta(self):
        pass
    
    def darseDeBaja(self):
        pass
    
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
        
    def AlquilarPeli(self,peli):
        #update tb usuarios column codigo_peli
        cursor.execute(f"select codigo_peli,id from peliculas where nombre = {peli}")
        resultado = cursor.fetchall()
        for i in resultado:
            print(i)
        resulint = int(i[0])
        print(resulint)
        sql = f"update usuarios set codigo_peli = {resulint}, situacion = 'A' where dni = {self.get_dni()}"
        cursor.execute(sql)
        conexionbbdd.commit()
        
        #update tb peliculas column dni_usuario
        sql2 = f"update peliculas set dni_usuario = {self.get_dni()} , situacion = 'A' where codigo_peli = {resulint}"
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
        sql3 = "insert into transacciones (fecha,tipo,usuario_id,pelicula_id) values (%s ,%s ,%s ,%s)"
        val = (formatfecha,"Alquiler", resulint2 ,int(i[1]))
        cursor.execute(sql3,val)
        conexionbbdd.commit()
        

    def DevolverPeli(self):
        pass
    
user1 = Usuarios(39909651,"Julieta",1136241814,"Rivadavia 1500")
#user1.verTodas()
#user1.verDisponibles()
user1.AlquilarPeli("'Caperucita Roja'")

""" ursor.execute("select date_format(now(),'%d-%m-%Y %h:%i:%s %p' )")
fecha = cursor.fetchone()
formatfecha = str(fecha[0])
print(formatfecha) """