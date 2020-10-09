class Jugador:
    def __init__(self,nombre, planteInicial):
        self.nombre_jugador = nombre
        self.monto = planteInicial


    def get_nombre(self):
        return self.nombre_jugador

    def restarPlante(self, cantidad):
        self.monto -= cantidad

    def sumarPlante(self, cantidad):
        self.monto += cantidad