class Login:
#CONSTRUCTOR ---------------------
    def __init__(self, idLogin, nombre, apellido, usuario, clave, tipo):
        self.__idLogin = idLogin
        self.__nombre = nombre
        self.__apellido = apellido
        self.__usuario = usuario
        self.__clave = clave
        self.__tipo = tipo

#METODOS ---------------------
    def setIdLogin(self, idLogin):
        self.__idLogin = idLogin

    def getIdLogin(self):
        return self.__idLogin

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
        print "idLogin: ", self.getIdLogin()
        print "Nombre: ", self.getNombre()
        print "Apellido: ", self.getApellido()
        print "Usuario: ", self.getUsuario()
        print "Password: ", self.getClave()
        print "Tipo: ", self.getTipo()


