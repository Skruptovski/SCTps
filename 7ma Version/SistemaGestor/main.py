#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.uix.popup import Popup

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

    def iniciar_sesion(self):
        # Intentar conectar a la base de datos
        try:
            sql = "SELECT tipo FROM usuarios WHERE usuario='"+self.usuario_input.text+"' AND clave='"+self.password_input.text+"'"
            cursor.execute(sql)
            row = cursor.fetchone()
            rol = str(row[0])
            # Traer la ventana correspondiente
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
            sql= "INSERT INTO `dbpython`.`peticiones` (`nombre`, `apellido`, `usuario`, `clave`, `tipo`, `idAdmin`) VALUES ('"+self.nombre_input.text+ "', '"+self.apellido_input.text+"', 'user1', 'user1c', '"+self.rol_input.text+"', '1')"
            cursor.execute(sql)
            db.commit()
            print("Peticion cargada con éxito")
        except Exception:
            print("Error al insertar la petición")

class AlumnoScreen(Screen):
    pass

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
            sql = "SELECT * from usuarios WHERE usuario='SMartins'"
            cursor.execute(sql)
            row = cursor.fetchone()
            user = Usuario(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]))
            user.crearTrabajoPractico(self.titulo_input.text, self.materia_input.text, self.carrera_input.text)
            print("Peticion cargada con éxito")
        except Exception:
            print("Error al insertar la petición")


class AdminScreen(Screen):
    pass

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
