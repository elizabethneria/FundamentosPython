###############################################################################
#Calcular el perí­metro y área de un rectángulo dada su base y su altura.
################################################################################

print("orograma que calcula el area y perimetro")

altura = input("ingresar la Altura: ")
altura = int(altura)
base = int(input("ingresa la base: "))

perimetro = base + altura + base + altura
area = base * altura

print ("El area del rectangulo es: " + str(area))
print("El perimetro del rectangulo es: " + str(perimetro))