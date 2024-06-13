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
    print("Bienvenido a Videoclub Roma (:")
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
                            Registro = busqueda(dni)[1]
                            userLogin = Usuarios(Registro[1],Registro[2],Registro[3],Registro[4],Registro[6])
                            if busqueda(dni)[1][5]== "B":
                                reac = 1
                                while reac == 1:
                                    try:
                                        reactivar = int(input("Actualmente está dado de baja, desea reactivar su cuenta?\n1- Si\n2- No\n"))
                                        if reactivar == 1:
                                            userLogin.modifSitu()
                                            print("Usuario Reactivado con éxito")
                                            print(f"¡Bienvenido/a nuevamente {(busqueda(dni)[1][2])}!")
                                            reac=0
                                        elif reactivar == 2:
                                            print("Vuelva Prontos")
                                            quit()
                                        else:
                                            print("Ingrese una opción correcta")    
                                    except ValueError:
                                        print("Ingrese un carácter númerico,por favor.")   
                            menuPrincipal(userLogin)
                            
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
                quit()
            else:
                print("Ingrese una opción correcta\n")
        except ValueError:
            print("Por favor, ingrese carácteres numéricos\n")
            
def menuPrincipal(user):
    print("Menu Principal\n")
    on = 1
    while on == 1:
        try:
            princi = int(input("Ingrese la opción deseada\n1- Menu Usuario\n2- Menu Peliculas\n3- Salir\n"))
            if princi == 1:
                menuUsers(user)
            elif princi ==2:
                menuPelis(user)
            elif princi ==3:
                quit()
            else:
                print("Ingrese una opción correcta")                             
        except ValueError:
            print("Ingrese carácteres correctos.-\n")

def menuUsers(user):
    print("Ingresando a Menu Usuario\n")
    on = 1
    while on == 1:
        try:
            menuUser= int(input("Ingrese la opción deseada\n1 - Ver sus datos\n2- Modificar datos\n3- Darse de Baja\n4- Atrás\n5-Salir\n"))
            if menuUser == 1:
                print("Estos son sus datos:\n")
                user.verDatos()
            elif menuUser == 2:
                    dato = int(input("Ingrese:\n1 - Para Modificar Telefono\n2 - Para Modificar Dirección\n"))
                    newdato = str(input("Ingrese el nuevo dato a actualizar\n"))
                    user.modificarDatos(dato,newdato)
            elif menuUser == 3: 
                retro = 1
                while retro == 1:
                    try:
                        baja = int(input("Usted esta seguro que quiere darse de baja?\n1- SI\n2- Atrás\n"))
                        if baja == 1:
                            user.darseDeBaja()
                            quit()
                        elif baja == 2:
                            retro = 0
                        else:
                            print("Ingrese una opción correcta\n")
                    except ValueError:
                        print("Ingrese carácteres correctos\n")
            elif menuUser == 4:
                on=0
            elif menuUser == 5:
                print("Saliendo del programa...\nGracias por usar la Aap")
                quit()
            else:
                print("Por favor, ingrese una opción del menú\n")       
        except ValueError:
            print("Ingrese carácteres correctos por favor\n")

def menuPelis(user):
    print("Ingresando a Menu Peliculas")
    on = 1
    while on == 1:
        try:
            menuPeli = int(input("Ingrese la opción deseada\n1- Ver todas las Peliculas\n2- Ver Peliculas DISPONIBLES\n3- Alquilar Pelicula\n4- Devolver Pelicula\n5- Atras\n6- Salir\n"))
            if menuPeli == 1:
                user.verTodas()
            elif menuPeli == 2:
                user.verDisponibles()
            elif menuPeli == 3:#podria agregar functions bsuqueda para nombre peli,lista,condicional para q escriba correscatamente el nombre
                alquilar = str(input("Ingrese el NOMBRE de la pelicula que quiere alquilar\n")).lower()
                user.AlquilaryDevolverPeli(alquilar,1)         
            elif menuPeli == 4:
                devolver = str(input("Ingrese el NOMBRE de la pelicula que quiere devolver\n")).lower()
                user.AlquilaryDevolverPeli(devolver,2)
            elif menuPeli == 5:
                on = 0
            elif menuPeli == 6:
                print("Saliendo del programa...\nGracias por usar la Aap")
                quit()    
            else:
                print("Por favor, ingrese una opción del menú\n")       
        except ValueError :
            print("Ingrese carácteres correctos,por favor.")


#print(busqueda(39909651)[1])
print(login())
