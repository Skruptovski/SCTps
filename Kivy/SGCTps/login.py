import kivy
import locale
import pymysql
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.image import Image

locale.setlocale(locale.LC_ALL, 'Spanish')

class Login(GridLayout):
    usuario_input = ObjectProperty()
    password_input = ObjectProperty()

    def iniciar_sesion(self):
        # Connect to the database and get the role of that user and password
        try:
            conn = pymysql.connect(user="root",passwd="pires777",host="127.0.0.1",port=3306,database="sgctps")
            cursor = conn.cursor()
            cursor.execute("SELECT rol FROM usuario WHERE Usuario='"+self.usuario_input.text+"' AND Password='"+self.password_input.text+"'")
            row = cursor.fetchone()
            rol = str(row[0])
            # Trigger app correspondiente
            print(rol)
        except Exception:
            print("Error")
        conn.close()

    def ingresar_alumno(self):
        pass

    def registrarse(self):
        pass

    def ayuda(self):
        pass

class LoginApp(App):
    def build(self):
        return Login()

loginApp = LoginApp()
loginApp.run()
