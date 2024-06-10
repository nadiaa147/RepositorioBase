import time

# Listas con terminos utilizados en el juego

verbos = ['coger', 'ir', 'poner', 'usar', 'ver']

objetos = ['espada', 'equipo', 'tiburón', 'peces', 'cofre', 'perla']

direcciones = ['norte', 'sur', 'este', 'oeste']

# Mapa del plano con sus salidas
#salidad[(columna,fila)]

salidas = {}
salidas [(0,0)] = ["norte", "oeste"]
salidas [(0,1)] = ["norte", "oeste","sur"]
salidas [(0,2)] = ["norte", "oeste", "sur"]
salidas [(0,3)] = ["norte", "oeste", "sur"]
salidas [(0,4)] = ["norte", "oeste", "sur"]
salidas [(0,5)] = []
salidas [(1,0)] = ["norte", "este", "oeste"]
salidas [(1,1)] = ["norte", "este", "oeste", "sur"]
salidas [(1,2)] = ["norte", "este", "oeste", "sur"]
salidas [(1,3)] = ["norte", "este", "oeste", "sur"]
salidas [(1,4)] = ["este", "oeste", "sur"]
salidas [(2,0)] = ["norte", "este", "oeste"]
salidas [(2,1)] = ["norte", "este", "oeste", "sur"]
salidas [(2,2)] = ["norte", "este", "oeste", "sur"]
salidas [(2,3)] = ["norte", "este", "oeste", "sur"]
salidas [(2,4)] = ["este", "oeste", "sur"]
salidas [(3,0)] = ["norte", "este"]
salidas [(3,1)] = ["norte", "este", "sur"]
salidas [(3,2)] = ["norte", "este", "sur"]
salidas [(3,3)] = ["norte", "este", "sur"]
salidas [(3,4)] = ["este", "sur"]

def intro():
    print("****************** BIENVENIDX A LA AVENTURA SUBACUÁTICA********************")
    print("----> ANTES DE COMENZAR TE DEJO AQUÍ LAS ACCIONES DISPONIBLES EN EL JUEGO<----")
    print("---->SIEMPRE QUE NECESITES VOLVER A VER LAS OPCIONES, ESCRIBE: AYUDA <----")
    time.sleep(3)
    print ( 'Debes usar verbos en infinitivo y después poner una dirección o un objeto para usar' ) 
    print ( 'Acciones disponibles:')
    for i in verbos: 
        print (i) 
    time.sleep(3)
    print("¡¡Mucha suerte en tu aventura!!")
    print("                         *** COMIENZA EL JUEGO ***")
    time.sleep(2)
    print ("Acabas de llegar al lago donde ibas a pasar tu día de vacaciones. Te tumbas en una toalla a disfrutar del sol.")
    time.sleep(2)
    print ("Ves en el suelo un sobre con una carta en la que dice que en el lago hay un tesoro...")
    print ("..por lo que dedides ir a por él.")
    time.sleep(2)
    print ()
    print ("Lo primero que necesitas es encontrar un equipo de buceo")
    time.sleep(2)
    print ()
    input("Pulsa <intro> para empezar el juego.")
    return

#____________________________________________________________________
#VER INVENTARIO 
def verInventario(o):
    if inventario == []: 
        print ( 'NO LLEVAS NADA EN ESTE MOMENTO')
        # Listar tus objetos
    else:
        print("Llevas contigo" + o) 
        for i in inventario:
            print(i)
            print()
    return


