# Programación de Computadores - UNAL
## Bucles 1

### Ciclo while
El ciclo mientras (while) permite ejecutar un bloque de instrucciones mientras que una expresión booleana dada se cumpla, es decir, mientras su evaluación dé como resultado verdadero.

La expresión booleana se denomina condición de parada y siempre se evalúa antes de ejecutar el bloque de instrucciones; tras esto se pueden presentar dos casos:

 + Si la condición no se cumple, el bloque no se ejecuta.
 + Si la condición se cumple, el bloque se ejecuta, después de lo cual la instrucción vuelve a empezar, es decir, la condición se vuelve a evaluar

En el caso en que la condición se evalúe la primera vez como falsa, el bloque de instrucciones no será ejecutado, lo cual quiere decir que el número de repeticiones o iteraciones de este bloque será cero (0). Si la condición siempre evalúa a verdadero, la instrucción se ejecutará indefinidamente, es decir, un número infinito de veces.

**Diagrama de flujo:**
<div align='center'>
<figure> <img src="https://i.postimg.cc/RhCKJp29/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b>Diagrama de flujo ciclo <i>while</i></b></figcaption></figure>
</div>

**Python:**
```python
<bloque_prev>
<inicia>
while(<cond>):
  <bloque>
  <actualiza>
<bloque_sigui>
```

Las partes del ciclo mientras (while) son:
 + El fragmento <bloque_prev> es el bloque de instrucciones previas que han sido ejecutadas antes del ciclo.
 + El fragmento <inicia> es el bloque de instrucciones donde se inicializan las variables que intervienen en la condición de parada.
 + El fragmento <cond> es la condición de parada que se evalúa cada vez que se inicia o se reinicia el ciclo.
 + El fragmento <bloque> es el bloque de instrucciones principal del ciclo que se ejecuta mientras la condición se cumpla. El fragmento <actualiza> es el bloque que se utiliza para actualizar las variables que son utilizadas para evaluar la condición de parada cuando se intenta reiniciar el ciclo. 
 + El fragmento <bloque_sigui> es el bloque de instrucciones que se ejecutan después de terminar de ejecutar el ciclo.

**Ejemplo 1:**
```python
<bloque_prev>
i = 0 #<inicia>
while(i <= 6): #<cond>
  print(i) #<bloque>
  i = i + 1 #<actualiza> 
<bloque_sigui>
```

**Ejemplo 2:**
```python
<bloque_prev>
i = 2 # inicializa a i en 2
j = 25 # inicializa a j en 25
while i < j: # mientras i sea menor a j
  print(i, j, sep = ", ") # imprime los valores de i y j usando el parametro separador 
  i *= 2 # i = i * 2; i se multıplica por 2 en cada paso
  j += 10 # j = j + 10; se incrementa de 10 en 10
print("the end.") # se ejecuta al terminar el ciclo
print(i, j, sep = ", ") # valores finales de i y j
<bloque_sigui>
```

**Ejercicios:**
1. Diseñe un algoritmo que involucre un ciclo y que nunca ingrese al ciclo.
2. Diseñe un algoritmo que involucre un ciclo y que se ejecute indefinidamente.
3. Diseñe un algoritmo que pida un valor entero, y que siga leyendo valores enteros mientras que alguno de esos valores no represente el código [ASCII](https://elcodigoascii.com.ar/) de una letra mayúscula en el abc del inglés.

### Ciclo do-while
Existe otra estructura c´ıclica en programación, ésta se conoce como un ciclo *hacer-mientras* (do). Esta estructura es casi equivalente a la estructura mientras (while), ya que usualmente se utiliza cuando con seguridad y de forma anticipada se sabe que se **hará al menos una evaluación del bloque principal del ciclo**. En esta estructura c´ıclica la verificación de la condición de parada se realiza al final del ciclo

**Diagrama de flujo:**
<div align='center'>
<figure> <img src="https://i.postimg.cc/zBWKcxyY/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b>Diagrama de flujo ciclo <i>do-while</i></b></figcaption></figure>
</div>

Si bien en Python no existe una forma dedicada para realizar el ciclo *do-while* (a diferencia de por ejemplo C), la siguiente es una implmentación al flujo del ciclo.

**Python:**
```python
<bloque_prev>
<inicia>
<bloque>
<actualiza>
  while(<cond>):
  <bloque>
  <actualiza>
<bloque_sigui>
```
**Disclaimer:** Nótese que se ejecuta una vez el contenido del ciclo antes y luego se repite hasta que la condición lo establezca.

### Uso de banderas 
Para evitar duplicar código al implementar un ciclo *do while* se pueden usar booleanos para agregar condiciones adicionales en la validación del ciclo y controlar el flujo.

**Python:**
```python
<bloque_prev>
<inicia>
bandera = True
  while(bandera or <cond>):
  bandera = False
  <bloque>
  <actualiza>
<bloque_sigui>
```

**Ejemplo 4:** Implementar ej ejercicio 4 usando un *do while* con bandera.

```python
bandera : bool = True
while bandera or (num < 65 or num > 90):
  bandera = False
  num = int(input("Ingrese un entero: "))
  print("El entero corresponde al caracter " + chr(num))
```

### break y continue
*break* y *continue* son palabras reservadas para controlar el flujo de ejecución de una estructura de iteraicón o selección en Python.

+ **continue:** Permite terminar la ejecución de la iteración actual pasando a la siguiente evaluación del ciclo. **Traucción** es la salida forzada de la iteración *actual* del ciclo.

+ **break:** Termina la ejecución del ciclo sin que se evaluen más condiciones. **Traducción** es la salida forzada de un ciclo.

**Pro tip:** El uso indiscriminado del *break* puede llevar al diseño pobre de algoritmos ya que se que por facilidad no se evaluan adecuadamente las condiciones de terminación de los ciclos.


**Ejemplo 5:** Hacer un programa que imprima los números del 1 al 10, exceptuando el 5.

```python
i : int = 0 
while(i < 10): 
  i += 1 
  if i == 5: 
    continue
  print(i) 
```

**Ejemplo 6:** Desarrollar un programa que lea números enteros y los sume hasta que lea un cero (0).

```python
sum : int = 0
while True:
  num = int(input("Ingrese un entero o  0 para salir: "))
  if num == 0:
    break
  sum += num
  print("La suma de los numeros ingresados es " + str(sum))
print("Ciclo terminado")
```

**Ejemplo 7:** Implementar el *ejemplo 6* sin usar la instrucción *break*.

```python
sum : int = 0
# num : int = 1 # Se puede eliminar el uso de la bandera declarando dato diferente de 0
bandera : bool = True
while bandera or num != 0: 
  bandera = False
  num = int(input("Ingrese un entero o  0 para salir: "))
  sum += num
  print("La suma de los numeros ingresados es " + str(sum))
print("Ciclo terminado")
```

## Reto 7
Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual asimismo cree un notebook con la solución a todos los problemas. Al finalizar suba todo a un repo y subalo al canal reto_7 en slack, los tres primeros puntos deben incluir diagrama de flujo.

**Nota:** Todo el código de aquí en adelante debe ir debidamente documentado.

1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
2.  Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
3.  Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
4. En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18:9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a
la de A.
5. Imprimir el factorial de un número natural n dado.
6. Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.
7. Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.
8. Implementar el algoritmo que muestre los números primos del 1 al 100. **nota:** use funciones

