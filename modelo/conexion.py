
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
  
def consulta_s(id):
  conn = __conec()
  cursor = conn.cursor()
  try:  
    consulta = "SELECT Saldo FROM cuenta WHERE {} = %s".format("codigo")
    valores = (id,)
    cursor.execute(consulta, valores)
    rows = cursor.fetchall()
    return rows[0][0]
  except Exception as e:
    print("\n\nError en la consulta:", e)
  finally:
    cursor.close()
    conn.close()

def consulta_c(id):
  conn = __conec()
  cursor = conn.cursor()
  try:  
    consulta = "SELECT N_Cuenta FROM cuenta WHERE {} = %s".format("codigo")
    valores = (id,)
    cursor.execute(consulta, valores)
    rows = cursor.fetchall()
    return rows[0][0]
  except Exception as e:
    print("\n\nError en la consulta:", e)
  finally:
    cursor.close()
    conn.close()

def movimientos(codigo, cuenta_origen, cuenta_destino, accion, monto):
    try:
        conn = __conec()
        
        cursor = conn.cursor()
        # Llamada a la función Movimientos_t
        cursor.callproc('Movimientos_t', (codigo, cuenta_origen, cuenta_destino, accion, monto))

        # Recuperar el mensaje de la función (si devuelve uno)
        for result in cursor.stored_results():
          mensaje = result.fetchone()[0]
          print(mensaje)

        conn.commit()

    except mysql.connector.Error as error:
        print("Error al llamar a la función:", error)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

    return mensaje

# movimientos(6, 4, 1, 'RETIRO', 100.0)
# movimientos(2, 4, 0, 'DEPOSITO', 100.0)
# movimientos(6, 4, 1, 'TRANSFERENCIA', 100.0)