# Función que se encarga de describir cada sala, identificada como previamente 
# se ha comentado por una tupla de tres números. 
#____________________________________________________________________
#DESCRIBIR CADA CASILLA 
def describir(c,f):
    # f es la fila
    # c es la columna
    global juegoAcabado
    espacio = (c,f)
    if espacio == (0,0):
        print ("Sin equipo de buceo no puedes ir al lago, búscalo al oeste.")
        return juegoAcabado
    elif espacio == (0,1):
        print ("Estás dentro del lago.")
        print ("Escuchas un ruído al norte.")
        return juegoAcabado
    elif espacio == (0,2):
        print ("Te encuentras con muchísimos peces.")
        print ("Te sientes rodeado y algo asustado.")
        return juegoAcabado
    elif espacio == (0,3):
        print ("Estás a salvo de los peces")
        print ("Por ahora...")
        return juegoAcabado
    elif espacio == (0,4):
        print ("Estás en un lío...")
        print ("Un tiburón te ha visto y viene hacia ti")
        print ("Te sientes acorralado!")
        return juegoAcabado
    elif espacio == (0,5):
        print ("¡¡¡EL TESOROOOO!!! LO HAS ENCONTRADO, ¡ENHORABUENA!")
        ganar()
        juegoAcabado=True
        return juegoAcabado
    elif espacio == (1,0):
        print ("Aún no has encontrado el equipo de buceo, sigue buscando.")
        return juegoAcabado
    elif espacio == (1,1):
        print ("Estás dentro del lago.")
        print ("Tienes muchas ganas de encontrar el tesoro")
        return juegoAcabado
    elif espacio == (1,2):
        print ("Parece que todavía no has encontrado nada, pero...")
        print ("Escuchas un ruído al este.")
        return juegoAcabado
    elif espacio == (1,3):
        print ("Oh no! Peces!")
        print ("Te asustas porque te han rodeado completamente")
        return juegoAcabado
    elif espacio == (1,4):
        print ("¿Ya has explorado todo el lago?")
        print ("De momento no hay más criaturas marinas cerca.")
        return juegoAcabado
    elif espacio == (2,0):
        print ("Te encuentras el equipo de buceo.")
        return juegoAcabado
    elif espacio == (2,1):
        print ("Estás dentro del lago.")
        print ("Sigue buscando el tesoro")
        return juegoAcabado
    elif espacio == (2,2):
        print ("¿Has encontrado algo ya?")
        print ("Si vas a al oeste puede que tengas suerte")
        return juegoAcabado
    elif espacio == (2,3):
        print ("¿Has encontrado algo ya?")
        print ("Al este se escuchan ruidos, ve con cuidado")
        return juegoAcabado
    elif espacio == (2,4):
        print ("Un montón de peces te rodean")
        print ("No te dejan ver nada, tampoco te permiten moverte")
        return juegoAcabado
    elif espacio == (3,0):
        print ("Ya tienes el equipo de buceo, puedes ir al agua")
        print ("Para ir al agua tienes que ir al norte")
        return juegoAcabado
    elif espacio == (3,1):
        print ("Sigues en el lago")
        print ("Ya no puedes ir más hacia el oeste")
        return juegoAcabado
    elif espacio == (3,2):
        print ("Aquí hay algo...")
        print ("¡Has encontrado una espada!")
        time.sleep (0.5)
        print ("Podría serte de mucha ayuda...")
        return juegoAcabado
    elif espacio == (3,3):
        print ("Sigue buscando...")
        print ("Mira al norte hay una pequeña luz")
        return juegoAcabado
    elif espacio == (3,4):
        print ("Hay una luz brillante ante ti...")
        print ("¡Oh! Has encontrado una perla.")
        print ("¿Para qué crees que sirve?")
        return juegoAcabado
    
