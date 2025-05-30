#3################################################################################
#3Escribir por pantalla cada carácter de una cadena introducida por teclado.
#3################################################################################

my_string = input('Ingresa un texto: ')

print(my_string)

for letra in my_string:
    print(letra, end= '-')

print()
# La funcion len nos da el tamaño de um strimg
for index in range(len(my_string)):
    print(f'[{ index }] = { my_string [index]}')

other_string = 'prueba'

print(other_string [0])
print(other_string [3])
print(other_string [5])