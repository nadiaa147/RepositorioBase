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
