#no messi

class Pelicula():
    def __init__(self,nombre,codigo,genero):
        self.__nombre= nombre  
        self.__codigo = codigo
        self.__genero=genero
        self.__situacion = "L"
        self.__dniUsuario = " "
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,newnombre):
        self.__nombre = newnombre
        
    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self,newcodigo):
        self.__codigo = newcodigo
        
    def get_genero(self):
        return self.__genero
    
    def set_genero(self,newgenero):
        self.__genero = newgenero
        
    def get_situacion(self):
        return self.__situacion
    
    def set_situacion(self,newsituacion):
        self.__situacion = newsituacion
        
    def get_dniUsuario(self):
        return self.__dniUsuario
    
    def set_dniUsuario(self,newdniUsuario):
        self.__dniUsuario = newdniUsuario
        
