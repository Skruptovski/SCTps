#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.uix.popup import Popup

import locale
import pymysql

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
            conn = pymysql.connect(user="root",passwd="pires777",host="127.0.0.1",port=3306,database="dbpython")
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT tipo FROM usuarios WHERE usuario='"+self.usuario_input.text+"' AND clave='"+self.password_input.text+"'")
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
            conn.close()
        except Exception:
            print("Error de base de datos")

    def ayuda(self):
        ayuda = AyudaPopup()
        ayuda.open()

class RegistrarseScreen(Screen):
    nombre_input = ObjectProperty()
    apellido_input = ObjectProperty()
    email_input = ObjectProperty()
    rol_input = ObjectProperty()

    def crear_peticion(self):
        nombre_input = ObjectProperty()
        apellido_input = ObjectProperty()
        email_input = ObjectProperty()
        rol_input = ObjectProperty()
        # Intentar conectar a la base de datos
        try:
            conn = pymysql.connect(user="root",passwd="pires777",host="127.0.0.1",port=3306,database="dbpython")
            # Insertar nueva peticion en la base
            try:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO `dbpython`.`peticiones` (`nombre`, `apellido`, `rol`, `email`) VALUES ('"+self.nombre_input.text+"', '"+self.apellido_input.text+"', '"+self.rol_input.text+"', '"+self.email_input.text+"'")
                print("Peticion cargada con éxito")
            except Exception:
                print("Error al insertar la petición")
            conn.close()
        except Exception:
            print("Error de base de datos")

class AlumnoScreen(Screen):
    pass

class DocenteScreen(Screen):
    pass

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
