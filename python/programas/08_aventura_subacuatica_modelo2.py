
# Importar los módulos que necesitar
import time

# Listas con terminos utilizados en el juego

verbos = ['coger', 'ir', 'sumergirse', 'abrir', 'atacar', 'poner', 'usar']

objetos = ['espada', 'equipo de buceo', 'tiburón', 'peces', 'cofre', 'perla']

direcciones = ['norte', 'sur', 'este', 'oeste']

# Mapa del plano con sus salidas

salidas = {}
salidas [(0,0)] = ["norte", "oeste"]
salidas [(1,0)] = ["norte", "este", "oeste"]
salidas [(2,0)] = ["norte", "este"]
salidas [(0,1)] = ["norte", "oeste"]
salidas [(0,2)] = ["norte", "oeste"]
salidas [(0,3)] = ["norte", "oeste"]
salidas [(0,4)] = ["norte", "sur", "oeste"]
salidas [(0,5)] = []
salidas [(1,1)] = ["norte", "este", "oeste"]
salidas [(1,2)] = ["norte", "sur", "este", "oeste"]
salidas [(1,3)] = ["norte", "sur", "este", "oeste"]
salidas [(1,4)] = ["sur", "este", "oeste"]
salidas [(2,1)] = ["norte", "este"]
salidas [(2,2)] = ["norte", "sur", "este", "oeste"]
salidas [(2,3)] = ["norte", "sur", "este", "oeste"]
salidas [(2,4)] = ["sur", "este", "oeste"]
salidas [(3,2)] = ["norte", "este"]
salidas [(3,3)] = ["norte", "sur", "este"]
salidas [(3,4)] = ["sur", "este"]

# Función que se encarga de describir cada sala, identificada como previamente 
# se ha comentado por una tupla de tres números. 

def describir(f,c):
    # f es la fila
    # c es la columna
        espacio = (f,c)
        print ("-----------------------------------------------------------------------")
        if espacio == (0,0):
            print ("Ves un equipo de buceo al oeste.")
        elif espacio == (1,0):
            print ("Aún no has encontrado el equipo de buceo, sigue buscando.")
        elif espacio == (2,0):
            print ("Te encuentras el equipo de buceo.")
            print ("Ahora ya puedes entrar al agua.")
        elif espacio == (0,1):
            print ("Estás dentro del lago.")
            print ("Escuchas un ruído al norte.")
        elif espacio == (1,1):
            print ("Estás dentro del lago.")
            print ("Tienes muchas ganas de encontrar el tesoro")
        elif espacio == (2,1):
            print ("Estás dentro del lago.")
            print ("Ves un camino que va hacia el norte.")
        elif espacio == (0,2):
            print ("Te encuentras con muchísimos peces.")
            print ("Te sientes rodeado y algo asustado.")
        elif espacio == (1,2):
            print ("Escuchas un ruído al este.")
        elif espacio == (2,2):
            print ("El camino continúa hacia el oeste.")
        elif espacio == (3,2):
            print ("El camino termina aquí...")
            print ("Has encontrado una espada!")
            time.sleep (0.5)
            print ("Podría serte de mucha ayuda...")
        elif espacio == (0,3):
            print ("Estás a salvo de criaturas.")
            print ("Por ahora...")
        elif espacio == (1,3):
            print ("Oh no! Peces!")
            print ("Te asustas")
        elif espacio == (2,3):
            print ("Estás a salvo, pero escuchas ruídos extraños hacia el este.")
        elif espacio == (3,3):
            print ("Ves una pequeña luz que viene por del norte.")
        elif espacio == (0,4):
            print ("Un tiburón!")
            print ("Te sientes acorralado!")
        elif espacio == (1,4):
            print ("Aquí te encuentras seguro.")
        elif espacio == (2,4):
            print ("Cuantos peces!")
            print ("Sientes algo de miedo ya que se acercan mucho a ti.")
        elif espacio == (3,4):
            print ("Has encontrado una perla!")
            print ("Para qué podrá servir?")
        elif espacio == (0,5):
            print ("Por fin has hayado el tesoro que buscabas!")
        
# Función que muestra en pantalla la introducción del Juego, con pausas.     
def intro():
   print ("Acabas de llegar al lago donde ibas a pasar tu día de vacaciones. Te tumbas en una toalla.")
   print ("Ves en el suelo un sobre con una carta en la que dice que en el lago hay un tesoro...")
   print ("..por lo que dedides ir a por él.")
   time.sleep(1)
   print ()
   print ("Necesitas encontrar un equipo de buceo")
   time.sleep(1)
   print ()
   input("Pulsa <intro> para empezar el juego.")

def proteccionAtaque(v,c): 
# v es el verbo; poner o usar
# c es perla, equipo de buceo o espada

    # Declarar los globales
    global inventario, juegoAcabado, tieneEspada, tienePerla, tieneEquipodebuceo
    
    #Comprobar que se lleva lo que se tiene
    if c not in inventario:
        print ('No tienes ' + c)
    	# Caso de querer usar... 
    if v == 'usar':
