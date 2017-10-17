class TrabajoPractico:
    def __init__(self, idTrabajo, titulo, materia, carrera, idLogin):
        self.__idTrabajo = idTrabajo
        self.__titulo = titulo
        self.__materia = materia
        self.__carrera = carrera
        self.__idLogin = idLogin

#METODOS ---------------------
    def setIdTrabajo(self, idTrabajo):
        self.__idTrabajo = idTrabajo

    def getIdTrabajo(self):
        return self.__idTrabajo

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def getTitulo(self):
        return self.__titulo

    def setMateria(self, materia):
        self.__materia = materia

    def getMateria(self):
        return self.__materia

    def setCarrera(self, carrera):
        self.__carrera = carrera

    def getCarrera(self):
        return self.__carrera

    def setIdLogin(self, idLogin):
        self.__idLogin = idLogin

    def getIdLogin(self):
        return self.__idLogin

    def imprimirDatos(self):
        print "idTrabajo: ", self.getIdTrabajo()
        print "Titulo: ", self.getTitulo()
        print "Materia: ", self.getMateria()
        print "Carrera: ", self.getCarrera()
        print "IdLogin: ", self.getIdLogin()
