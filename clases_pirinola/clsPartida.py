#Juan Pablo Solarte
#Jorge Ivan Solano

from clases_pirinola.clsJugador import Jugador
from clases_pirinola.clsTurno import Turno


class Partida:
    def __init__(self, id_partida, valor_partida):
        self.id_partida = id_partida
        self.valor_partida = valor_partida
        self.lista_jugadores = list()
        self.lista_turnos = list()
        self.ganador=None
        self.empate=True
        self.valor_ganado=0
        self.n_jugador=0
        self.acumulado = 0
        self.todosEmpate = False

    def add_jugador(self, nombre,monto):
        self.lista_jugadores.append(Jugador(nombre,monto))

    def get_valor_partida(self):
        return self.valor_partida

    def listar_jugadores(self):
        for juga in self.lista_jugadores:
            print("Nombre: "+juga.get_nombre+" Monto Actual: "+juga.get_monto)

    def calcular_acumulado_inicial(self):
        valor = self.valor_partida * len(self.lista_jugadores)
        return valor

    def add_turno(self, jugador, id_turno):
        self.lista_turnos.append(Turno(jugador, id_turno))

    
    def verificarJugadores(self,listaAux):
        posicion=0
        for jugador in self.lista_jugadores:
            if jugador.monto>0:
                self.empate=False
                break
        if self.empate == True:
            return
        for jugador in self.lista_jugadores:
            if jugador.monto <= 0:

                print("Jugador " + jugador.nombre_jugador + " salió del juego")
                self.lista_jugadores.remove(jugador)
                listaAux.pop(posicion)
                self.n_jugador-=1
            posicion+=1

    def inicia_turnos(self):
        self.empate=True
        listaAux = list()
        self.darPrimeraApuesta()
        for i in self.lista_jugadores:
            listaAux.append(i.get_monto())
        #self.verificarJugadores(listaAux)
        self.acumulado = self.calcular_acumulado_inicial()
        self.n_jugador = 0
        n_turno = 0
        print("------------------------------------------------------------")
        while (self.acumulado > 0 and len(self.lista_jugadores)>1):
            print("Lanzamiento de: ", self.lista_jugadores[self.n_jugador].get_nombre())
            input("Presione ENTER para lanzar la pirinola...")
            self.lista_turnos.append(Turno(self.lista_jugadores[self.n_jugador], n_turno))
            resultado_turno = self.lista_turnos[n_turno].retornar_valor_sacado()
            print("Turno: "+str(n_turno+1)+" Valor de Turno: "+resultado_turno)
            self.__ajustarAcumulado(resultado_turno,self.lista_jugadores[self.n_jugador])
            print("Monto de Jugador: ",self.lista_jugadores[self.n_jugador].monto)
            print("Acumulado de Partida: ", self.acumulado)
            print("------------------------------------------------------------")
            self.verificarJugadores(listaAux)
            if self.empate==True:
                self.dividirAcumulado()
                print("Todos los jugadores terminaron con 0 pesos")
                print("Hubo un empate, se repartió el acumulado en el número de jugadores restantes")
                break
            n_turno = n_turno + 1
            self.n_jugador = self.n_jugador + 1
            if (self.n_jugador == len(self.lista_jugadores)):
                self.n_jugador = 0
        if len(self.lista_jugadores)==1:
            self.lista_jugadores[0].sumarPlante(self.acumulado)
            self.acumulado = 0
        print("Ronda terminada")
        self.definirTodosEmpate(listaAux)
        if self.empate==False:
            self.ganador,self.valor_ganado=self.definirGanador(listaAux)
        else:
            self.ganador=None
#De acuerdo al re4sultado de la pirinola
    def __ajustarAcumulado(self,resultado_turno,jugador:Jugador):
        if resultado_turno == 'Toma1':
            if self.acumulado==self.valor_partida:
                self.acumulado=0
            else:
                self.acumulado -= self.valor_partida
            jugador.sumarPlante(self.valor_partida)
        elif resultado_turno == 'Toma2':
            if self.acumulado == self.valor_partida:
                self.acumulado = 0
                jugador.sumarPlante(self.valor_partida)
            else:
                self.acumulado -= (self.valor_partida * 2)
                jugador.sumarPlante(self.valor_partida * 2)

        elif resultado_turno == 'Pon1':
            jugador.restarPlante(self.valor_partida)
            self.acumulado += self.valor_partida
        elif resultado_turno == 'Pon2':
            if jugador.monto == self.valor_partida:
                self.acumulado += (self.valor_partida)
                jugador.restarPlante(self.valor_partida)
            else:
                self.acumulado += (self.valor_partida*2)
                jugador.restarPlante(self.valor_partida * 2)
        elif resultado_turno == 'TodosPonen':
            for jugador in self.lista_jugadores:
                jugador.restarPlante(self.valor_partida)
            self.acumulado += (self.valor_partida * len(self.lista_jugadores))
        else:
            jugador.sumarPlante(self.acumulado)
            self.acumulado = 0

    def definirGanador(self,listaMontoInicial):
        valor=0
        ganador=None
        for posJug in range (len(self.lista_jugadores)):
            montActualJugador=self.lista_jugadores[posJug].get_monto()
            montInicialJugador=listaMontoInicial[posJug]
            resta = montActualJugador-montInicialJugador
            if resta>valor:
                valor=resta
                ganador=self.lista_jugadores[posJug]
        return ganador,valor

    def definirTodosEmpate(self,listaMontoInicial):
        restas = list()
        if len(listaMontoInicial) == 1:
            self.empate = False
            return
        for posJug in range (len(self.lista_jugadores)):
            montActualJugador=self.lista_jugadores[posJug].get_monto()
            montInicialJugador=listaMontoInicial[posJug]
            resta = montActualJugador-montInicialJugador
            restas.append(resta)
        valor = restas[0]
        for i in restas:
            if i != valor:
                self.empate = False
                return
        self.empate = True

    def dividirAcumulado(self):
        div=self.acumulado/len(self.lista_jugadores)
        for jug in self.lista_jugadores:
            jug.monto=div

    def darPrimeraApuesta(self):
        for jug in self.lista_jugadores:
            if(jug.monto < self.valor_partida*2):
                print("El jugador ",jug.nombre_jugador," no tiene suficiente dinero para jugar al menos una ronda")
                self.lista_jugadores.remove(jug)
            else:
                jug.restarPlante(self.valor_partida)
                print("jugador ",jug.nombre_jugador," monto actual descontando primera apuesta: ",jug.monto)

