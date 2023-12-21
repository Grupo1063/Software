import sys
sys.path.append("C:/Users/PC/Documents/GitHub/Software/")
from modelo import conexion as con
import datetime

def f_fecha(fecha_entrada):
    fecha_objeto = datetime.datetime.strptime(fecha_entrada, "%d/%m/%Y")
    fecha_salida = fecha_objeto.strftime("%Y-%m-%d")
    return fecha_salida

def registro_u(id, nombres, fecha, email, pass_1, pass_2, rol=3):
    if(pass_1 == pass_2 and len(id)==10):
        fecha = f_fecha(fecha)
        # print(f"\n\nDatos Ingresados\n\n{id}, \n{nombres}, \n{fecha}, \n{rol}, \n{email}, \n{pass_1} ")
        con.insertar(id, nombres, fecha, rol, email, pass_1)
        return True
    else:
        return False

def user(email, pass_):
    band, user = con.buscar_log(email, pass_)
    return band, user
        