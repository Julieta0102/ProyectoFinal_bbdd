from claseUsuario import Usuarios
from conexion import conexionbbdd,cursor
from functions import busqueda


on = 1
while on == 1 :
    try :
        print("Bienvenido a Videoclub Roma")
        inicio = int(input("Ingrese la opcion deseada\n1 - Iniciar sesion\n2 - Registrarse\n3 - Salir\n"))
        if inicio == 1:
            dni = int(input("Ingrese su dni\n"))
            if busqueda(dni)[0] == True:
                contra = str(input("Ingrese su contraseña\n"))
                if contra == busqueda(dni)[1][6]:
                    print("Ingreso con éxito")
                    tupla = busqueda(dni)[1]
                    userpru = Usuarios(tupla[1],tupla[2],tupla[3],tupla[4],tupla[6])
                    print(userpru.verDatos())
                    menu = int(input(f"Hola {userpru.get_nombre()} Ingrese la opción deseada :\n1 - Menu Usuario\n2 - Menu Pelicula\n3 - Salir\n"))
                    if menu == 1:
                        submenu = int(input("1 - Modificar Datos\n2 - Darse de Baja\n3 - Ver dato\n"))
                        if submenu == 1:
                            datos = int(input("Ingrese la opción deseada\n1 - Modificar telefono\n2 - Modificar direccion\n"))
                            newdato = int(input("Ingrese el nuevo dato"))
                            #user.modificarDatos(datos,newdato)
                    elif submenu ==2:
                        pass
                else:
                    print("La contraseña es incorrecta")
            else:
                print("Usted no esta registrado")
        elif inicio == 2:
                    dni = int(input("Ingrese su dni\n"))
                    nombre = str(input("Ingrese su nombre\n"))
                    tel = int(input("Ingrese su telefono\n"))
                    dir = str(input("Ingrese su direccion\n"))
                    user = Usuarios(dni,nombre,tel,dir)
                    user.darseDeAlta()
        elif inicio == 3:
            print("Saliendo del programa")
            on = 0
        
        else:
            pass
    except ValueError:
        print("debe ingresar un numero entero")
 
user1 = Usuarios(1515115,"Elsa",113628797,"Olivieri 123","78971")
