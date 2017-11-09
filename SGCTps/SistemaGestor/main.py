#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.properties import *

import locale
from clases.dbpython import *
from clases.Usuario import Usuario, Sesion
from clases.Peticion import Peticion
from clases.Admin import Admin

class ErrorPopup(Popup):
    pass

class AyudaPopup(Popup):
    pass

class LoginScreen(Screen):
    usuario_input = ObjectProperty()
    password_input = ObjectProperty()
    user =Usuario(None,None,None,None,None)#creo un user vacio para luego cargarlo y llamarlo desde otra clase
    sesion=Sesion()#creo la instancia de la clase Sesion para pder realizar acciones sobre el usuario
    def iniciar_sesion(self):
        # Intentar conectar a la base de datos
        try:
            usuario=self.sesion.traerUsuarioSes(self.usuario_input.text,self.password_input.text)
            #con el metodo de sesion traerusuario  obtube  una instancia de Usuario guardada en usuario

            rol =usuario.getTipo()#guardo el tipo de usuario en rol para luego decidir a que pantalla es dirigido
            LoginScreen.user=usuario #guardo la instancia de usuario en user para que sea usado por otra clase


            print(rol)
            if(rol=="Docente"):
                screenmanager.current = "docente"
            else:
                if(rol=="Administrador"):
                    screenmanager.current = "admin"
        except Exception:
            print("Error de logueo")
            error = ErrorPopup()
            error.open()
    def ayuda(self):
        ayuda = AyudaPopup()
        ayuda.open()

class RegistrarseScreen(Screen):
    nombre_input = ObjectProperty()
    apellido_input = ObjectProperty()
    email_input = ObjectProperty()
    clave_input = ObjectProperty()

    def crear_peticion(self):
        print self.nombre_input.text
        print self.apellido_input.text
        print self.email_input.text
        print self.clave_input.text
        peticion=Peticion(None ,self.nombre_input.text,self.apellido_input.text,self.email_input.text,self.clave_input.text )
        try:
            peticion.crearPeticion()
            print("Peticion cargada con éxito")
        except Exception:
            print("Error al insertar la petición")

class AlumnoScreen(Screen):
    nombretp_input = ObjectProperty()
    consigna = 0
    def resolver_tp(self):

        try:
            #Primero hace una consulta a la base de datos por el trabajo tomando en cuenta su nombre, y
            #a partir de esa informacion trae el id. Realiza una segunda consulta a la bd respecto a las
            #consignas relacionadas con ese id. Estaba pensando que es muy probable que necesitemos id consigna
            #por si son varias ....
            num = 1
            print  int(num)
            print self.nombretp_input.text

            sql = "SELECT consigna, respuesta1, respuesta2, respuesta3, correcta FROM actividades WHERE idTrabajo =(Select idTrabajo FROM dbpython.trabajos where titulo = '"+ self.nombretp_input.text + "' ) and numero = '1' "
            #(Select idTrabajo FROM dbpython.trabajos where titulo = '"+ self.nombretp_input.text + "' )
            cursor.execute(sql)

            print self.nombretp_input.text
            row = cursor.fetchone()
            AlumnoScreen.consigna = str(row[0])
            AlumnoScreen.r1 = str(row[1])
            AlumnoScreen.r2 = str(row[2])
            AlumnoScreen.r3 = str(row[3])
            AlumnoScreen.correcta = str(row[4])
            sql2 = "Select materia, carrera, titulo FROM trabajos where titulo = '" + self.nombretp_input.text + "' "
            cursor.execute(sql2)
            row2 = cursor.fetchone()
            AlumnoScreen.materia = str(row2[0])
            AlumnoScreen.carrera = str(row2[1])
            AlumnoScreen.titulo = str(row2[2])



            screenmanager.current = "resolver"


        except Exception:
            print("Error")
            error = ErrorPopup()
            error.open()


    def ayuda(self):
        ayuda = AyudaPopup()
        ayuda.open()

class DocenteScreen(Screen):
    pass

