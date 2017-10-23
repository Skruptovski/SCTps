from Admin import Admin
from Usuario import Usuario
from dbpython import *

sql = "SELECT usuario from usuarios WHERE usuario='SMartins'"
cursor.execute(sql)
row = cursor.fetchone()
usuario = str(row[0])
admin = Admin(usuario)
#CARGAR UN REGISTRO DE TIPO USUARIO----------
admin.crearUsuario("Fabricio", "Bustos", "Best4ARG", "CAI")
#CARGAR UN REGISTRO DE TIPO TP----------
sql = "SELECT * from usuarios WHERE usuario='Skribano'"
cursor.execute(sql)
row = cursor.fetchone()
idUsuario = str(row[0])
nombre = str(row[1])
apellido = str(row[2])
usuario = str(row[3])
clave = str(row[4])
user = Usuario(idUsuario, nombre, apellido, usuario, clave)
user.crearTrabajoPractico()


