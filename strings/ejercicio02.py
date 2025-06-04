#3################################################################################
#3Realizar un programa que comprueba si una cadena leída por teclado comienza por 
#3una subcadena introducida por teclado.
#3################################################################################

#my_string = 'Este es un texto'

# print(my_string.capitalize())
# print(my_string.lower())
# print(my_string.title())
# print(my_string.startswith('Este'))
# print(my_string.startswith('Esta'))

my_str_1 = input('Ingresa una cadena de texto: ')
my_str_2 = input('Ingresa las priemeras letras de la cadea anterior: ')

if my_str_1.startswith(my_str_2):
    print(f'"{my_str_1}"Comienza con "{my_str_2}"')
else:
    print(f'"{my_str_1}"No comiensa con "{my_str_2}"')
    