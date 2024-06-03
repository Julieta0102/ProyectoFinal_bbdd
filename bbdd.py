from conexion import conexionbbdd,cursor

cursor.execute("drop database videoclub")
cursor.execute("create database videoclub")
cursor.execute("use videoclub")
cursor.execute("Create table Usuarios (id int primary key auto_increment, dni int , nombre varchar(50),telefono int,direccion varchar(50),situacion varchar(50),contrasenia TEXT ,codigo_peli int )")
cursor.execute("create table peliculas (id int primary key auto_increment, nombre varchar(50),codigo_peli int ,genero varchar(50),situacion varchar(50),dni_usuario int)")
cursor.execute("create table transacciones (id int primary key auto_increment, fecha datetime , tipo varchar(50), usuario_id int, foreign key (usuario_id) references usuarios(id),pelicula_id int, foreign key (pelicula_id) references peliculas(id))")
sql = "insert into usuarios (dni,nombre,telefono,direccion,situacion,contrasenia,codigo_peli) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = [
    (39909651,"Julieta",1136241814,"Ramon Falcon 4658","L","hola",None),
    (16254968,"Omar",1165895647,"Rivadavia 1234","L","hola2",None),
    (39856987,"Esteban",1169857485,"Oliveri 789","L","hola3",None),
    (24125965,"Rocio",1122334455,"White 150","L","hola4",None),
    (36539525,"Analia",1166778899,"Mozart 15","L","hola5",None),
    (38728545,"Diana",1163112247,"Medina 123","L","hola6",None),
    (29080371,"Roma",1136987458,"Av Escalada 1510","L","hola7",None),
    (16106313,"Magali",1138414591,"Lacarra 12","L","hola8",None),
    (36789651,"Isabella",1162789649,"Gral Paz 12055","L","hola9",None),
    (40125746,"Mateo",1133669988,"Juan B. Alberdi 4785","L","hola10",None),
]
cursor.executemany(sql,val)
conexionbbdd.commit()
sql = "insert into peliculas (nombre,codigo_peli,genero,situacion,dni_usuario) values (%s ,%s ,%s ,%s ,%s)"
val= [
    ("Matrix",1234,"Accion","L",None),
    ("Caperucita Roja",5678,"Infatil","L",None),
    ("Jefe en Pañales",9101,"Infatil","L",None),
    ("Duro de matar",1112,"Accion","L",None),
    ("Bad boys",1314,"Accion","L",None),
    ("Avengers",1516,"Ciencia Ficcion","L",None),
    ("Flash",1718,"Ciencia Ficcion","L",None),
    ("Intensamente 1",1920,"Infatil","L",None),
    ("Busqueda Implacable 1",2122,"Accion","L",None),
    ("Madagascar",2324,"Infatil","L",None)
]

cursor.executemany(sql,val)
conexionbbdd.commit()

