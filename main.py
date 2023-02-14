# Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
name = input('Hola, por favor ingrese su nombre: ')
nombre = name.capitalize()
item = input(f'Hola {nombre}, por favor ingrese una lista de sus paises favoritos separados solo por una coma (,), nosotros los ordenaremos alfabeticamente para usted y si hay alguno repetido lo eliminaremos.\n')

# Acá agregamos a paises cada item que agreguemos en paises y que esten separados por una coma (,)
paises = [pais for pais in item.split(',')]

print(','.join(sorted(list(set(paises)))))