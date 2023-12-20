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
    id_ = input("Ingrese su Cedula:\n>")
    nombre = input("Ingrese su Nombre:\n>")
    apellido = input("Ingrese su Apellido:\n>")
    nombre_c = nombre + " " + apellido
    fecha = input("Ingrese su fecha de nacimiento (dd/mm/yyyy):\n>")
    email = input("Ingrese su Correo Electronico:\n>")
    pass_1 = input("Ingrese su Contrasena:\n>")
    pass_2 = input("Confirmar Contrasena:\n>")
    if (rg.registro_u(id_, nombre_c, fecha, email, pass_1 ,pass_2)):
        print("\n\n\n\n************ Registro exitoso ************")
    else:
        print("\n\n\n\n************ Los datos ingresados son incorectos ************")
        
    
def inicio():
    i=0
    while (i!=1):
        menu()
        op = int(input("Ingrese una opcion \n>"))
        match op:
            case 1:
                reg()               
            case 2:
                print("Make juice!")
            case 3:
                print("\t\tSaliendo del sistema \n Gracias por usar el banco de ahorros")
                i=1
            
inicio()