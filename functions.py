from conexion import conexionbbdd,cursor

def busqueda(valor):
        lista1 = []
        cursor.execute("select dni from usuarios")
        result = cursor.fetchall()
        for i in result: #tupla
            for j in i : #saca valores de la tupla
                lista1.append(j)
        if valor not in lista1:
            return [False]
        else:
            cursor.execute(f"select * from usuarios where dni = {valor}")
            asd = cursor.fetchone()
            asd2 = [True,asd]
            return asd2
