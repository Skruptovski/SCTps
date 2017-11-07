from Usuario import Usuario
from TrabajoPractico import TrabajoPractico
from Actividad import Actividad
from dbpython import *
#CARGAR UN REGISTRO DE TIPO USUARIO----------
usuario = Usuario(1, "Sebastian", "Martins", "User1", "unla", "Admin")
usuario.imprimirDatos()
print
sql = "INSERT INTO usuarios(nombre, apellido, usuario, clave, tipo) values('" + usuario.getNombre() + "', '" + usuario.getApellido() + "', '" + usuario.getUsuario() + "', '" + usuario.getClave() + "', '" + usuario.getTipo() + "')"
cursor.execute(sql)
db.commit()
#CARGAR UN REGISTRO DE TIPO TRABAJO PRACTICO----------
tp = TrabajoPractico(1, "Calculo", "Matematica", "Licenciatura en Sistemas",
     usuario.getIdUsuario())
tp.imprimirDatos()
print
sql = "INSERT INTO trabajos(titulo, materia, carrera, idUsuario) values('" + tp.getTitulo() + "', '" + tp.getMateria() + "', '" + tp.getCarrera() + "', '1')"
#Cuando quiero mandarle la idUsuario del tp, no me deja hacerlo, asi que lo deje en 1 para ver que el resto funciona
cursor.execute(sql)
db.commit()
print
actividad = Actividad(tp.getIdTrabajo(), "2+2 = ", "4")
actividad.imprimirDatos()
print