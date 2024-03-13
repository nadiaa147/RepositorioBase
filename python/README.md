## *Programación en Python:*

A diferencia de markdown, que solo ayuda a la legibilidad de un texto, Python puede hacer otro tipo de operaciones ya que se usa para programar.

### Tipos de lenguaje:


- *Lenguaje de alto nivel:* Es aquel que se parece más al lenguaje humano. Sobretodo en la sintaxis.
- *Lenguaje de bajo nivel:* Es aquel que está formado por números.

### Tipos de tipado:

- *Tipado fuerte:* Es aquel que diferencia claramente los tipos de variables.
- *Tipado dinámico:* En este tipado la diferenciación se hace sobre la marcha.
                     Se asigna el tipo cuando se define el valor.


```
Qué son las librerías?

Es donde se guardan programas auxiliares
```

## *En Python:*

`#: Es un comentario. Es Utilizado para comentar lo que hacemos`


`\: Se usa para continuar la línea abajo ya que una misma instrucción puede estar dividida en varias líneas.`

### Identación:

Se usa para mover algo a la derecha para indicar que forma parte del bloque anterior.
Se puede usar el tabulador o 4 espacios.


----



```mermaid
flowchart TD
    A[Tipos de variables] --> B(Numéricos)
    A[Tipos de variables] --> C(Texto)
    A[Tipos de variables] --> D(Boleano)
    B(Numéricos) --> E(Enteros)
    B(Numéricos) --> F(Decimales)
    B(Numéricos) --> G(Complejos)
    C(Texto) --> H(Cadenas)
    D(Boleano) --> I(True)
    D(Boleano) --> J(False)
```


---


```mermaid
flowchart TD
    A[Tipos de operadores] --> B(Aritméticos)
    A[Tipos de operadores] --> C(Comparación)
    A[Tipos de operadores] --> D(Lógicos)
    A[Tipos de operadores] --> E(Asignación)
    A[Tipos de operadores] --> F(Especiales)
    B[Aritméticos] --> G(Suma)
    G(Suma) --- H(Resta)
    H(Resta) --- I(Multiplicación)
    I(Multiplicación) --- J(División)
    J(División) --- K(Exponente)
    K(Exponente) --- L(Módulo)
    L(Módulo) --- M(División entera)
    C[Comparación] --> N(Igual que: ==)
    N(Igual que: ==) --- O(Diferente de: !=)
    O(Diferente de: !=) --- P(Mayor que: >)
    P(Mayor que: >) --- Q(Menor que: <)
    Q(Menor que: <) --- R(Mayor y igual que: >=)
    R(Mayor y igual que: >=) --- S(Menor y igual que: <=)
    D[Lógicos] --> T(AND)
    T(And) --- U(OR)
    U(OR) --- V(NOT)
    F[Especiales] --> W(IS)
    W(IS) --- X(IS NOT)
    X(IS NOT) --- Y(IN)
    Y(IN) --- Z(NOT IN)
    E[Asignación] -->  AA(Igual: =)
    AA(Igual: =) --- AB(Incremento: +=)
    AB(Incremento: +=) --- AC(Decremento: -=)
    AC(Decremento: -=) --- AD(Dividir: /*)
    AD(Dividir: /*) --- AE(Multiplicar: *x)
    AE(Multiplicar: *x) --- AF(Cociente: //*)
    AF(Cociente: //*) --- AG(Potencia: **x)
```


---


### **VARIABLE:**

Es el espacio en la memoria del ordenador dónde se almacenará un valor que podrá cambiar durante la ejecución del programa.

*Cortesía*: Consiste en asignar a la variable un nombre que siempre empiece por minúscula. Puede llevar un número pero no empezar por él. 
            Se deben usar serpientes, es decir, barras bajas.
            
El valor está determinado por el contenido, no por el contenedor


```
"número = 5"

"número" es el contenedor y "5" es el contenido
```


Para que nos diga el tipo debemos usar:

`print type (nombre)`


### **FUNCIONES:**

