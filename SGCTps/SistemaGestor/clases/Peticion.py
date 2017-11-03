class Peticion:

#CONSTRUCTOR ---------------------
    def __init__(self, idPeticion, nombre, apellido, usuario, clave, tipo):
        # type: (object, object, object, object, object, object) -> object
        self.__idPeticion = idPeticion
        self.__nombre = nombre
        self.__apellido = apellido
        self.__usuario = usuario
        self.__clave = clave
        self.__tipo=tipo


    #METODOS ---------------------
    def setIdPeticion(self, idPeticion):
        self.__idPeticion = idPeticion

    def getIdPeticion(self):
        return self.__idPeticion

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


    @property
    def imprimirDatos(self):


        return ("PETICION:\nIdPeticion: "+ str(self.__idPeticion)+" Nombre: "+self.__nombre+" Apellido: "+self.__apellido+ " Usuario: "+self.__usuario+" Password: "+self.__clave+" Tipo "+self.__tipo+"\n")



    def crearPeticion(self):
        from dbpython import *
        sql = "INSERT INTO peticiones(nombre, apellido, usuario, clave, tipo) values('" + self.getNombre() + "', '" + self.getApellido() + "', '" + self.getUsuario() + "', '" + self.getClave() +  "', '" + self.getTipo()+ "')"
        cursor.execute(sql)
        db.commit()
    def traerPeticion(self,id ):
        from dbpython import *
        cursor = db.cursor()
        idPeticion=str(id)
        sql = "SELECT * FROM peticiones WHERE idPeticion="+idPeticion
        cursor.execute(sql)
        row = cursor.fetchone()

        # Trigger app correspondient
        idPeticion =str(row[0])
        nombre = str(row[1])
        apellido = str(row[2])
        usuario = str(row[3])
        clave = str(row[4])
        tipo = str(row[5])

        return Peticion(idPeticion, nombre, apellido, usuario, clave,tipo)
