class Usuario:
#CONSTRUCTOR ---------------------
    def __init__(self, nombre, apellido, usuario, clave, tipo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__usuario = usuario
        self.__clave = clave
        self.__tipo = tipo

#METODOS ---------------------

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def setApellido(self, apellido):
        self.__apellido = apellido

    def getApellido(self):
        return self.__apellido

    def setUsuario(self, usuario):
        self.__usuario = usuario

    def getUsuario(self):
        return self.__usuario

    def setClave(self, clave):
        self.__clave = clave

    def getClave(self):
        return self.__clave

    def setTipo(self, tipo):
        self.__tipo = tipo

    def getTipo(self):
        return self.__tipo

    def imprimirDatos(self):
        print "Nombre: ", self.getNombre()
        print "Apellido: ", self.getApellido()
        print "Usuario: ", self.getUsuario()
        print "Password: ", self.getClave()
