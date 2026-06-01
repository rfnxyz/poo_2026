from Seeder import Seeder


class Main:
    """Clase principal que maneja toda la interacción con el usuario."""

    def __init__(self):
        self.__seeder = Seeder()
        self.__seeder.inicializarDatos()
        self.__continentes = self.__seeder.getContinentes()

    def ejecutar(self):
        """Bucle principal del menú."""
        opcion = 0
        while opcion != 6:
            self.__mostrarMenu()
            opcion = self.__leerEntero("Seleccione una opción: ")
            if opcion == 1:
                self.__listarContinentes()
            elif opcion == 2:
                self.__listarPaisesDeContinente()
            elif opcion == 3:
                self.__mostrarDetallePais()
            elif opcion == 4:
                self.__listarLimitrofesDePais()
            elif opcion == 5:
                self.__listarProvinciasDePais()
            elif opcion == 6:
                print("\n¡Hasta luego!")
            else:
                print("\nOpción inválida. Intente nuevamente.")

    # --- Menú ---

    def __mostrarMenu(self):
        print("\n" + "=" * 50)
        print("       MAPA DEL MUNDO - MENÚ PRINCIPAL")
        print("=" * 50)
        print("1. Listar continentes")
        print("2. Listar países de un continente")
        print("3. Mostrar detalle de un país")
        print("4. Listar países limítrofes de un país")
        print("5. Listar provincias de un país")
        print("6. Salir")
        print("-" * 50)

    # --- Opciones ---

    def __listarContinentes(self):
        print("\n--- Continentes ---")
        for i in range(len(self.__continentes)):
            continente = self.__continentes[i]
            print(str(i + 1) + ". " + continente.getNombre()
                  + " (" + str(continente.getCantidadPaises()) + " países)")

    def __listarPaisesDeContinente(self):
        self.__listarContinentes()
        indice = self.__leerEntero("\nIngrese el número del continente: ")
        if indice < 1 or indice > len(self.__continentes):
            print("Número de continente inválido.")
            return
        continente = self.__continentes[indice - 1]
        paises = continente.getPaises()
        print("\n--- Países de " + continente.getNombre() + " ---")
        for i in range(len(paises)):
            print(str(i + 1) + ". " + paises[i].getNombre()
                  + " (Capital: " + paises[i].getCapital() + ")")

    def __mostrarDetallePais(self):
        pais = self.__seleccionarPais()
        if pais == None:
            return
        print("\n--- Detalle del País ---")
        print(pais.toString())

    def __listarLimitrofesDePais(self):
        pais = self.__seleccionarPais()
        if pais == None:
            return
        limitrofes = pais.getLimitrofes()
        print("\n--- Países limítrofes de " + pais.getNombre() + " ---")
        if len(limitrofes) == 0:
            print("Este país no tiene limítrofes terrestres registrados.")
        else:
            for i in range(len(limitrofes)):
                print(str(i + 1) + ". " + limitrofes[i].getNombre())

    def __listarProvinciasDePais(self):
        pais = self.__seleccionarPais()
        if pais == None:
            return
        provincias = pais.getProvincias()
        print("\n--- Provincias de " + pais.getNombre() + " ---")
        if len(provincias) == 0:
            print("Este país no tiene provincias registradas.")
        else:
            for i in range(len(provincias)):
                print(str(i + 1) + ". " + provincias[i].toString())

    # --- Métodos auxiliares ---

    def __seleccionarPais(self):
        """Permite al usuario seleccionar un continente y luego un país.
        Retorna el país seleccionado o None si la selección es inválida."""
        self.__listarContinentes()
        indiceCont = self.__leerEntero("\nIngrese el número del continente: ")
        if indiceCont < 1 or indiceCont > len(self.__continentes):
            print("Número de continente inválido.")
            return None
        continente = self.__continentes[indiceCont - 1]
        paises = continente.getPaises()
        print("\n--- Países de " + continente.getNombre() + " ---")
        for i in range(len(paises)):
            print(str(i + 1) + ". " + paises[i].getNombre())
        indicePais = self.__leerEntero("\nIngrese el número del país: ")
        if indicePais < 1 or indicePais > len(paises):
            print("Número de país inválido.")
            return None
        return paises[indicePais - 1]

    def __leerEntero(self, mensaje):
        """Lee un entero desde teclado. Retorna -1 si la entrada no es válida."""
        entrada = input(mensaje)
        if entrada.isdigit():
            return int(entrada)
        return -1


# --- Punto de entrada ---
main = Main()
main.ejecutar()
