import kivy
import locale
import pymysql
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.config import Config

locale.setlocale(locale.LC_ALL, 'Spanish')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class CustomPopup(Popup):
    pass

class Profesor(GridLayout):
    idtp_input = ObjectProperty()
    profesor_input = ObjectProperty()
    materia_input = ObjectProperty()


class ProfesorApp(App):
    def build(self):
        return Profesor()

ProfesorApp = ProfesorApp()
ProfesorApp.run()