#____________________________________________________________________
#IR direcciones
def irDirecciones(d,columna,fila):
    global juegoAcabado
    juegoAcabado=False
    if d == 'norte':
        if visteEquipo:
            if (columna,fila)==(0,4):
                fila=fila+1 
                print ("-----------------------------------------------------------------------")
                print("AVANZAS AL NORTE")
                juegoAcabado=describir(columna,fila)
                return (columna,fila),juegoAcabado
            elif fila == 4:
                print ("-----------------------------------------------------------------------")
                print("NO PUEDES IR AL", d)
                return (columna,fila),juegoAcabado
            else:
                fila=fila+1 
                print ("-----------------------------------------------------------------------")
                print("AVANZAS AL NORTE")
                juegoAcabado=describir(columna,fila)
                return (columna,fila),juegoAcabado
        else:
            print ("-----------------------------------------------------------------------")
            print("NO PUEDES IR AL NORTE SIN PONERTE EL EQUIPO")
            return (columna,fila), juegoAcabado
    elif d == 'este':
        if columna==0:
            print ("-----------------------------------------------------------------------")
            print("NO PUEDES IR AL ESTE")
            return (columna,fila),juegoAcabado
        else:
            columna=columna-1
            print ("-----------------------------------------------------------------------")
            print("AVANZAS AL ESTE")
            juegoAcabado=describir(columna,fila)
            return (columna,fila),juegoAcabado
    elif d == 'sur':
        if columna==0:
            print ("-----------------------------------------------------------------------")
            print("NO PUEDES IR AL SUR")
            return (columna,fila),juegoAcabado
        else:
            columna=columna-1
            print ("-----------------------------------------------------------------------")
            print("AVANZAS AL SUR")
            juegoAcabado=describir(columna,fila)
            return (columna,fila),juegoAcabado
    elif d == 'oeste':
        if columna==3:
            print ("-----------------------------------------------------------------------")
            print("NO PUEDES IR AL OESTE")
            return (columna,fila),juegoAcabado
        else:
            columna += 1
            print ("-----------------------------------------------------------------------")
            print("AVANZAS AL OESTE")
            juegoAcabado=describir(columna,fila)
            return (columna,fila),juegoAcabado
    else:
        print ("-----------------------------------------------------------------------")
        print("NO EXISTE ESA DIRECCIÓN, PRUEBA OTRA VEZ")
        return (columna,fila)

#____________________________________________________________________
#COGER OBJETOS
def cogerObjetos(o,columna,fila, mapa):
    global tieneEspada, tienePerla, tieneEquipo
    if o == 'espada' and (columna, fila) == (3,2):
        inventario.append(o)
        mapa[(columna,fila)].remove(o)
        # Confirmar la acción
        tieneEspada = True
        print("..............................................")
        print ("Llevas contigo:" + o)
        print("..............................................")
        return (columna,fila),tienePerla,tieneEspada,tieneEquipo
    elif o == 'perla' and (columna,fila)==(3,4) :
        tienePerla=False
        inventario.append(o)
        mapa[(columna,fila)].remove(o)
        # Confirmar la acción
        tienePerla = True
        print("..............................................")
        print ("Llevas contigo:" + o)
        print("..............................................")
        return (columna, fila),tienePerla,tieneEspada,tieneEquipo
    elif o == 'equipo' and (columna,fila)==(2,0):
        inventario.append(o)
        mapa[(columna,fila)].remove(o)
        # Confirmar la acción
        tieneEquipo = True
        print("..............................................")
        print ("Llevas contigo:" + o)
        print("..............................................")
        return (columna, fila),tienePerla,tieneEspada, tieneEquipo
    elif o=='espada' or o=='perla' or o=='equipo' or(columna,fila)==(2,0) or (columna,fila)==(3,4) or (columna, fila) == (3,2): 
        print("Este objeto no está en esta posición, busca la posición correcta")
        return (columna, fila),tienePerla,tieneEspada,tieneEquipo
    else: 
        print("Este objeto no pertenece a este juego")
        return (columna,fila),tienePerla,tieneEspada, tieneEquipo

#____________________________________________________________________
#PONER OBJETOS
def ponerObjetos(o,tieneEquipo,visteEquipo):
    if o == 'equipo' and tieneEquipo==True:
        print("-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --")
        print("TE HAS PUESTO EL EQUIPO, YA PUEDES IR AL LAGO")
        print("-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --")
        inventario.remove(o)
        tieneEquipo=False
        visteEquipo=True
        return tieneEquipo,visteEquipo
    elif not tieneEquipo:
        print("No has cogido el equipo...no puedes ponertelo")
        return tieneEquipo, visteEquipo
    else:
        print("No puedes usar el verbo PONER con el objeto", o)
        return tieneEquipo,visteEquipo

