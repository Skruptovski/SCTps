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
from clases.Usuario import Usuario


class ErrorPopup(Popup):
    pass

class AyudaPopup(Popup):
    pass

class LoginScreen(Screen):
    usuario_input = ObjectProperty()
    password_input = ObjectProperty()
    us = 0
    def iniciar_sesion(self):
        # Intentar conectar a la base de datos
        try:
            sql = "SELECT tipo,usuario FROM usuarios WHERE usuario='"+self.usuario_input.text+"' AND clave='"+self.password_input.text+"'"
            cursor.execute(sql)
            row = cursor.fetchone()
            rol = str(row[0])
            LoginScreen.us = str(row[1])
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
    rol_input = ObjectProperty()

    def crear_peticion(self):
        print self.nombre_input.text
        print self.apellido_input.text
        print self.email_input.text
        print self.rol_input.text

        # Intentar conectar a la base de datos
        try:
            sql= "INSERT INTO `dbpython`.`peticiones` (`nombre`, `apellido`, `tipo`, `email`) VALUES ('"+self.nombre_input.text+ "', '"+self.apellido_input.text+"', '"+self.rol_input.text+"', '"+self.email_input.text+"')"
            cursor.execute(sql)
            db.commit()
            print("Peticion cargada con éxito")
        except Exception:
            print("Error al insertar la petición")

class AlumnoScreen(Screen):
    nombretp_input = ObjectProperty()
    consigna = 0
    def resolver_tp(self):
        #print self.nombretp_input.text
        try:
            #Primero hace una consulta a la base de datos por el trabajo tomando en cuenta su nombre, y
            #a partir de esa informacion trae el id. Realiza una segunda consulta a la bd respecto a las
            #consignas relacionadas con ese id. Estaba pensando que es muy probable que necesitemos id consigna
            #por si son varias ....

            sql = "SELECT consigna, respuesta1, respuesta2, respuesta3, correcta FROM actividades WHERE idTrabajo = (Select idTrabajo FROM dbpython.trabajos where titulo = '"+ self.nombretp_input.text + "' )"
            cursor.execute(sql)
            row = cursor.fetchone()
            AlumnoScreen.consigna = str(row[0])
            AlumnoScreen.r1 = str(row[1])
            AlumnoScreen.r2 = str(row[2])
            AlumnoScreen.r3 = str(row[3])
            AlumnoScreen.correcta = str(row[4])

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
        #print 'Usuario' + LoginScreen.us

        # Intentar conectar a la base de datos
        try:
            #La idea sería traer el id desde el .kv original
            sql = "SELECT * from usuarios WHERE usuario= '"+LoginScreen.us+ "'"
            cursor.execute(sql)
            row = cursor.fetchone()
            user = Usuario(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]))
            user.crearTrabajoPractico(self.titulo_input.text, self.materia_input.text, self.carrera_input.text)
            print("Peticion cargada con éxito")
        except Exception:
            print("Error al insertar la petición")


class AdminScreen(Screen):
    pass


class ActividadesScreen(Screen):
    pass

class ResolverScreen(Screen):
    consigna2 = StringProperty('Cargar Preguntas')
    r1 = StringProperty('')
    r2 = StringProperty('')
    r3 = StringProperty('')
    is_active = BooleanProperty(False)

    def resv_tp(self):
        self.consigna2 = AlumnoScreen.consigna
        self.r1 = AlumnoScreen.r1
        self.r2 = AlumnoScreen.r2
        self.r3 = AlumnoScreen.r3

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
