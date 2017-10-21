from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

Builder.load_string("""

<Test>:
    size_hint: .9, .8
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False

    TabbedPanelItem:
        text: 'Pregunta 1'
        spacing: 10
        BoxLayout:
            size_hint_x: None
            width: 720
            orientation: "vertical"
            Label:
                #Estaba pensando que viniera de la base de datos
                text: "Pregunta numero 1"
            TextInput:
                text: "Pregunta"
                id: idtp_input
                multiline: False
            BoxLayout:
                size_hint_x: None
                width: 720
                orientation: "horizontal"
                Label:
                    text: "Verdadero"
                CheckBox:
                    center: self.parent.center
                    #on_active: 
                Label:
                    text: "Falso"
                CheckBox:
                    center: self.parent.center
                    #on_active:
                Label:
                    text: "Otro"
                CheckBox:
                    center: self.parent.center
                    #on_active:   
            BoxLayout:
                size_hint_x: None
                width: 720
                orientation: "horizontal"
        
                Label:
                    text: 'Elegir 1 opcion'
                CheckBox:
                    size_hint_y: None
                    height: '48dp'
                    group: 'g2'
                CheckBox:
                    size_hint_y: None
                    height: '48dp'
                    group: 'g2'       
                CheckBox:
                    size_hint_y: None
                    height: '48dp'
                    group: 'g2'
            BoxLayout:
                size_hint_x: None
                width: 720
                orientation: "horizontal"
                
                Button:
                    size_hint_y: None
                    height: 50
                    text: "Enviar"
                Button:
                    size_hint_y: None
                    height: 50
                    text: "Comprobar"  
    TabbedPanelItem:
        text: 'Pregunta 2'
        spacing: 10
        BoxLayout:
            size_hint_x: None
            width: 720
            orientation: "vertical"
            Label:
                #Estaba pensando que viniera de la base de datos
                text: "Pregunta numero 2"
            TextInput:
                text: "Pregunta"
                id: idtp_input
                multiline: False
            BoxLayout:
                size_hint_x: None
                width: 720
                orientation: "horizontal"
                Label:
                    text: "Verdadero"
                CheckBox:
                    center: self.parent.center
                    #on_active: 
                Label:
                    text: "Falso"
                CheckBox:
                    center: self.parent.center
                    #on_active:
                Label:
                    text: "Otro"
                CheckBox:
                    center: self.parent.center
                    #on_active:   
            BoxLayout:
                size_hint_x: None
                width: 720
                orientation: "horizontal"
        
                Label:
                    text: 'Elegir 1 opcion'
                CheckBox:
                    size_hint_y: None
                    height: '48dp'
                    group: 'g2'
                CheckBox:
                    size_hint_y: None
                    height: '48dp'
                    group: 'g2'       
                CheckBox:
                    size_hint_y: None
                    height: '48dp'
                    group: 'g2'
            BoxLayout:
                size_hint_x: None
                width: 720
                orientation: "horizontal"
                
                Button:
                    size_hint_y: None
                    height: 50
                    text: "Enviar"
                Button:
                    size_hint_y: None
                    height: 50
                    text: "Comprobar"    
    TabbedPanelItem:
        text: 'Pregunta 3'   
    TabbedPanelItem:
        text: 'Pregunta 4'
    TabbedPanelItem:
        text: 'Pregunta 5'
    TabbedPanelItem:
        text: 'Pregunta 6'
    TabbedPanelItem:
        text: 'Pregunta 7'


""")


class Test(TabbedPanel):
    pass



class TestApp(App):
    def build(self):
        return Test()

TestApp = TestApp()
TestApp.run()
