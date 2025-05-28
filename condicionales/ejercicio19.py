##################################################################################
##Escribe un programa que pida un número entero entre uno y doce e imprima el 
##número de días que tiene el mes correspondiente.
## Si introducimos otro número nos da un error.
##################################################################################


month = int(input("Ingresa un mes de 1 al 12: "))

match month:
    case 1:
        print("Enero tiene 31 dias")
    case 2:
        print("Febrero tiene 28 dias")
    case 3:
        print("Marzo tiene 31 dias")
    case 4:
        print("Abril tiene 30 dias")
    case 5:
        print("Mayo tiene 31 dias")
    case 6:
        print("Junio tiene 30 dias")
    case 7:
        print("Julio tiene 31 dias")
    case 8:
        print("Agosto tiene 30 dias")
    case 9:
        print("Septiembre tiene 31 dias")
    case 10:
        print("Octubre tiene 30 dias")
    case 11:
        print("Noviembre tiene 30 dias")
    case 12:
        print("Diciembre tiene 30 dias")
    case _:
        print("El mes no existe")