
import mysql.connector

__host = "localhost"
__port = "3306"
__database = "prueba"
__user = "root"
__password = ""

def __conec():
  # Establecer la conexión
  conn = mysql.connector.connect(
      host=__host,
      port=__port,
      database=__database,
      user=__user,
      password=__password
  )
  return conn

def buscar_log(email, passw):
  conn = __conec()
  cursor = conn.cursor()
  consulta = "SELECT * FROM usuarios WHERE {} = %s AND {} = %s".format("email", "password")
  valores = (email, passw)
  cursor.execute(consulta, valores)
  rows = cursor.fetchall()
  cursor.close()
  conn.close()
  return bool(rows), rows

def insertar(id, nombres, fecha, rol, email, pass_1):
  conn = __conec()
  cursor = conn.cursor()
  sql = "INSERT INTO `usuarios` (identidad, nombres, fecha_n, id_rol, email, password) VALUES (%s, %s, %s, %s, %s, %s);"
  values = (id, nombres, fecha, rol, email, pass_1)
  cursor.execute(sql, values)
  conn.commit()
  cursor.close()
  conn.close()