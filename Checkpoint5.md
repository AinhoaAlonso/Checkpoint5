# ¿Qué es un condicional?

Un condicional es uno de los conceptos fundamentales sobre lo que se necesita para hacer que un programa Python se vuelva dinámico.
Los condicionales son una forma de decir que si ocurre una situación quiero que ,como programa, realices una tarea, pero si ocurre una situación diferente, quiero que realices otra tarea.

##### Sintaxis
Es importante el sangrado de los bloques, se aconseja utilizar siempre el mismo número de espacios en el sangrado, generalmente 2 o 4.
```
age = 25
if age >= 18:
    print('Puedes conducir acompañado de una persona de 25 años o más')
elif age >= 25:
    print('Puedes conducir solo')
else:
    print('Eres menor de edad, no puede conducir')
```
**Ejemplo:** en este caso definimos una variable edad en 25 años, y gracias al condicional evaluamos si la persona puede conducir solo, acompañado o es menor de edad para conducir.
\* elif es lo mismo que decir else if.

##### Operadores de Comparación
Un operador de comparación es lo que colocamos dentro de nuestra condición para verificar elementos como igualdad o desigualdad. También podemos comparar rango de valores, verificar si un elementos es mayor o igual a otro ó menor o igual, esto nos permite agregar comportamientos dinámicos y también resultados True o False.

- == Igualdad
- != Desigualdad
- \> Mayor que
- \>= Mayor o igual que
- \< Menor que
- \<= Menor o igual que

##### Operadores Lógicos
Para escribir condiciones más complejas, devuelve siempre un valor True o False.

**And (y):** para que se ejecute el bloque de código las 2 condiciones tienen que ser True.

```
username = 'Ainhoa'
password = 1234
if username == 'Ainhoa' and password == 1234:
    print('Acceso permitido')
else:
    print('Acceso NO permitido')
```
**Or (o):** para que funcione el bloque de código solo es necesario que se cumpla 1 de las 2 condiciones.
```
username = 'Ainhoa'
email = 'ainhoa@curso.com'
if username =='Ainhoa' or email =='ainhoa@curso.com'
    print('Acceso permitido')
else: 
    print('Acceso NO permitido')
```
**Not (no):** bloque de código donde el resultado es el contrario del valor de la condición.
```
num = 5
if not num == 0:
    print('El número es diferente de 0')
else:
    print('El número es igual a 0')
```
\* not num ==0 devuelve el contrario, en este caso True e imprime que El número es diferente de 0.
##### Para ampliar conocimientos
Los ejemplos anteriores son una forma básica y fácil de entender los condicionales, para mayor información y para saber como trabajar con ellos en listas o strings, os animo a leer estos enlaces:
<https://aprendepython.es/core/controlflow/conditionals/>
<https://www.mclibre.org/consultar/python/lecciones/python-if-else.html>

# ¿Cuáles son los diferentes tipos de bucles en Python?
Los bucles permiten ahorrar tiempo y líneas de codigo al desarrollador, permiten ejecutar instrucciones múltiples. Hay 2 tipos de bucles en Python: for y while.

**For:** el bucle for (in) toma una colección de datos e iterará sobre ella pasando por cada elemento que esté dentro de la colección hasta que se acaben y el bucle se detiene.
```
alimentos = ['fruta', 'verdura', 'lácteos', 'carne', 'pescado']
for alimento in alimentos:
    print(alimento)
````
**Ejemplo:** en este caso el bucle for va iterando por cada uno de los elementos de la lista alimentos y los va imprimiendo, el bucle termina en cuanto se acaban los elementos.

**While:** el bucle while también va recorriendo un número de elementos pero hay que decirle cuando tiene que parar, si no seguirá y se convertirá en un bucle infinito pudiendo bloquear el programa.
```
i=1
while(i<5):
    print(i)
    i=i+1
```
**Ejemplo:** definimos una variable de control (i), que se encarga de controlar la ejecución del ciclo. Iniciamos el bucle while dónde la condición es que se ejecutará mientras i sea menor que 5. Se va imprimiendo cada numero y en cada iteración se suma 1 a i, en cuanto llega a 5 ya no entra en el bucle y se detiene.
    
##### Operadores de control de flujo

Hay ocasiones en las que queremos detener o alterar el comportamiento en algún punto del bucle o en función de una condición.
**Continue:** el programa continúa aunque haya encontrado lo que buscaba, sigue dando vueltas en la colección.
**Break:** el programa se para en cuanto encuentra lo que busca.

```
i=0
while (i<6):
    i+=1
    if i==3:
        print('Número 3 no permitido')
        continue
    print(i)
    if i==4:
        print('Encontré el número 4, saliendo del bucle...')
        break
