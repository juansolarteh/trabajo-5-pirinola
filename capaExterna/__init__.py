#Clase que itera un menu de opciones que son otorgadas
#en el constructor del objeto menu. Tambien procesa la eleccion
#de la opcion del menu valida la eleccion y tiene un metodo publico
#que retorna la opcion(int) elegida por el usuario


class Menu():
    def __init__(self, titulo, listaOpciones, mensajePedirOpcion):

        self.__validarStr(titulo)
        self.__validarOpciones(listaOpciones)
        self.__validarStr(mensajePedirOpcion)

        self.__opcion = 0
        self.__opcionValida = False
        self.__titulo = titulo
        self.__listaOpciones = listaOpciones
        self.__mensajePedirOpcion = mensajePedirOpcion
        self.__numeroOpciones = len(self.__listaOpciones)

        while (self.__opcionValida == False):
            self.__escribirTitulo(self.__titulo)
            self.__escribirOpciones(self.__listaOpciones)
            self.__pedirOpcion()
            self.__opcionValida = self.__validarOpcion()
            if (self.__opcionValida == True):
                if (int(self.__opcion) < 1 or int(self.__opcion) > self.__numeroOpciones):
                    self.__opcionValida = False
                    print()
                    print('Debe ingresar un numero del 1 al ', self.__numeroOpciones)
            else:
                print()
                print('Solo se permite ingresar numeros')

    def __validarStr(self, titulo):
        if not type(titulo) is str:
            raise TypeError('El parametro titulo solo permite un dato de tipo cadena')

    def __escribirTitulo(self, titulo):
        print()
        print('----------', titulo, '----------')
        print()

    def __validarOpciones(self, listaOpciones):
        for i in listaOpciones:
            if not type(i) is str:
                raise TypeError('El parametro listaOpciones solo permite ' \
                                'un dato de tipo coleccion o almacen de datos ' \
                                'que contenga cadenas')

    def __escribirOpciones(self, listaOpciones):
        contador = 0
        for i in listaOpciones:
            contador += 1
            print(contador, '. ', i)
        print()

    def __pedirOpcion(self):
        self.__opcion = input(self.__mensajePedirOpcion)

    def __validarOpcion(self):
        try:
            int(self.__opcion)
            return True
        except:
            return False

    def darOpcion(self):
        return int(self.__opcion)

    def regresarMenu(self):
        self.__opcionValida = False
        while (self.__opcionValida == False):
            self.__escribirTitulo(self.__titulo)
            self.__escribirOpciones(self.__listaOpciones)
            self.__pedirOpcion()
            self.__opcionValida = self.__validarOpcion()
            if (self.__opcionValida == True):
                if (int(self.__opcion) < 1 or int(self.__opcion) > self.__numeroOpciones):
                    self.__opcionValida = False
                    print()
                    print('Debe ingresar un numero del 1 al ', self.__numeroOpciones)
            else:
                print()
                print('Solo se permite ingresar numeros')