Son un conxunto de lineas de código agrupadas que funcionan como unha unidad realizando unha tarea específica.
Pueden devolver valores ou non e poden ter parámetros ou non.

En *POO* (Programación Orientada a Objeto) se llaman métodos.
Una función de un objeto, en realidad, es un método. Primero se definen y después se les llama, por lo tanto tienen nombre

Una función es un objeto que en realidad puede ser un método. Primero se definen y después se les llama, por lo tanto tienen nombre.

#### *Sintaxis:*

```
def nombre_función(parámetros):
  instrucións da función
  return (opcional)
```
La primera línea es la declaración de la función, y el código que forma parte de esta debe ir identado.

#### *Ejecución:*
Consiste en llamar a la función

Si la función no recibe parámetros:
`nombre_función()`

Si los recibe:
`nombre_funición(parámetros)`


El **flujo de ejecución** de un programa siempre va de arriba a abajo excepto si se encuentra con funciones y bucles. 


### **LISTAS:**

Estructuras de datos que nos permiten almacenar grandes cantidad de valores. (Equivalente a los array en otros lenguajes de programación).
En Python las listas pueden guardas varios tipos de valores.
Se pueden expandir dinámicamente añadiendo nuevos elementos. De esta manera las listas se pueden ampliar (es una novedad en cuanto a otros lenguajes).

#### *Sintaxis:*
`nombreLista= [elem1, elem2, elem3, ...]`

La posición del elemento dentro de la lista es el índice. Este empieza en "0"
Cuando queremos imprimir la lista entera, la sintaxis sería la siguiente:

`print(miLista[:])`

Cuando queremos acceder a un elemento en concreto habría que escribir el índice de este elemento.

`print(miLista[<un número>])`

### *Métodos de listas:*
Un método es una función dentro de un objeto.
El método
`append`
agrega elementos a la lista.

```
miLista.append("<elem>")
```

Si queremos agregar el elemento en un lugar específico debemos utilizar `insert`.

```
miLista.insert(<índice>,<elem>)
```

`extend` se utiliza para agregar otra lista, no nuevos elementos.

```
miLista.extend(["<elem>","<elem>","<elem>"])
```

Utilizamos `index` para saber el índice de algún elemento.

```
print(miLista.index(“<elem>”))
```

### *Funciones:*

- `in` es una función interna. Se usa para saber si hay o buscar algún elemento en la lista.
- `remove` se usa para borrar un elemento de la lista.
- `pop` se usa para eliminar el último elemento de una lista.

#### *Operadores:*

Con el operador (+) **suma** se pueden unir listas. Es el “catenador” o “cat”.
Con el operador (*) **multiplicación**  podemos repetir la lista la cantidad de veces por las que la multipliquemos.


### **ESTRUCTURAS DE CONTROL DE FLUJO:**

El flujo de ejecución de un programa es el **orden** en el que se ejecutan sus instrucciones.
En Python, normalmente, el orden normal es de arriba abajo. Pero hay estructuras de control de fujo que modifican las instrucciones.

Las estructuras condicionales pueden romper este flujo.

-  #### *Condicionales:*

Las condiciones a evaluar dan como resultado verdadero (true) o falso (false). Si la condición es verdadera se ejecutan los bloques identados dentro del IF, si es falsa, el resto de instrucciones no se ejecutan, por lo que se rompe el flujo normal. Después se continua haciendo el resto de instrucciones.

  #### *Sintaxis:*

```
if <condición>
  *identación*
```

--------------------------------------------------

- En Python existe la función `input`, que es predefinida y sirve para introducir datos por el teclado. Lo que recibe lo convierte en datos de texto.
- `int(_)` transforma en entero los distintos parámetros.

---------------------------------------------------

**Ámbito de una variable:** La parte del programa desde donde es accesible la variable. Si una variable es global es accesible en todo el programa.

`else` (y si no es verdad) se ejecuta cuando la condición da como resultado falso. Se usa para ejecutar un código sin que sea una condición. Siempre es compañero del if más cercano.




