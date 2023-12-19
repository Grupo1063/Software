import Control.registro as rg

def menu():
    print("\n\t\tMenu")
    print("1) Reguistrar")
    print("2) Iniciar Sesion")
    print("3) Salir")

def reg():
    print("Registro")
    nombre = input("Ingrese su Nombre")
    apellido = input("Ingrese su Apellido")
    fecha = input("Ingrese su fecha de nacimiento")
    email = input("Ingrese su Correo Electronico")
    pass_1 = input("Ingrese su Contrasena ")
    pass_2 = input("Confirmar Contrasena")
    if (pass_1 == pass_2):
        nombre_c = nombre + apellido
        rg.registro(nombre_c, fecha, 1, email, pass_1 )
        
    
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