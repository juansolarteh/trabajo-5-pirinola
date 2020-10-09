from clases_pirinola.clsJugador import Jugador
from clases_pirinola.clsTurno import Turno


class Partida:
    def __init__(self, id_partida, valor_partida):
        self.id_partida = id_partida
        self.valor_partida = valor_partida
        self.lista_jugadores = list()
        self.lista_turnos = list()
        self.acumulado = 0

    def add_jugador(self, nombre):
        self.lista_jugadores.append(Jugador(nombre, 500))

    def listar_jugadores(self):
        for juga in self.lista_jugadores:
            dato = getattr(juga, 'nombre_jugador')
            print(dato)

    def calcular_acumulado_inicial(self):
        valor = self.valor_partida * len(self.lista_jugadores)
        return valor

    def add_turno(self, jugador, id_turno):
        self.lista_turnos.append(Turno(jugador, id_turno))

    def verificarJugadores(self):
        for jugador in self.lista_jugadores:
            if jugador.monto == 0:
                print("Jugador " + jugador.nombre_jugador + " salio del juego")
                self.lista_jugadores.remove(jugador)


    def inicia_turnos(self):
        self.verificarJugadores()
        self.acumulado = self.calcular_acumulado_inicial()
        n_jugador = 0
        n_turno = 0
        print("------------------------------------------------------------")
        while (self.acumulado > 0):
            self.verificarJugadores()
            print("Lanza jugador", self.lista_jugadores[n_jugador].get_nombre())
            self.lista_turnos.append(Turno(self.lista_jugadores[n_jugador], n_turno))
            resultado_turno = self.lista_turnos[n_turno].retornar_valor_sacado()
            print("Valor ", resultado_turno, 'Turno', n_turno)
            self.__ajustarAcumulado(resultado_turno)
            print("Acumulado actual ", self.acumulado)
            print("------------------------------------------------------------")
            n_turno = n_turno + 1
            n_jugador = n_jugador + 1
            if (n_jugador == len(self.lista_jugadores)):
                n_jugador = 0

#De acuerdo al re4sultado de la pirinola
    def __ajustarAcumulado(self,resultado_turno):
        if resultado_turno == 'Toma1':
            self.acumulado -= self.valor_partida
        elif resultado_turno == 'Toma2':
            if self.acumulado == self.valor_partida:
                self.acumulado = 0
            else:
                self.acumulado -= (self.valor_partida * 2)
        elif resultado_turno == 'Pon1':
            self.acumulado += self.valor_partida
        elif resultado_turno == 'Pon2':
            self.acumulado += (self.valor_partida * 2)
        elif resultado_turno == 'TodosPonen':
            self.acumulado += (self.valor_partida * len(self.lista_jugadores))
        else:
            self.acumulado = 0