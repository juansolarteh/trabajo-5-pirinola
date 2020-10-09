from random import randint
from clases_pirinola.clsJugador import Jugador


class Turno:

    def __init__(self,jugador,id_turno):
        self.jugador=Jugador(jugador)
        self.id_turno=id_turno
        self.valor_sacado = self.retornar_valor_sacado()

    def retornar_valor_sacado(self):
        valores=['Toma1','Toma2','Pon1','Pon2','TodosPonen','TomaTodo']
        valor_opcion = randint(0,5)
        return valores[valor_opcion]