class TrabajoPractico:
    def __init__(self, idTrabajo, titulo, materia, carrera, idUsuario):
        self.__idTrabajo = idTrabajo
        self.__titulo = titulo
        self.__materia = materia
        self.__carrera = carrera
        self.__idUsuario = idUsuario

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

    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario

    def getIdUsuario(self):
        return self.__idUsuario

    def imprimirDatos(self):
        print "idTrabajo: ", self.getIdTrabajo()
        print "Titulo: ", self.getTitulo()
        print "Materia: ", self.getMateria()
        print "Carrera: ", self.getCarrera()
        print "IdUsuario: ", self.getIdUsuario()
