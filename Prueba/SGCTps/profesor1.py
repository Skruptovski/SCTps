import locale
from kivy.config import Config
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition
locale.setlocale(locale.LC_ALL, 'Spanish')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')



class Profesor1(Screen):
    pass



class Profesor1App(App):
    def build(self):
        return Profesor1()

ProfesorApp = Profesor1App()
ProfesorApp.run()
