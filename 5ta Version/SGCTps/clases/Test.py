from Admin import Admin
from dbpython import *

sql = "SELECT usuario from usuarios WHERE usuario='SMartins'"
cursor.execute(sql)
row = cursor.fetchone()
usuario = str(row[0])
admin = Admin(usuario)
#CARGAR UN REGISTRO DE TIPO USUARIO----------
admin.crearUsuario("Diego", "Saavedra", "Skribano", "RojoLocura")

