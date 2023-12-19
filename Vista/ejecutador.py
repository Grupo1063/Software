            
def menu():
    print("\n\t\tMenu")
    print("1) Reguistrar")
    print("2) Iniciar Sesion")
    print("3) Salir")
    
def inicio():
    i=0
    while (i!=1):
        menu()
        op = int(input("Ingrese una opcion \n>"))
        match op:
            case 1:
                print("Eat it raw!")
            case 2:
                print("Make juice!")
            case 3:
                print("\t\tSaliendo del sistema \n Gracias por usar el banco de ahorros")
                i=1
            
inicio()