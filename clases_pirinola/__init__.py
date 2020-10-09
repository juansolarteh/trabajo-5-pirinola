from clases_pirinola.clsPartida import Partida


class Pirinola:
    def __init__(self):
        self.numeroPartida = 0
        self.listaHistorialPartidas = list()
        self.partidaActual = None

    def iniciar_juego(self):
        #itera hasta que el usuario ingrese un numero
        while True:
            self.numero_jugadores=input("Digite el numero de Jugadores: ")
            try:
                self.numero_jugadores = int(self.numero_jugadores)
                if self.numero_jugadores >= 1:
                    break
                else:
                    print("EL NUMERO DE JUGADORES TIENE QUE SER MAYOR A 1")
            except:
                print("DEBE INGRESAR UN DATO NUMERICO")
        nu=0
        while( nu < self.numero_jugadores):
            nombre=input("Digite nombre Jugador: ")
            self.partidaActual.add_jugador(nombre)
            nu=nu+1

    def crearPartida(self, valor_partida):
        self.partidaActual = Partida(self.numeroPartida, valor_partida)

    def jugarPartida(self):
        self.numeroPartida += 1
        self.partidaActual.id_partida = self.numeroPartida
        self.partidaActual.inicia_turnos()