#____________________________________________________________________
#USAR OBJETOS (Esta función comprueba el objeto que quieres usar y lo usa)
def UsarObjetos(o):
    if o == 'espada':
        if tieneEspada == True:
            print("****************************************")
            print ('Ahora puedes protegerte del tiburón.')
            print ('Has matado al tiburón.')
            print("****************************************")
            return False
        else:
            print("No tienes la espada, la encontrarás hacia el oeste")
            return True
    elif o == 'perla':
        if tienePerla == True:
            print("**************************************************************")
            print ('Puedes utilizar la piedra brillante para espantar a los peces')
            print ('Esta te ha salvado de los peces!')
            print("**************************************************************")
            return False
        else:
            print("No tienes la perla, la encontrás hacia noroeste")
            return True
    elif o == 'equipo':
        print("Con el equipo solo puedes usar los verbos: coger o poner.")
        return False
    else:
        print("Prueba con otro objeto ", o, "no existe en este juego")
        return False




#____________________________________________________________________
#USAR OBJETOS (Esta función hace que solo puedas usar la espada y la perla en las casillas
#de los peces y/o el tiburón, y también controla si sobrevives o te matan)
def UsarObjetos2(juegoAcabado):
    if (columna,fila)==(0,2) or (columna,fila)==(1,3) or (columna,fila)==(2,4):
            tiempo =0
            while tiempo <2:
                print("Decide rápido o morirás...")
                orden = input('--->¿Qué quieres hacer?<---').lower()
                palabras = orden.split()
                verbo = palabras[0]
                objeto = palabras[1]
                if verbo == 'usar' and objeto=='perla':   
                    juegoAcabado=UsarObjetos(objeto)
                    tiempo += 1
                    return juegoAcabado
                elif verbo=='coger' or verbo =='ir': 
                    print ("Esa acción no sirve")
                    tiempo += 1
                    juegoAcabado=juegoAcabado
                else:
                    juegoAcabado=procesar(orden,mapa)
                    tiempo += 1 
                    juegoAcabado=juegoAcabado
                if juegoAcabado==True or tiempo ==2:
                    print("<<<________________________________________>>>")
                    print("LO SIENTO...HAS SIDO MUY LENTO...TE HAN MATADO")
                    juegoAcabado=True
                    return juegoAcabado
    elif (columna,fila)==(0,4):
            tiempo =0
            while tiempo <2:
                print("Decide rápido o morirás...")
                orden = input('--->¿Qué quieres hacer?<---').lower()
                palabras = orden.split()
                verbo = palabras[0]
                objeto = palabras[1]
                if verbo == 'usar' and objeto=='espada':   
                    juegoAcabado=procesar(orden,mapa)
                    tiempo +=1
                    return juegoAcabado
                elif verbo=='coger' or verbo =='ir': 
                    print ("Esa acción no sirve")
                    tiempo += 1
                else:
                    juegoAcabado=procesar(orden,mapa)
                    tiempo += 1 
                if juegoAcabado==True or tiempo ==2:
                    print("<<<________________________________________>>>")
                    print("LO SIENTO...HAS SIDO MUY LENTO...EL TIBURÓN TE HA MATADO")
                    juegoAcabado=True
                    return juegoAcabado
    else:
        print ("No puedes usar ningún objeto en este lugar...")
        return juegoAcabado

