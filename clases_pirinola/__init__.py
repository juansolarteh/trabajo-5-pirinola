#Juan Pablo Solarte
#Jorge Ivan Solano
from clases_pirinola.clsPartida import Partida
from clases_pirinola.clsHistorialPartida import HistorialPartida

class Pirinola:
    def __init__(self):
        self.numeroPartida = 0
        self.listaHistorialPartidas = list()
        self.partidaActual = None

    def ingresarDatoInt(self,texto):
        while True:
            dato = input(texto)
            try:
                return int(dato)
            except:
                print()
                print("debe ingresar un dato numerico")
                print()

    def crearPartida(self, valor_partida):
        self.partidaActual = Partida(self.numeroPartida, valor_partida)

    def jugarPartida(self):
        if len(self.partidaActual.lista_jugadores)==1:
            print("Solo hay un jugador, no se puede jugar más, Reinicie el Juego.")
            return
        self.numeroPartida += 1
        self.partidaActual.id_partida = self.numeroPartida
        self.partidaActual.inicia_turnos()
        if self.partidaActual.ganador is not None:
            his = HistorialPartida(self.numeroPartida,self.partidaActual.ganador.get_nombre(),
                                   self.partidaActual.valor_ganado-self.partidaActual.get_valor_partida(),
                                   self.partidaActual.ganador.get_monto())
        else:
            his = HistorialPartida(self.numeroPartida, "EMPATE",0,0)
        self.listaHistorialPartidas.append(his)

    def iniciar_juego(self):
        #itera hasta que el usuario ingrese un numero
        while True:
            self.numero_jugadores=self.ingresarDatoInt("Digite el numero de Jugadores: ")
            if self.numero_jugadores>1:
                break
            else:
                print("EL NUMERO DE JUGADORES TIENE QUE SER MAYOR A 1")
        nu=0
        while( nu < self.numero_jugadores):
            nombre=input("Digite nombre Jugador "+str(nu+1)+": ")
            while True:
                monto=self.ingresarDatoInt("Digite el monto del Jugador "+nombre+": ")
                if monto >= self.partidaActual.get_valor_partida():
                    break
                else:
                    print("El monto debe ser mayor a la apuesta inicial")
            self.partidaActual.add_jugador(nombre, monto)
            nu = nu + 1

