from Login import Login
from TrabajoPractico import TrabajoPractico
from Actividad import Actividad

login = Login(1, "Raul", "Perez", "User1", "h", "Admin")
login.imprimirDatos()
print

tp = TrabajoPractico(1, "Calculo", "Matematica", "Licenciatura en Sistemas", login.getIdLogin())
tp.imprimirDatos()
print

actividad = Actividad(tp.getIdTrabajo(), "2+2 = ", "4")
actividad.imprimirDatos()
print