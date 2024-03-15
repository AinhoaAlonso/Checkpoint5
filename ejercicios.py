#Cree un bucle For de Python.

num_list = range (1,11)

for num in num_list:
    print(num)

#Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(num1, num2, num3):
    total = num1 + num2 + num3
    return total
print(suma(3,5,7))

#Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

suma = lambda num1, num2, num3: num1 + num2 + num3

print(suma(3,5,7))

"""Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.
"""

lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']
nombre = 'Enrique'

if nombre in lista_nombre:
    print('El nombre es igual a Enrique')
else:
    print('El nombre Enrique no está en la lista')
