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
                self.__listarPaisesDeContinente()
            elif opcion == 2:
                self.__listarProvinciasDePais()
            elif opcion == 3:
                self.__listarLimitrofesDePais()
            elif opcion == 4:
                self.__listarPaisesOrdenadosPorSuperficie()
            elif opcion == 5:
                self.__compararDosPaises()
            elif opcion == 6:
                print("\n¡Hasta luego!")
            else:
                print("\nOpción inválida. Intente nuevamente.")

    # --- Menú ---

    def __mostrarMenu(self):
        print("\n" + "=" * 55)
        print("        MAPA DEL MUNDO - MENÚ PRINCIPAL")
        print("=" * 55)
        print("1. Listar países de un continente")
        print("2. Listar provincias de un país")
        print("3. Listar países limítrofes de un país")
        print("4. Listar todos los países ordenados por superficie")
        print("5. Comparar superficie de 2 países")
        print("6. Salir")
        print("-" * 55)

    # --- Opción 1: Listar países de un continente ---

    def __listarPaisesDeContinente(self):
        nombre = input("\nIngrese el nombre del continente: ")
        continente = self.__buscarContinente(nombre)
        if continente == None:
            print("No se encontró el continente '" + nombre + "'.")
            return
        paises = continente.getPaises()
        print("\n--- Países de " + continente.getNombre()
              + " (" + str(len(paises)) + ") ---")
        for i in range(len(paises)):
            pais = paises[i]
            print(str(i + 1) + ". " + pais.getNombre()
                  + " - Capital: " + pais.getCapital()
                  + " - Superficie: " + str(pais.getSuperficie()) + " km2")

    # --- Opción 2: Listar provincias de un país ---

    def __listarProvinciasDePais(self):
        nombre = input("\nIngrese el nombre del país: ")
        pais = self.__buscarPais(nombre)
        if pais == None:
            print("No se encontró el país '" + nombre + "'.")
            return
        provincias = pais.getProvincias()
        print("\n--- Provincias de " + pais.getNombre()
              + " (" + str(len(provincias)) + ") ---")
        if len(provincias) == 0:
            print("Este país no tiene provincias registradas.")
        else:
            for i in range(len(provincias)):
                print(str(i + 1) + ". " + provincias[i].toString())

    # --- Opción 3: Listar limítrofes de un país ---

    def __listarLimitrofesDePais(self):
        nombre = input("\nIngrese el nombre del país: ")
        pais = self.__buscarPais(nombre)
        if pais == None:
            print("No se encontró el país '" + nombre + "'.")
            return
        limitrofes = pais.getLimitrofes()
        print("\n--- Países limítrofes de " + pais.getNombre()
              + " (" + str(len(limitrofes)) + ") ---")
        if len(limitrofes) == 0:
            print("Este país no tiene limítrofes terrestres registrados.")
        else:
            for i in range(len(limitrofes)):
                print(str(i + 1) + ". " + limitrofes[i].getNombre())

    # --- Opción 4: Listar países ordenados por superficie ---

    def __listarPaisesOrdenadosPorSuperficie(self):
        todosLosPaises = self.__obtenerTodosLosPaises()

        # Ordenamiento burbuja de mayor a menor por superficie
        for i in range(len(todosLosPaises)):
            for j in range(0, len(todosLosPaises) - i - 1):
                if todosLosPaises[j].getSuperficie() < todosLosPaises[j + 1].getSuperficie():
                    aux = todosLosPaises[j]
                    todosLosPaises[j] = todosLosPaises[j + 1]
                    todosLosPaises[j + 1] = aux

        print("\n--- Países ordenados por superficie (mayor a menor) ---")
        for i in range(len(todosLosPaises)):
            pais = todosLosPaises[i]
            print(str(i + 1) + ". " + pais.getNombre()
                  + " (" + pais.getContinente().getNombre() + ")"
                  + " - " + str(pais.getSuperficie()) + " km2")

    # --- Opción 5: Comparar 2 países ---

    def __compararDosPaises(self):
        nombre1 = input("\nIngrese el nombre del primer país: ")
        pais1 = self.__buscarPais(nombre1)
        if pais1 == None:
            print("No se encontró el país '" + nombre1 + "'.")
            return

        nombre2 = input("Ingrese el nombre del segundo país: ")
        pais2 = self.__buscarPais(nombre2)
        if pais2 == None:
            print("No se encontró el país '" + nombre2 + "'.")
            return

        print("\n--- Comparación de superficie ---")
        print(pais1.getNombre() + ": " + str(pais1.getSuperficie()) + " km2")
        print(pais2.getNombre() + ": " + str(pais2.getSuperficie()) + " km2")
        print("")

        if pais1.getSuperficie() > pais2.getSuperficie():
            print(pais1.getNombre() + " tiene mayor superficie que "
                  + pais2.getNombre() + ".")
        elif pais2.getSuperficie() > pais1.getSuperficie():
            print(pais2.getNombre() + " tiene mayor superficie que "
                  + pais1.getNombre() + ".")
        else:
            print("Ambos países tienen la misma superficie.")

    # --- Métodos auxiliares ---

    def __buscarContinente(self, nombre):
        """Busca un continente por nombre (insensible a mayúsculas/minúsculas).
        Retorna el continente o None si no se encuentra."""
        for i in range(len(self.__continentes)):
            if self.__continentes[i].getNombre().lower() == nombre.lower():
                return self.__continentes[i]
        return None

    def __buscarPais(self, nombre):
        """Busca un país por nombre en todos los continentes
        (insensible a mayúsculas/minúsculas).
        Retorna el país o None si no se encuentra."""
        for i in range(len(self.__continentes)):
            paises = self.__continentes[i].getPaises()
            for j in range(len(paises)):
                if paises[j].getNombre().lower() == nombre.lower():
                    return paises[j]
        return None

    def __obtenerTodosLosPaises(self):
        """Retorna una nueva lista con todos los países de todos los continentes."""
        todos = []
        for i in range(len(self.__continentes)):
            paises = self.__continentes[i].getPaises()
            for j in range(len(paises)):
                todos.append(paises[j])
        return todos

    def __leerEntero(self, mensaje):
        """Lee un entero desde teclado. Retorna -1 si la entrada no es válida."""
        entrada = input(mensaje)
        if entrada.isdigit():
            return int(entrada)
        return -1


# --- Punto de entrada ---
main = Main()
main.ejecutar()
