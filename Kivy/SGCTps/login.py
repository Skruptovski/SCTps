import kivy
import locale
import pymysql
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.config import Config

from kivy.uix.textinput import TextInput

from Usuario import Usuario
from TrabajoPractico import TrabajoPractico
from Actividad import Actividad
from dbpython import *
locale.setlocale(locale.LC_ALL, 'Spanish')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class CustomPopup(Popup):
    pass


class Login(GridLayout):
    usuario_input = ObjectProperty()
    password_input = ObjectProperty()

    def iniciar_sesion(self):
        # Connect to the database and get the role of that user and password
        try:

            cursor = db.cursor()
            print(self.usuario_input.text)
            print( self.password_input.text)
            cursor.execute("SELECT tipo FROM usuarios WHERE usuario='"+self.usuario_input.text+"' AND clave='"+self.password_input.text+"'")
            row = cursor.fetchone()
            tipo = str(row[0])
            # Trigger app correspondient
            print(tipo)


        except Exception:
            print("Error")
        db.close()

    def ingresar_alumno(self):
        pass

    def registrarse(self):
        pass

    def ayuda(self):
        ayuda_popup = CustomPopup()
        ayuda_popup.open()

class LoginApp(App):
    def build(self):
        return Login()

loginApp = LoginApp()
loginApp.run()
