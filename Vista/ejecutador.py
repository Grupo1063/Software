import sys
sys.path.append("C:/Users/PC/Documents/GitHub/Software/")
from control import sesiones as rg

def menu():
    print("\n\t\tMenu")
    print("1) Reguistrar")
    print("2) Iniciar Sesion")
    print("3) Salir")

def reg():
    print("Registro")
    id_ = input("Ingrese Cedula de identidad:\n>")
    nombre = input("Ingrese Nombre:\n>")
    apellido = input("Ingrese Apellido:\n>")
    nombre_c = nombre + " " + apellido
    fecha = input("Ingrese fecha de nacimiento (dd/mm/yyyy):\n>")
    email = input("Ingrese Correo Electronico:\n>")
    pass_1 = input("Ingrese Contrasena:\n>")
    pass_2 = input("Confirmar Contrasena:\n>")
    if (rg.registro_u(id_, nombre_c, fecha, email, pass_1 ,pass_2)):
        print("\n\n\n\n************ Registro exitoso ************")
    else:
        print("\n\n\n\n************ Los datos ingresados son incorectos ************")
        
def sesion():
    print("Inicia Sesión")
    email = input("Ingrese su Correo Electronico:\n>")
    pass_ = input("Ingrese su Contrasena:\n>")
    if( len(email)!=0 and len(pass_)!=0 ):
        band, user = rg.user(email, pass_)
        if(band):
            print("\n\n\n\n************ Sesion Exitosa ************")
            rol = user[0][3]
            match rol:
                case 1:
                    print("\n\n************ Proximamente Administrador ************")              
                case 2:
                    print("\n\n************ Proximamente Gerente ************")
                case 3:
                    print("\n\n************ Proximamente Empleado ************")
                case 4:
                    print("\n\n************ Proximamente Cliente ************")
        else:
            print("\n\n\n\n************ Las credenciales ingresadas son incorectos ************")
    
def inicio():
    i=0
    while (i!=1):
        menu()
        op = int(input("Ingrese una opcion \n>"))
        match op:
            case 1:
                reg()               
            case 2:
                sesion()
            case 3:
                print("\t\tSaliendo del sistema \n Gracias por usar el banco de ahorros")
                i=1
            
inicio()