class Actividad:
    def __init__(self, idTrabajo, consigna, respuesta):
        self.__idTrabajo = idTrabajo
        self.__consigna = consigna
        self.__respuesta = respuesta

#METODOS ---------------------
    def setIdTrabajo(self, idTrabajo):
        self.__idTrabajo = idTrabajo

    def getIdTrabajo(self):
        return self.__idTrabajo

    def setConsigna(self, consigna):
        self.__consigna = consigna

    def getConsigna(self):
        return self.__consigna

    def setRespuesta(self, respuesta):
        self.__respuesta = respuesta

    def getRespuesta(self):
        return self.__respuesta

    def imprimirDatos(self):
        print "idTrabajo: ", self.getIdTrabajo()
        print "Consigna: ", self.getConsigna()
        print "Respuesta: ", self.getRespuesta()
