class Admin:
#CONSTRUCTOR ---------------------
    def __init__(self, usuario):
        self.__usuario = usuario

#METODOS ---------------------

    def setUsuario(self, usuario):
        self.__usuario = usuario

    def getUsuario(self):
        return self.__usuario

    def imprimirDatos(self):
        print "Nombre: ", self.getNombre()
        print "Apellido: ", self.getApellido()
        print "Usuario: ", self.getUsuario()
        print "Password: ", self.getClave()

    def crearUsuario(self, nombre, apellido, usuario, clave):
        from dbpython import *
        sql = "INSERT INTO usuarios(nombre, apellido, usuario, clave) values('" + nombre + "', '" + apellido + "', '" + usuario + "', '" + clave + "')"
        cursor.execute(sql)
        db.commit()