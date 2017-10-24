class Usuario:
#CONSTRUCTOR ---------------------
    def __init__(self,idUsuario, nombre, apellido, usuario, clave):
        self.__idUsuario = idUsuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__usuario = usuario
        self.__clave = clave

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

    def imprimirDatos(self):
        print "IdUsuario: ", self.getIdUsuario()
        print "Nombre: ", self.getNombre()
        print "Apellido: ", self.getApellido()
        print "Usuario: ", self.getUsuario()
        print "Password: ", self.getClave()

    def crearTrabajoPractico(self):
        titulo = raw_input("Ingrese titulo del trabajo practico: ")
        materia = raw_input("Ingrese materia del trabajo practico: ")
        carrera = raw_input("Ingrese carrera del trabajo practico: ")
        idUsuario = str(self.getIdUsuario())
        from dbpython import *
        sql = "INSERT INTO trabajos(titulo, materia, carrera, idUsuario) values('" + titulo + "', '" + materia + "', '" + carrera + "', '" + idUsuario + "')"
        cursor.execute(sql)
        db.commit()
        ### Modifico para que agregue la consigna correspondiente al Tp y no al Usuario
        from dbpython import *
        sql = "Select idTrabajo from trabajos where titulo = '" + titulo + "' and materia = '" + materia + "' and carrera = '" + carrera + "'"
        cursor.execute(sql)
        row = cursor.fetchone()
        idTrabajo = str(row[0])
        print idTrabajo
        ###
        consigna = raw_input("Detalle su ejercicio: ")
        respuesta = raw_input("Escriba la respuesta correcta: ")
        sql = "SELECT idTrabajo from trabajos WHERE idTrabajo='" + idTrabajo + "'"
        cursor.execute(sql)
        row = cursor.fetchone()
        idTrabajo = str(row[0])
        sql = "INSERT INTO actividades(idTrabajo, consigna, respuesta) values('" + idTrabajo + "', '" + consigna + "', '" + respuesta + "')"
        cursor.execute(sql)
        db.commit()