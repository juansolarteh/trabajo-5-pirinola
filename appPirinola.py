from clases_pirinola import Pirinola
from capaExterna import Menu

def ingresarDatoInt(texto):
    while True:
        dato = input(texto)
        try:
            return int(dato)
        except:
            print()
            print("debe ingresar un dato numerico")
            print()

#Creacion del menu, iteracion del menu, procesamiento de eleccion de opcion
mnuPirinola = Menu("PIRINOLA",["JugarPartida","Historial partidas","Reiniciar juego","Salir"],
                   "Digite una opcion: ")
listaPirinola = list()
piri = None

#Iteracion
while True:
    opcion = mnuPirinola.darOpcion()
    if opcion == 1:
        if piri == None:
            valorApuesta = ingresarDatoInt("Digite el valor de la apuesta: ")
            #Creacion de la pirinola
            piri = Pirinola()
            #Creacion de partida con el monto de apuesta
            piri.crearPartida(valorApuesta)
            #Agrgacion de jugadores al juego "Falta pedir los montos iniciales de cada jugador"
            piri.iniciar_juego()
            #iteracion del una ronda(partida)
            piri.jugarPartida()
        else:
            pass
            #Toca configurar si ya existe una pirinola (Ya se inicio un juego), que continue
            #el juego de Pirinola piri
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    else:
        break
    #Despues de cualquier opcion difernte a la de salir escribe el menu y pide opcion internamente
    mnuPirinola.regresarMenu()




##Marque con "XXXXX" los puntos realizados
##LO mas importante la aplicacion debe quedar en capas o paquetes
# El jugador debe tener un plante que va subiendo o bajando segun las partidas
## se debe calcular el acumulado en cada turno XXXXX
## la pirinola debe tener barias partidas, y se debe saber consultar quien gano y cuando en cada partida
## el jugador que quede sin plante debe salir del juego
## en cada turno se debe imprimir el acumulado que va quedando XXXXX, ademas el plante del jugador que lanza
## la aplicacion debe quedar en capas o paquetes XXXXX
## la opcion de lanzar para cada jugador debe activarse con el enter
## hacer un menu  con las opciones XXXXX

##Cree la clase historialPartida, y la clase pirinola tiene una lista de historialPartida.
##pero no he agregado ni actualizado el historial