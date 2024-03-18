def tabla_de_multiplicar ():
    for i in range (1,11):
        print(f"Tabla del {i}:")
        for h in range (1,11):
            resultado = i * h
            print (f"{i} * {h} = resultado")
            
tabla_de_multiplicar()