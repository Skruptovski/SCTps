class Usuario:
#CONSTRUCTOR ---------------------
    def __init__(self, idUsuario, nombre, apellido, usuario, clave, tipo):
        self.__idUsuario = idUsuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__usuario = usuario
        self.__clave = clave
        self.__tipo = tipo

#METODOS ---------------------
    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario

    def getIdUsuario(self):
        return self.__idUsuario

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
        print "idUsuario: ", self.getIdUsuario()
        print "Nombre: ", self.getNombre()
        print "Apellido: ", self.getApellido()
        print "Usuario: ", self.getUsuario()
        print "Password: ", self.getClave()
        print "Tipo: ", self.getTipo()

    def CrearUsuario(self, idUsuario, nombre, apellido, usuario, clave, tipo):
        pass

