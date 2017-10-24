from clases.dbpython import *
sql = "INSERT INTO usuarios(nombre, apellido, usuario, clave, tipo) values('Sebastian', 'Martins', 'SMartins', 'unla', 'Administrador')"
cursor.execute(sql)
db.commit()
sql = "SELECT idUsuario FROM usuarios WHERE usuario='SMartins' AND clave='unla'"
cursor.execute(sql)
row = cursor.fetchone()
idUsuario = str(row[0])
sql = "INSERT INTO administradores(idUsuario) values('" + idUsuario + "')"
cursor.execute(sql)
db.commit()
