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
        # Conectar a la base y traer rol del usuario
        try:
            conn = pymysql.connect(user="root",passwd="pires777",host="127.0.0.1",port=3306,database="dbpython")
            cursor = conn.cursor()
            cursor.execute("SELECT tipo FROM usuarios WHERE usuario='"+self.usuario_input.text+"' AND clave='"+self.password_input.text+"'")
            row = cursor.fetchone()
            rol = str(row[0])
            conn.close()
            # Traer la ventana correspondiente
            print(rol)
            if(rol=="Docente"):
                screenmanager.current = "docente"
            else:
                if(rol=="Administrador"):
                    screenmanager.current = "admin"
        # Ya sea por error de login o de la base devolver Error por consola
        except Exception:
            print("Error")
            conn.close()
            error = ErrorPopup()
            error.open()

    def ayuda(self):
        ayuda = AyudaPopup()
        ayuda.open()

class RegistrarseScreen(Screen):
    pass

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

# Main
#Configs
screenmanager = Builder.load_file("kv/main.kv")
locale.setlocale(locale.LC_ALL, 'Spanish')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

if __name__ == "__main__":
    MainApp().run()
