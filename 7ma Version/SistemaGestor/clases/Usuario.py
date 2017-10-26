class Usuario:
#CONSTRUCTOR ---------------------
    def __init__(self, usuario, nombre, apellido, clave, tipo):
        self.__usuario = usuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__clave = clave
        self.__tipo = tipo

#METODOS ---------------------
    def setUsuario(self, usuario):
        self.__usuario = usuario

    def getUsuario(self):
        return self.__usuario

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def setApellido(self, apellido):
        self.__apellido = apellido

    def getApellido(self):
        return self.__apellido

    def setClave(self, clave):
        self.__clave = clave

    def getClave(self):
        return self.__clave

    def setTipo(self, tipo):
        self.__tipo = tipo

    def getTipo(self):
        return self.__tipo

    def imprimirDatos(self):
        print "Usuario: ", self.getUsuario()
        print "Nombre: ", self.getNombre()
        print "Apellido: ", self.getApellido()
        print "Clave: ", self.getClave()
        print "Tipo: ", self.getTipo()


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
        sql = "INSERT INTO actividades(idTrabajo, consigna, respuesta) values('" + idTrabajo + "', '" + consigna + "', '" + respuesta + "')"
        cursor.execute(sql)
        db.commit()


    def crearTrabajoPractico(self, titulo, materia, carrera):
        usuario = str(self.getUsuario())
        #print usuario
        from dbpython import *
        sql = "INSERT INTO trabajos(titulo, materia, carrera, usuario) values('" + titulo + "', '" + materia + "', '" + carrera + "', '" + usuario + "')"
        cursor.execute(sql)
        db.commit()
        ### Modifico para que agregue la consigna correspondiente al Tp y no al Usuario
        from dbpython import *
        sql = "Select idTrabajo from trabajos where titulo = '" + titulo + "' and materia = '" + materia + "' and carrera = '" + carrera + "'"
        cursor.execute(sql)
        row = cursor.fetchone()
        idTrabajo = str(row[0])
        ###
        return idTrabajo


"""
    def crearTrabajoPractico(self):
        titulo = raw_input("Ingrese titulo del trabajo practico: ")
        materia = raw_input("Ingrese materia del trabajo practico: ")
        carrera = raw_input("Ingrese carrera del trabajo practico: ")
        idUsuario = str(self.getIdUsuario())

        from dbpython import *
        sql = "INSERT INTO trabajos(titulo, materia, carrera, idUsuario) values('" + titulo + "', '" + materia + "', '" + carrera + "', '" + idUsuario + "')"
        cursor.execute(sql)
        db.commit()
        consigna = raw_input("Detalle su ejercicio: ")
        respuesta = raw_input("Escriba la respuesta correcta: ")
        sql = "SELECT idTrabajo from trabajos WHERE idUsuario='" + idUsuario + "'"
        cursor.execute(sql)
        row = cursor.fetchone()
        idTrabajo = str(row[0])
        sql = "INSERT INTO actividades(idTrabajo, consigna, respuesta) values('" + idTrabajo + "', '" + consigna + "', '" + respuesta + "')"
        cursor.execute(sql)
        db.commit()

"""