class CrearTPScreen(Screen):
    titulo_input = ObjectProperty()
    materia_input = ObjectProperty()
    carrera_input = ObjectProperty()

    def crear_tp(self):


        # Intentar conectar a la base de datos
        try:
            #La idea sería traer el id desde el .kv original
            #puebo trae la instancia de usuario desde  LoginScreen
            print("Usuario: "+str(LoginScreen.user.getUsuario()))
            #con la instancia user accedo al metodo agregarTp de Usuario() y le paso por parametro las entradas del teclado
            LoginScreen.user.crearTrabajoPractico(self.titulo_input.text, self.materia_input.text, self.carrera_input.text)
            print("TP creado con éxito")
        except Exception:
            print("Error al insertar TP")


class AdminScreen(Screen):
    adm=Admin(LoginScreen.user)
    def mostrarPeticiones(self):
        self.adm.traerPeticiones()#traigo la lista de peticiones
        #self.adm.aprobarPeticion(self.adm.traerPeticion(6))  #cuando funcione aca le paso el id de
        # la peticion a aprobar y el sistema lo convierte en usuario


class PeticionesScreen(Screen):
    pass

class ActividadesScreen(Screen):
    pass

class ResolverScreen(Screen):
    consigna2 = StringProperty('Comenzar')
    r1 = StringProperty('')
    r2 = StringProperty('')
    r3 = StringProperty('')
    carrera = StringProperty('')
    materia = StringProperty('')
    titulo = StringProperty('')
    infoc = StringProperty('')
    infom = StringProperty('')
    is_active = BooleanProperty(False)
    num = 1

    def resv_tp(self):
        self.consigna2 = AlumnoScreen.consigna
        self.r1 = AlumnoScreen.r1
        self.r2 = AlumnoScreen.r2
        self.r3 = AlumnoScreen.r3
        self.titulo = AlumnoScreen.titulo

    #Probema con estos métodos, tuve que crearlos porque no tengo forma de pasar las variables de la clase anterior si no
    #es por medio de ellos. Capaz exista otra forma, yo no la encontré
    def resv_info(self):

        self.materia = AlumnoScreen.materia
        self.carrera = AlumnoScreen.carrera
        self.infoc = "Carrera del Trabajo: "
        self.infom = "Materia del Trabajo:"
        self.titulo = AlumnoScreen.titulo

    #Este método muestra la siguiente consigna, el problemá es el tope.
    #Capaz convendría armar una consulta que cuente la cantidad de consignas relacionadas
    def total(self):
        sql = "SELECT count(numero) FROM actividades WHERE idTrabajo = (Select idTrabajo FROM dbpython.trabajos where titulo = '" + AlumnoScreen.titulo + "' )"
        cursor.execute(sql)
        row = cursor.fetchone()
        return row[0]
    def ir_siguiente(self):
        self.num = self.num+1
        if (self.total() >= self.num):

            sql = "SELECT consigna, respuesta1, respuesta2, respuesta3, correcta FROM actividades WHERE idTrabajo = (Select idTrabajo FROM dbpython.trabajos where titulo = '" + AlumnoScreen.titulo + "' ) and numero = '" +str(self.num) +"' "
            cursor.execute(sql)
            row = cursor.fetchone()
            AlumnoScreen.consigna = str(row[0])
            AlumnoScreen.r1 = str(row[1])
            AlumnoScreen.r2 = str(row[2])
            AlumnoScreen.r3 = str(row[3])
            AlumnoScreen.correcta = str(row[4])
            self.consigna2 = AlumnoScreen.consigna
            self.r1 = AlumnoScreen.r1
            self.r2 = AlumnoScreen.r2
            self.r3 = AlumnoScreen.r3
        else:
            print("no hay mas actividades")

    def toggle(self):

        self.is_active = not self.is_active
        print self.is_active


class ScreenManagement(ScreenManager):
    pass



class MainApp(App):
    def build(self):
        self.icon = "images/icon.png"
        self.title = "SGCTps"

        return screenmanager

#Configs
screenmanager = Builder.load_file("kv/main.kv")
locale.setlocale(locale.LC_ALL, 'Spanish')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
#Main
if __name__ == "__main__":
    MainApp().run()
