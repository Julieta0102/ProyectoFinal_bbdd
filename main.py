from claseUsuario import Usuarios
from conexion import conexionbbdd,cursor


def busqueda(valor):
    lista1 = []
    cursor.execute("select dni from usuarios")
    result = cursor.fetchall()
    for i in result:
        for j in i :
            lista1.append(j)
    if valor not in lista1:
        return False
    else:
        return True
    
incio = 0
while incio != 3 :
    print("Bienvenido a Videoclub Roma")
    incio = int(input("Ingrese la opcion deseada\n1 - Iniciar sesion\n2- Registrarse\3- Salir"))
    if incio == 1:
        dni = int(input("Ingrese su dni"))
        if busqueda(dni) == True:
            contra = str(input("Ingrese su contraseña\n"))
        else:
            print("Usted no esta registrado")

        menu = int(input("Ingrese la opción deseada :\n1 - Menu Usuario\n2 - Menu Pelicula\n3 - Salir"))
        if menu == 1:
            submenu = int(input("1 - Registrarse\n2 - Modificar Datos\n3 - Darse de Baja\n4 - Ver datos"))
            if submenu == 1:
                dni = int(input("Ingrese su dni"))
                nombre = str(input("Ingrese su nombre"))
                tel = int(input("Ingrese su telefono"))
                dir = str(input("Ingrese su direccion"))
                user = Usuarios(dni,nombre,tel,dir)
                user.darseDeAlta()
            elif submenu ==2:

                datos = int(input("Ingrese la opción deseada\n1 - Modificar telefono\n2 - Modificar direccion"))
                newdato = int(input("Ingrese el nuevo dato"))
                Usuarios.modificarDatos(self,datos,newdato)