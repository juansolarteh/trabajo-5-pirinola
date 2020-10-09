from clases_pirinola.clsJugador import Jugador
from clases_pirinola.clsTurno import Turno


class Partida:
    def __init__(self, id_partida, valor_partida):
        self.id_partida = id_partida
        self.valor_partida = valor_partida
        self.lista_jugadores = list()
        self.lista_turnos = list()
        self.acumulado = self.calcular_acumulado_inicial()

    def add_jugador(self, nombre):
        self.lista_jugadores.append(Jugador(nombre))

    def listar_jugadores(self):
        for juga in self.lista_jugadores:
            dato = getattr(juga, 'nombre_jugador')
            print(dato)

    def calcular_acumulado_inicial(self):
        valor = self.valor_partida * len(self.lista_jugadores)
        return valor

    def add_turno(self, jugador, id_turno):
        self.lista_turnos.append(Turno(jugador, id_turno))

    def inicia_turnos(self):
        resultado_turno = ''
        n_jugador = 0
        n_turno = 0
        while (resultado_turno != 'TomaTodo'):
            print("Lanza jugador", self.lista_jugadores[n_jugador].get_nombre())
            self.lista_turnos.append(Turno(self.lista_jugadores[n_jugador].get_nombre(), n_turno))
            resultado_turno = self.lista_turnos[n_turno].retornar_valor_sacado()
            print("Valor ", resultado_turno, 'Turno', n_turno)
            print("------------------------------------------------------------")
            n_turno = n_turno + 1
            n_jugador = n_jugador + 1
            if (n_jugador == len(self.lista_jugadores)):
                n_jugador = 0