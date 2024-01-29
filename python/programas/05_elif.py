nota_de_materia = int(input("Introduce tu nota")) #a la variable nota_de_materia se le asigna un valor numérico intoducido por el teclado. Este se transformará en un texto
if nota_de_materia > 10: #si el valor de la variable es mayor que 10 entonces la nota no es válida
    print("nota no válida")
if nota_de_materia < 0: #si el valor de la valiable es menor que 0 entonces la nota no es válida 
    print("nota no válida")
elif nota_de_materia < 5: #si el valor de la variable es menor que 5 entonces la nota es insuficiente
    print("insuficiente")
elif nota_de_materia==5: #si el valor de la variable es igual que 5 entonces la nota es suficiente
    print("suficiente")
elif nota_de_materia==6: #si el valor de la variable es igual que 6 entonces la nota está bien
    print("bien")
elif nota_de_materia==7: #si el valor de la variable es igual que 7 entonces la nota es un notable
    print ("notable")
elif nota_de_materia==8: #si el valor de la variable es igual que 8 entonces la nota es un notable
    print ("notable")
elif nota_de_materia==9: #si el valor de la variable es igual que 9 entonces la nota es un sobresaliente
    print ("sobresaliente")
elif nota_de_materia==10: #si el valor de la variable es igual que 10 entonces la nota es un sobresaliente
    print ("sobresaliente")