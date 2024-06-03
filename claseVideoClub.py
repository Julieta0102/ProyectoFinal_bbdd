class VideoClub():
    def __init__(self):
        self.__usuario = []
        self.__pelicula = []
        
    def get_usuario(self):
        return self.__usuario
    
    def set_usuario(self,newusuario):
        self.__usuario = newusuario
        
    def get_pelicula(self):
        return self.__pelicula
    
    def set_pelicula(self,newpelicula):
        self.__pelicula = newpelicula
        
    def agregar_usuario(self,usuario_obj):
        self.get_usuario().append(usuario_obj)
        
    def agregar_pelicula(self,pelicula_obj):
        self.get_pelicula().append(pelicula_obj)
        
    def eliminar_usuario(self,usuario_obj):
        self.get_usuario().remove(usuario_obj)
        
    def eliminar_pelicula(self,pelicula_obj):
        self.get_pelicula().remove(pelicula_obj)