```
**Ejemplo:** lo que nos muestra
- 1
- 2
- Número 3 no permitido: cuando i == 3 ejecuta continue y salta a la siguiente iteración.
- 4
- Encontré el número 4, saliendo del bucle...: cuando i==4 encuentra lo que busca y ejecuta el break y se detien el bucle aunque la condición aún es verdadera.

##### Para ampliar conocimientos
Si quieres ampliar conocimiento y ver otros ejemplos, te animo a que entres en los siguientes enlaces:
<https://www.freecodecamp.org/espanol/news/bucle-for-en-python-ejemplo-de-for-i-en-range/>
<https://aprendepython.es/core/controlflow/loops/>

# ¿Qué es una lista por comprensión en Python?
Una lista de comprensión es un conjunto de bucles for y condicionales que se pueden colocar todos dentro de una misma línea de código.
##### Sintaxis
```
lista_de_comprension = [acción for elemento in lista if condicion(opcional)]
```
```
num_list = range(1,11)
lista_comprension = [num for num in num_list if num % 2 == 0]
print(lista_comprension)
```
**Ejemplo:** en este caso tenemos un rango que va del 1 al 10 (es uno menos), y nos genera una lista dónde num es la variable de iteracción, y va iterando por nuestra colección con la condición que sean números pares y los va guardando. 

# ¿Qué es un argumento en Python?

Son los valores que se pasan a una función cuando esta se invoca. Hay varios tipos:
- **Argumentos posicionales:** el mapeo entre el valor y como se usa ese valor en la función está determinado por la posición y el orden en el que pasamos los valores.
    ```
    def suma(a,b):
        return a + b
    print(suma(3,5))
    
    resultado : 8
    ```
- **Argumentos de palabra clave:** son argumentos que se pasan a la función con nombre y se asignan a los paramentros de la función según sus nombres.
    ```
    def saludar(nombre, saludo):
        return f'{saludo}, {nombre}'
    print(saludar(nombre= 'Ainhoa', saludo = 'Buenos días'))
    
    resultado: Buenos días, Ainhoa
    ```
- **Argumentos predeterminados:** son los argumentos que tienen valores predeterminados, si no se pasa ningún valor al llamar a la función , se utiliza el predeterminado. Si hay más de un valor en python el que tiene el valor predeterminado va al final.
     ```
     def saludar(saludo, nombre= 'a todos'):
        return f'{saludo} {nombre}'
    print(saludar(saludo ='Buenos días'))
    
    resultado = Buenos días a todos
    ```
- **Argumentos arbitrarios posicionales:** permiten a una función aceptar un numero variable de argumentos (no tienes que saber cuántos son). Se definen utilizando un *args, se puede poner cualquier nombre pero por convención de python se suele utilizar args, y se empaquetan en una tupla.
    ```
    Devuelve una tupla que podemos ver con el siguiente ejemplo:
     
    def suma(*args):
        print(type(args))
        print(args)
    suma(2, 3, 5)

    resultado: <class 'tuple'>
                (2, 3, 5)
    
    Si queremos realizar alguna operación, la tenemos que hacer como tupla:
    
    def suma(*args):
        total = 0
        for num in args: (aquí se pone sin el *)
            total+=num
        return total
    print(suma(2,3,5))
    
    resultado:10
    ```
- **Argumentos arbitrarios de palabra clave:** son iguales que los posicionales pero los argumentos están compuestos por un nombre y un valor. Se definen utilizando **kwargs y se empaquetan en un diccionario.
    ```
    Devuelve una diccionario que podemos ver con el siguiente ejemplo:
     
    def suma(**kwargs):
        print(kwargs)
    
    suma(a = 1, b = 3, c = 2)
    
    resultado: {'a': 1, 'b' : 3, 'c' : 2}
    
    Si queremos operar con las claves o los valores lo tenemos que hacer como un diccionario.
    
    def suma(**kwargs):
        total = 0
        for value in kwargs.values():(trabajamos con los valores .values())
            total += value
        return total

    print(suma(a = 1, b = 3, c = 2))
    
    resultado:6
    ```
##### Para ampliar conocimientos
Si quieres ampliar conocimiento y ver otros ejemplos, te animo a que entres en el siguiente enlace:
<https://interactivechaos.com/es/manual/tutorial-de-python/tipos-de-argumentos>

# ¿Qué es una función Lambda en Python
Es una herramienta que permite empaquetar un comportamiento (resumir una función más pequeña), almacenarla en una variable y luego pasar todo el proceso a otras funciones y otras partes del programa.
Son móviles y fáciles de usar, se pueden comparar con variables que se pueden introducir en un lugar de un valor básico, como una cadena, un diccionario,...

``` 
full_name = lambda first, last: f'Hola {first} {last}' 

print(full_name('Ainhoa', 'Alonso'))
```
**Ejemplo:** en esta caso la función lambda toma 2 argumentos y luego devuelve una cadena formateada que concatena los dos nombres.

```
def resultado_final (a, b, operacion):
  resultado = operacion(a,b)
  return f'El resultado final es: {resultado}'

suma = lambda a, b : a + b
print(resultado_final(3, 5, suma))

resultad: El resultado final es: 8
```
**Ejemplo:** en este caso hemos introducido una función lambda de la suma de 2 números en otra funciona llamada resultado_final.

# ¿Qué es un paquete pip?
PIP => pip install packages. 
Es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software que crearon otros desarrolladores y utilizarlos en nuestros propios programas.

##### Instalación

 1. Descargamos el archivo [get-pip.py](https://bootstrap.pypa.io/get-pip.py) (Botón derecho y lo guardamos dónde queramos).
 2. Desde símbolo de sistema nos posicionamos en el directorio donde hemos guardado el archivo.(Hay que tener instalado [python](https://www.python.org/downloads/)).
            ```python get-pip.py```
 3. Para asegurarnos que está instalado: ```pip --version``` y tiene que aparecer la versión instalada.

Para instalar los paquetes: ```pip install nombre_del_paquete```.
Algunos ejemplos de paquetes PIP incluyen bibliotecas como Numpy, Math, Requests, Inflection,Pprint,...


 
 










