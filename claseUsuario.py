from conexion import conexionbbdd,cursor
from functions import busqueda

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
        lista1 = []
        detalle = ["ID","DNI","Nombre","Telefono","Direccion","Situacion","Contraseña","Codigo Pelicula"]
        cursor.execute(f"select * from usuarios where dni = {self.get_dni()}")
        result = cursor.fetchone()
        for i in result:
            lista1.append(i)
        for i,j in zip(detalle,lista1):
            print(f"{i} : {j}")
    
    def modificarDatos(self,tipo,dato):
     on = 1
     while on == 1:   
        try :
            if tipo == 1 : #telefono
                if dato.isdecimal(): 
                    sql2 = f"update usuarios set telefono = {dato} where dni = {self.get_dni()}"
                    cursor.execute(sql2)
                    conexionbbdd.commit()
                    print("Teléfono modificado con éxito")
                else:
                    print("No es un número entero")
                on = 0
            elif tipo == 2:
                sql3 = f"update usuarios set direccion = '{dato}' where dni = {self.get_dni()} "
                cursor.execute(sql3)
                conexionbbdd.commit()
                print("Dirección modificada con éxito")
                on = 0
            else:
                print("Ingrese valores correctos)")
        except ValueError:
            print("Ingrese datos correctos")
            
    def modifSitu(self):
        cursor.execute(f"update usuarios set situacion = 'L' where dni = {self.get_dni()}")
        conexionbbdd.commit()


    def darseDeAlta(self,dni):
        valor1 = busqueda(dni)
        if valor1 == [False]:
            sql = "insert into usuarios (dni,nombre,telefono,direccion,situacion,contrasenia,codigo_peli) VALUES (%s , %s ,%s ,%s ,%s ,%s, %s)"
            val = (self.get_dni(),self.get_nombre(),self.get_telefono(),self.get_direccion(),self.get_situacion(),self.get_contrasenia(),self.get_codigo())
            cursor.execute(sql,val)
            conexionbbdd.commit()
            print(f"¡Bienvenido/a {self.get_nombre()}!\nYa creaste tu Usuario (:")
        else:
            print("Ya esta registrado en la bbdd")
    
    def darseDeBaja(self):
        cursor.execute(f"select situacion from usuarios where dni = {self.get_dni()} ")
        sit = cursor.fetchall()
        valor = 1
        for i in sit:
            valor = i
            break
        sitstr = str(valor[0])
        on = 1
        while on == 1:
            if sitstr == "L":
                sql = f"update usuarios set situacion = 'B' where dni = {self.get_dni()} "
                cursor.execute(sql)
                conexionbbdd.commit()
                print("Usuario dado de baja satisfactoriamente")
                print("Gracias por haber sido parte de nuestro amado VideoClub ♥\nAbrazo..")
                quit()
            elif sitstr == "A":
                print("No puede darse de baja, tiene una pelicula Alquilada")
                on = 0
            elif sitstr == "B":
                print("Usted ya se encuentra dado de baja")
                on = 0
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
        try:
            nombresPeli = []
            cursor.execute("select nombre from peliculas")
            resulnombre = cursor.fetchall()
            for i in resulnombre:
                for j in i :
                    nombresPeli.append(j.lower())
            if str(peli) in str(nombresPeli) :
                #tb pelicula
                cursor.execute(f"select situacion from peliculas where nombre = '{peli}'")
                global sitPeli
                sitPeli1 = cursor.fetchone()
                for i in sitPeli1:
                    break
                sitPeli = str(i[0]) # situacion Pelicula
                cursor.execute(f"select codigo_peli,id from peliculas where nombre = '{peli}'")
                resultado = cursor.fetchall()
                for i in resultado:
                    break
                global resulint
                resulint = int(i[0]) #codigo pelicula
                #tb usuario
                cursor.execute(f"select id from usuarios where dni = {self.get_dni()}")
                resultado2 = cursor.fetchone()
                resulint2 = int(resultado2[0]) #id usuario
                #tb transacciones
                cursor.execute("select date_format(now(),'%Y-%m-%d %h:%i:%s %p' )")
                fecha = cursor.fetchone()
                formatfecha = str(fecha[0]) # formato fecha iyec sql
                #ALQUILER
                if tipo == 1 and busqueda(self.get_dni())[1][5] == "L" and sitPeli == "L" : #alquiler 
                    #update tb usuario column codigo_peli
                    sql = f"update usuarios set codigo_peli = {resulint}, situacion = 'A' where dni = {self.get_dni()}"
                    cursor.execute(sql)
                    conexionbbdd.commit()
                    print("Pelicula Alquilada con éxito\n")
                    #update tb peliculas column dni_usuario
                    sql2 = f"update peliculas set dni_usuario = {self.get_dni()} , situacion = 'A' where codigo_peli = {resulint}"
                    cursor.execute(sql2)
                    conexionbbdd.commit()
                    #update tb transacciones column usuario_id , pelicula_id , tipo "Alquiler"
                    sql3 = "insert into transacciones (fecha,tipo,usuario_id,pelicula_id) values (%s ,%s ,%s ,%s)"
                    val = (formatfecha,"Alquiler", resulint2 ,int(i[1]))
                    cursor.execute(sql3,val)
                    conexionbbdd.commit()
                #DEVOLUCION
                elif tipo == 2 and busqueda(self.get_dni())[1][5] == "A" and sitPeli == "A" and busqueda(self.get_dni())[1][7] == resulint : #devolucion
                    #update tb usuario column codigo_peli
                    sql = f"update usuarios set codigo_peli = NULL, situacion = 'L' where dni = {self.get_dni()}"
                    cursor.execute(sql)
                    conexionbbdd.commit()   
                    print("Devolución Exitosa\n")
                    #update tb peliculas column dni_usuario
                    sql2 = f"update peliculas set dni_usuario = NULL , situacion = 'L' where codigo_peli = {resulint}"
                    cursor.execute(sql2)
                    conexionbbdd.commit()
                    #update tb transacciones - registrar devolucion
                    sql3 = "insert into transacciones (fecha,tipo,usuario_id,pelicula_id) values (%s ,%s ,%s ,%s)"
                    val = (formatfecha,"Devolución", resulint2 ,int(i[1]))
                    cursor.execute(sql3,val)
                    conexionbbdd.commit()
                else:
                    print("No se puede completar la operación\n")
            else:
                print("La pelicula ingresada no se encuentra en nuestro VideoClub\n")
        except ValueError:
            print("Ingrese caracteres correctos")
        
#user1 = Usuarios(39909651,"Julieta",1136241814,"Rivadavia 1500","hola")
#user1.verTodas()
#user1.verDisponibles()
#user1.AlquilaryDevolverPeli("avengers",2)
#user1.verDatos()
""" ursor.execute("select date_format(now(),'%d-%m-%Y %h:%i:%s %p' )")
fecha = cursor.fetchone()
formatfecha = str(fecha[0])
print(formatfecha) """
#user1.modificarDatos(1,156165165)
#user1.darseDeBaja()
#user2 = Usuarios(96587465,"Roma",965815,"Olivieri 9653")
#user2.darseDeAlta()
#user3 = Usuarios(78785,"Roma",965815,"Olivieri 9653")
#user3.darseDeAlta()