# ... perla 
        if c == 'perla': 
            print ('Has utilizado la piedra brillante.')
            print ('Esta te ha salvado de los peces!')
        # Activar el indicador de usado 
            tienePerla = True
# ... espada
        elif c == 'espada': 
            print ('Con esta espada puedes atacar al tiburón.')
            print ('Has matado al tiburón.')
        # Activar el indicador de usado 
            tieneEspada = True
        elif v == 'poner':
            if c == 'equipo de buceo':
                print ('Te has puesto el equipo de buceo.')
                print ('Ya puedes entrar en el agua.')
                tieneEquipodebuceo = True
                inventario.remove(objeto)
            else:
                print ('No puedes usar o ponerte + c.')
    # Activar el indicador de fin de juego
    
	# Función que procesa las acciones del jugador ('parser') 
def procesar(instrucciones): 
	   
	# Hay que declarar como globales las variables que pueden modificarse 
    global fila, columna, juegoAcabado, inventario, yaDescrito, sinEspada 
    global tieneEspada, tiburonVivo, tienePerla, tieneEquipodebuceo
	# Si no se ha escrito nada, no hacer nada 
    if instrucciones == '':
        return
	# Mostrar ayuda si se solicita 
    if instrucciones == 'ayuda': 
        print ( 'Debes usar verbos en infinitivo y, si lo necesitas, un nombre.' ) 
        print ( 'Acciones disponibles:')
        for i in verbos: 
            print ( i,) 
            print () 
        return

	
	# Separar la acción en palabras 
    palabras = instrucciones.split() 

	# El verbo ha de ser siempre el primero 
    verbo = palabras[0] 
	
	# Si el verbo es desconocido, no hacer nada y volver a preguntar 
    if verbo not in verbos: 
        print ( "Perdona, no te entiendo")
        return
	# Si el verbo es 'ir'... 
    if verbo == 'ir':
	# Comprobar que va acompañado de una direección 
        if len(palabras) != 2 or palabras[1] not in direcciones:
            print ( "No entiendo a dónde tengo que ir.") 
            return
	# Almacenar la dirección en la variable  
    donde = palabras[1] 
	# Si la dirección elegida no está disponible, comunicarlo 
    if donde not in salidas[(fila, columna)]: 
        print ( "No puedo ir hacia el " + donde)
        return
	# Desplazarse en la dirección solicitada 
    elif donde == "norte":
        if columna == 0 and tieneEquipodebuceo:
	        print ("Avanzas al norte y ya estás en el lago.") 
	        columna = columna + 1
	        return
        elif columna == (0) and not tieneEquipodebuceo:
	        print ("No tienes equipo de buceo, busca uno y póntelo")
	        return
    elif (fila,columna) == (0,4) and tieneEspada:
        # La segunda es cuando se ha atraviesa el pozo sin saltar 
        print ("Te encuentras con un tiburón")
        print ("Te recuerdo que tienes una espada")
        time.sleep(1) 
        print ("Qué quieres hacer?")
        return
    elif (fila, columna) == (0,4) and not tieneEspada:
        print ("Te encuentras con un tiburón y no tienes espada.")
        time.sleep(1)
        print ("Lo siento te ha comido.")
        juegoAcabado = True
        fila = fila - 1
        return

    if donde == "sur":
        if columna == 0 or columna == 1 or (fila,columna) == (3,2):
            print ("No puedes ir al sur.")
            return
        elif (fila, columna) == (0,2) or (fila, columna) == (1,3):
	        if tienePerla == True:
	            print ("Los peces no atacan porque tienes la perla.")
	            print ("Sigue buscando el cofre.")
	            return
	        else:
	            print ("No tienes la perla, los peces te matan")
	            juegoAcabado = True
	            return
        elif fila > 0:
            print("puedes ir al sur")
            fila = fila - 1
            return
    elif donde == "oeste":
        if columna < 4:
            print("puedes ir al oeste")
            return
            if (fila, columna) == (0,2) or (1,3) or (2,4):
                print(fila,columna)
                if tienePerla == True:
                    print ("Los peces no atacan porque tienes la perla.")
                    print ("Sigue buscando el cofre.")
                    return
                else:
                    print ("Te atacan unos peces. Oh no! Has muerto.")
                    juegoAcabado = True
                    return
        elif (fila,columna) == (0,4):
            if tieneEspada:
                print("Te encuentras con un tiburón")
                print ("Te recuerdo que tienes una espada")
                time.sleep(1)
                print ("Qué quieres hacer?")
                return
            else:
                print ("Te encuentras con un tiburón y no tienes espada.")
                time.sleep(1)
                print ("Lo siento te ha comido.")
                juegoAcabado = True
                columna = columna + 1
                return
    elif donde == 'este':
         if (fila, columna) == (1,3) or (2,4):
             if tienePerla == True:
                 print ("Los peces no atacan porque tienes la perla.")
                 print ("Sigue buscando el cofre.")
                 return
             else:
                     print ("No tienes la perla, los peces te matan")
                     juegoAcabado = True
                     return
         elif columna > 4:
                print ("Puedes avanzar")
                columna=columna-1 
                return
         elif columna < 4:
            print("puedes ir al este")
            columna=columna+columna-1
            return
    else:
        print ("Escoge otra dirección")
        return
	# Una vez que el jugador se ha movido, confirmarlo y activar el 
	# indicador de describir la nueva sala 
        print ( "Vas hacia el " + donde)
        yaDescrito = False
        return

    if verbo == 'poner': 
	# Asegurarse que se indica lo que se quiere poner 
	    if len(palabras) == 1:
	        print ('Perdona... ¿el qué?')
	        return
	    else:
	# Enviar a la función que gestiona el alimento, tanto si 
	# come o bebe como el qué 
	        proteccionAtaque(verbo, palabras[1]) 
	# Coger objetos 
    if verbo == 'coger':
	# Asegurarse que se indica lo que se quiere coger
	    if len(palabras) == 1:
	        print ('Perdona... ¿coger qué?')
	        return
    else:
        objeto = palabras[1]
	        
	# Comprobar que el objeto está en el espacio 
    if objeto in mapa[(fila,columna)]:
    # Añadirlo al inventario y quitarlo de la sala
        inventario.append(objeto)
        mapa[(fila,columna)].remove(objeto)
	# Confirmar la acción
        print ("Llevas contigo:" + objeto)
    elif (fila,columna)== (3,4) and objeto == "perla" and not tienePerla:
	# Añadir la perla al inventario
	    inventario.append(objeto)
	    tienePerla = True
	# Confirmar la acción
	    print ( 'Llevas contigo: ' + objeto)

    elif (fila,columna)== (3,2) and objeto == 'espada' and not tieneEspada:
	# Añadir la espada al inventario
	    inventario.append(objeto)
	    tieneEspada = True 
	# Confirmar la acción
	    print ( 'Llevas contigo: ' + objeto)

    elif (fila,columna)== (2,0) and objeto == 'equipo de buceo' and not tieneEquipodebuceo:
	# Añadir la espada al inventario
        inventario.append(objeto)
        tieneEquipodebuceo = True
        print('Llevas contigo:' + objeto)
    else:
        print ( 'No puedo hacer eso.')
	
	# Mostrar el inventario 
    if verbo == 'inventario': 
    # Verificar que llevas algo
     if inventario == []: 
        print ( 'No llevas nada')
    # Listar tus objetos
        print("Llevas contigo" + objeto) 
    for i in inventario: 
        print(i) 
        print() 
	# Atacar al tiburón 

	
	# Función que gestiona las felicitaciones al ganar el juego 
