################################################################################
#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
################################################################################

#hipotenusa ** 2 = cateto1 ** 2 + cateto2 ** 2

##el operador doble asterisco ** permite elevar un numero a una potencia

##para operaciones matematicas avanzadas importamos la libreria manth

import math

cateto1 = int(input ('Ingresar valor de Cateto 1: ')) 
cateto2 = int(input ('Ingresar valor de Cateto 2: ')) 

hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

print("La hipotenusa del triangulo es:" + str(hipotenusa))