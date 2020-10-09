from clases_pirinola.clsPartida import Partida


class Pirinola:
    def __init__(self,nombre_piri,id_partida,valor_partida):
        self.nombre_piri=nombre_piri
        self.partida = Partida(id_partida,valor_partida)

    def iniciar_juego(self):
        self.numero_jugadores=int(input("Digite numero Jugadores"))
        nu=0
        while( nu < self.numero_jugadores):
            nombre=input("Digite nombre Jugador")
            self.partida.add_jugador(nombre)
            nu=nu+1