#____________________________________________________________________
#PROCESAR INSTRUCCIONES 
def procesar(instrucciones, mapa):
    global fila, columna, juegoAcabado, inventario, objeto, verbos
    global tieneEspada, tienePerla, tieneEquipo, visteEquipo, verbo
   
    if instrucciones == '':
        print('No has escrito nada, prueba de nuevo')
        return
    
    if instrucciones == 'ayuda': 
        print ( 'Debes usar verbos en infinitivo y después poner una dirección o un objeto para usar' ) 
        print ( 'Acciones disponibles:')
        for i in verbos: 
            print (i) 
            print () 
        return
    
    # Separar la acción en palabras 
    palabras = instrucciones.split() 
    
    # El verbo ha de ser siempre el primero 
    verbo = palabras[0]
    if verbo not in verbos: 
        print ( "Perdona, no te entiendo")
        return
    # Separar las intrucciones en palabras 
    palabras = instrucciones.split() 
	# De esas palabras cogemos el verbo que es la primera palabra
    verbo = palabras[0]
    objeto = palabras[1]
    donde =palabras[1]
    
    if verbo == 'ir':
        if len(palabras) != 2 or palabras[1] not in direcciones:
            print ( "No entiendo a dónde tengo que ir.") 
            return juegoAcabado
        # Si la dirección elegida no está disponible, comunicarlo 
        donde = palabras[1]
        if donde not in salidas[(columna, fila)]: 
            print ( "NO PUEDES IR AL " + donde)
            return juegoAcabado
        # Con la dirección y las posiciones de columna y fila 
        #llamamos a la función irDirecciones
        (columna,fila),juegoAcabado =irDirecciones(donde,columna,fila)
        if (columna,fila)==(0,2) or (columna,fila)==(1,3) or (columna,fila)==(2,4) or (columna,fila)==(0,4):
            juegoAcabado=UsarObjetos2(juegoAcabado)
        return juegoAcabado
    elif verbo == 'poner':
        #Cogemos objeto de las palabras de las instrucciones
        objeto = palabras[1]
        tieneEquipo, visteEquipo =ponerObjetos(objeto,tieneEquipo,visteEquipo)
        return juegoAcabado
    elif verbo == 'coger':
        (columna,fila),tienePerla,tieneEspada,tieneEquipo = cogerObjetos(objeto,columna,fila, mapa)
        return juegoAcabado
    elif verbo == 'ver':
        verInventario(objeto)
        return juegoAcabado

#____________________________________________________________________
#GANAR 
def ganar():
    print ( '*******************************************************') 
    print ( '¡El resplandor de las monedas en el cofre te deslumbra!') 
    print ( '*************** ENHORABUENA, ENCONTRASTE **************') 
    print ( '*************** EL COFRE QUE BUSCABAS *****************')
    print ( '*******************************************************')
    return

while True:
    fila = 0
    columna = 0
    tieneEspada = False 
    tieneEquipodebuceo = False
    tienePerla = False
    visteEquipo = False
    inventario = [] 
    
    mapa ={} 
    mapa [(0,0)] = []
    mapa [(0,1)] = []
    mapa [(0,2)] = ["peces"]
    mapa [(0,3)] = []
    mapa [(0,4)] = ["tiburón"]
    mapa [(0,5)] = ["cofre"]
    mapa [(1,0)] = []
    mapa [(1,1)] = []
    mapa [(1,2)] = []
    mapa [(1,3)] = ["peces"]
    mapa [(1,4)] = []
    mapa [(2,0)] = ["equipo"]
    mapa [(2,1)] = []
    mapa [(2,2)] = []
    mapa [(2,3)] = []
    mapa [(2,4)] = ["peces"]
    mapa [(3,0)] = []
    mapa [(3,1)] = []
    mapa [(3,2)] = ["espada"]
    mapa [(3,3)] = []
    mapa [(3,4)] = ["perla"]
    
    
    o='inventario'
    juegoAcabado = False
    tiempo = 0
    
    print("------------------------------------------------")
    intro()
    
    while not juegoAcabado:
        if tiempo<25:
            tiempo += 1
            orden = input('--->¿Qué quieres hacer?<---').lower()
            juegoAcabado=procesar(orden,mapa)
        else:
            print("TE HAS QUEDADO SIN OXIGENO EN TU BOMBONA")
            print("¡¡TE HAS MUERTO!!")
            juegoAcabado=True
        
    continuar = input('¿Quieres jugar otra vez? ').lower().startswith('s') 
    if not continuar:
        break 
    
    
