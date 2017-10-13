# -*- coding: utf-8 -*-

import Tkinter as Tk
from PIL import Image, ImageTk
import pymysql


########################################################################
class CrearTP(Tk.Toplevel):

    # ----------------------------------------------------------------------
    def __init__(self, original):

        def dp(v1):
            global dps
            dps = v1
        """Constructor"""
        self.original_frame = original
        Tk.Toplevel.__init__(self)

        self.title("Crear Trabajo Práctico")
        self.geometry('802x604')
        photo2 = ImageTk.PhotoImage(file='C:\Users\Usuario\PycharmProjects\SistemaGestor\image\SGTPS.png')
        lbl2 = Tk.Label(self, image=photo2)
        lbl2.pack()
        titulo = Tk.Entry(self, width=18, font=("bold", 11), highlightthickness=2)
        titulo.place(x=220, y=223)
        print titulo.get()
        materia = Tk.Entry(self, width=18, font=("bold", 11), highlightthickness=2)
        materia.place(x=220, y=270)
        boton = Tk.Button(self, text='Siguiente', fg='white')
        boton.config(width=13, font=("bold", 12), bg="red4", height=1)
        boton.place(x=630, y=485)
        boton2 = Tk.Button(self, text='Cerrar Sesión', fg='white', command=self.onClose)
        boton2.config(width=11, font=("bold", 12), bg="red4")
        boton2.place(x=690, y=85)
        boton = Tk.Button(self, text='← Atrás', fg='white', command=self.onClose)
        boton.config(width=11, font=("bold", 12), bg="red4", height=1)
        boton.place(x=580, y=85)
        options = ["Sistemas", "Traductorado", "Alimentos"]
        var = Tk.StringVar()
        var.set("Elegir")
        dp = Tk.OptionMenu(self, var, *options, command=dp)
        dp.config(width=16, font=("bold", 10), bg="white")
        dp.place(x=220, y=314)

        text0 = Tk.Label(self, text="Universidad Nacional de Lanús", bg='lightsteelblue', fg="red4",
                         font=("bold", 18)).place(x=110, y=7)
        text = Tk.Label(self, text="Sistema Gestor de Corrección de TPs", bg='white', font=("bold", 15)).place(x=115,
                                                                                                               y=65)
        text1 = Tk.Label(self, text="CREAR TRABAJO PRACTICO: ", bg='white', font=("bold", 14)).place(x=300, y=152)
        text2 = Tk.Label(self, text="Ingrese los Siguientes Datos: ", bg='white', font=("bold", 13)).place(x=142, y=188)
        text3 = Tk.Label(self, text="Título: ", bg='white', font=("bold", 13)).place(x=148, y=230)
        text4 = Tk.Label(self, text="Materia: ", bg='white', font=("bold", 13)).place(x=148, y=276)
        text5 = Tk.Label(self, text="Carrera: ", bg='white', font=("bold", 13)).place(x=148, y=322)

        self.mainloop()


    # ----------------------------------------------------------------------
    def onClose(self):
        """"""
        self.destroy()
        self.original_frame.show()


########################################################################
class MyApp(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""

        self.root = parent
        self.root.title("Login")
        self.frame = Tk.Frame(parent)
        self.frame.pack()

        el = Tk.Label(self.root, text="Usuario:", bg="red4", fg="white", width=10)
        el.pack(padx=5, pady=5, ipadx=5, ipady=5)
        el.place(x=350, y=260)

        self.entrada1 = Tk.Entry(self.root)
        self.entrada1.pack(padx=5, pady=5, ipadx=5, ipady=5)
        self.entrada1.place(x=430, y=260)

        el = Tk.Label(self.root, text="Password:", bg="red4", fg="white", width=10)
        el.pack(padx=5, pady=5, ipadx=5, ipady=5)
        el.place(x=350, y=310)

        self.entrada2 = Tk.Entry(self.root)
        self.entrada2.pack(padx=5, pady=5, ipadx=5, ipady=5)
        self.entrada2.place(x=430, y=310)

        self.frame = Tk.Frame(parent)
        self.frame.pack()

        #boton = Tk.Button(self.root, text="Crear Trabajo Práctico", fg="blue",
        #                  command=self.crearTrabajoPractico, width=20)
        #boton.place(x=120, y=100)

        buton3 = Tk.Button(self.root, text="Login",
                           fg="white", bg="red4", command=self.validar, width=20)
        buton3.place(x=384, y=370)

        buton4 = Tk.Button(self.root, text="Entrar como Invitado",
                           fg="white", bg="red4", command=self.validar, width=20)
        buton4.place(x=384, y=460)

        text0 = Tk.Label(self.root, text="Universidad Nacional de Lanús", bg='lightsteelblue', fg="red4",
                         font=("bold", 18)).place(x=110, y=7)

        text = Tk.Label(text="Sistema Gestor de Corrección de TPs", bg='white', font=("bold", 19)).place(x=245, y=172)

    # ----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()

    # ----------------------------------------------------------------------

    def crearTrabajoPractico(self):
        """"""
        self.hide()
        subFrame = CrearTP(self)

    def validar(self):
        """"""
        self.hide()
        # Aca deberiamos hacer la conexion con la bd, comprobando el usuario y contrasenia
        try:
            db = pymysql.connect(user="root",
                                 passwd="root",
                                 host="127.0.0.1",
                                 port=3306,
                                 db="dbpython")
        except:
            print("Error de Conexión")

        cur = db.cursor()

        try:
            respuesta = cur.execute(
            "SELECT nombre, apellido, tipo FROM Login WHERE usuario ='" + self.entrada1.get() + "' AND clave ='" + self.entrada2.get() + "' ")
            row = cur.fetchone()
            st3 = str(row[2])
            if respuesta == 1 and st3 == 'Profesor':
                self.crearTrabajoPractico()

        except:
            print("Error de Login")

    # --------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()


# ----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry('802x604')
    photo2 = ImageTk.PhotoImage(file='C:\Users\Usuario\PycharmProjects\SistemaGestor\image\SGTPS.png')
    lbl2 = Tk.Label(root, image=photo2)
    lbl2.pack()
    app = MyApp(root)
    root.mainloop()


