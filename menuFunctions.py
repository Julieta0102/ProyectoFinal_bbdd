import mysql.connector
from conexion import conexionbbdd,cursor
from claseUsuario import Usuarios

def busqueda(valor):
        lista1 = []
        cursor.execute("select dni from usuarios")
        result = cursor.fetchall()
        for i in result: #tupla
            for j in i : # saca valores de la tupla
                lista1.append(j) #agrega dni's a lista
        if valor not in lista1: 
            return [False]
        else:
            cursor.execute(f"select * from usuarios where dni = {valor}")
            asd = cursor.fetchone()
            asd2 = [True,asd]
            return asd2

def login():
    on = 1
    while on ==1:
        try:
            login = int(input("Ingrese la opción deseada\n1- Iniciar sesion\n2- Registrarse\n3- Salir\n"))
            if login == 1:
                try:
                    dni = int(input("Ingrese su dni\n"))
                    if busqueda(dni)[0] == True:
                        passw = str(input("Ingrese su contraseña\n"))
                        if busqueda(dni)[1][6] == passw:
                            print(f"¡Bienvenida {(busqueda(dni)[1][2])}!")
                            #llamar funcion menuPrincipal
                        else:
                            print("Contraseña incorrecta")
                    else:
                        print("Usted no está registrado en nuestra base de datos\nPara utilizar nuestro servicio debe REGISTRARSE\n")
                except ValueError:
                    print("Por favor, ingrese carácteres numéricos\n")   
            elif login ==2:
                try:
                    dni = int(input("Ingrese su dni\n"))
                    if busqueda(dni)[0] == True:
                        print("Usted ya se encuentra registrado en nuestra Base de Datos\nInicie sesion para comenzar a operar\n")
                    else:
                        nombre = str(input("Ingrese su nombre\n"))
                        tel = int(input("Ingrese su telefono\n"))
                        dir = str(input("Ingrese su direccion\n"))
                        contra = str(input("Ingrese su contraseña\n"))
                        userAlta = Usuarios(dni,nombre,tel,dir,contra)
                        userAlta.darseDeAlta(dni)
                except ValueError:
                    print("Ingrese carácteres numéricos/alfabéticos, según corresponda")        
            elif login == 3:
                print("Saliendo del programa...\nGracias por usar la Aap")    
                on = 0
                return 
            else:
                print("Ingrese una opción correcta")
        except ValueError:
            print("Por favor, ingrese carácteres numéricos\n")
            
def menuPrincipal():
    on = 1
    while on == 1:
        try:
            pass
            
        except ValueError:
            print("Ingrese carácteres correctos.-")

def menuUsers():
    pass

def menuPelis():
    pass

print(login())