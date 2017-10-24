import kivy
kivy.require('1.9.0')
import pymysql
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition
import locale
from kivy.config import Config
from kivy.app import App
from kivy.properties import ObjectProperty

locale.setlocale(locale.LC_ALL, 'Spanish')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
sm = ScreenManager(transition=NoTransition())

class TPScreen(Screen):

    idtp_input = ObjectProperty()
    profesor_input = ObjectProperty()
    materia_input = ObjectProperty()


    def iniciar_sesion(self):
        print self.idtp_input.text
        print self.profesor_input.text
        print self.materia_input.text


class MenuScreen(Screen):
    pass

class PRScreen(Screen):
    pass

class ProfesorApp(App):

    def build(self):
        Config.set('kivy','keyboard_mode','')
        Config.write()
        self.width = Config.getint('graphics','width')
        self.height= Config.getint('graphics','height')
        self.tp_screen = TPScreen(name="TP")
        self.menu_screen = MenuScreen(name="Menu")
        self.pr_screen = PRScreen(name="PR")
        sm.add_widget(self.tp_screen)
        sm.add_widget(self.menu_screen)
        sm.add_widget(self.pr_screen)
        sm.current = "Menu"
        return sm

    def submit_clicked(self, id2):
        if id2 == "TPv":
            sm.current = "TP"
        if id2 == "PRv":
            sm.current = "PR"


if __name__=="__main__":
    ProfesorApp().run()