def ganar():
    print ( '******************************************') 
    print ( '¡El resplandor de las joyas te deslumbra!') 
    print ( '******** ENHORABUENA, ENCONTRASTE ********') 
    print ( '********* EL COFRE QUE BUSCABAS ***********')
    print ( '******************************************') 
	
	# Bucle general, necesario por si se quiere volver a jugar 
while True: 
    fila = 0
    columna = 0
    tieneEspada = False 
    tieneEquipodebuceo = False
    tienePerla = False
    inventario = [] 
    mapa ={} 
    mapa [(0,0)] = []
    mapa [(1,0)] = []
    mapa [(2,0)] = ["equipo de buceo"]
    mapa [(0,1)] = []
    mapa [(0,2)] = ["peces"]
    mapa [(0,3)] = []
    mapa [(0,4)] = ["tiburón"]
    mapa [(0,5)] = ["cofre"]
    mapa [(1,1)] = []
    mapa [(1,2)] = []
    mapa [(1,3)] = ["peces"]
    mapa [(1,4)] = []
    mapa [(2,1)] = []
    mapa [(2,2)] = []
    mapa [(2,3)] = []
    mapa [(2,4)] = ["peces"]
    mapa [(3,2)] = ["espada"]
    mapa [(3,3)] = []
    mapa [(3,4)] = ["perla"]
    juegoAcabado = False 
    yaDescrito = False 
    tiempo = 0
    tiburonVivo = True 
    intro()
    break
		# Bucle de juego. Se repite una y otra vez mientras dura el juego 
while True: 
    if not yaDescrito: 
	    describir(fila, columna) 
	    yaDescrito = True 
	# Pedir al jugador que realice una acción 
    orden = input('¿Qué quieres hacer? ').lower()
	
	# Aumentar el tiempo 
    tiempo = tiempo + 1 
	
	# Procesar la acción y ejecutarla 
    procesar(orden) 
	# Si no se ha bebido pasado un tiempo, se pierde si ya no se ha hecho 
    if tiempo>25 and not juegoAcabado: 
        print ('Tu bombona de oxígeno se ha terminado') 
        time.sleep(1) 
        print ('Te quedas sin aire y te desmayas...')
        juegoAcabado = True 
	# Si has pasado demasiado tiempo en presencia del tiburón 
	# o si está activo, te ataca. 
	# Pero siempre que no lo haya hecho ya y estés muerto 
    
	# Si el juego ha terminado, salir del bucle 
    if juegoAcabado:
        break

    print () 
    print ( '---------------------------------------------------') 
    continuar = input('¿Quieres jugar otra vez? ').lower().startswith('s') 
    if not continuar:
        break 
        print ( '---------------------------------------------------') 
        print ()
