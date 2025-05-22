##################################################################################
## Crea un programa que pida al usuario dos números y muestre su división 
##si el segundo no es cero, o un mensaje de aviso en caso contrario.
##################################################################################

numero1 = int(input("Ingresa un nuemero: "))
numero2= int(input("Ingresa otro numero;"))

if numero2 != 0:
    división = numero1/numero2
    print("El resultado es:",división)
else:
    print("El segundo nuemro no dede ser cero")

