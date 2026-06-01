class Pais:
    """Clase que representa un país con capital, superficie, provincias y limítrofes."""

    def __init__(self, nombre, capital, superficie):
        self.__nombre = nombre
        self.__capital = capital
        self.__superficie = superficie
        self.__continente = None
        self.__provincias = []
        self.__limitrofes = []

    # --- Getters ---

    def getNombre(self):
        return self.__nombre

    def getCapital(self):
        return self.__capital

    def getSuperficie(self):
        return self.__superficie

    def getContinente(self):
        return self.__continente

    def getProvincias(self):
        return self.__provincias

    def getLimitrofes(self):
        return self.__limitrofes

    def getCantidadProvincias(self):
        return len(self.__provincias)

    def getCantidadLimitrofes(self):
        return len(self.__limitrofes)

    # --- Setters ---

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setCapital(self, capital):
        self.__capital = capital

    def setSuperficie(self, superficie):
        self.__superficie = superficie

    def setContinente(self, continente):
        self.__continente = continente

    # --- Métodos de vinculación ---

    def agregarProvincia(self, provincia):
        """Agrega una provincia al país."""
        self.__provincias.append(provincia)

    def agregarLimitrofe(self, pais):
        """Agrega un país limítrofe."""
        self.__limitrofes.append(pais)

    # --- toString ---

    def toString(self):
        nombreContinente = "Sin continente"
        if self.__continente != None:
            nombreContinente = self.__continente.getNombre()

        nombresProvincias = ""
        for i in range(len(self.__provincias)):
            nombresProvincias += self.__provincias[i].toString()
            if i < len(self.__provincias) - 1:
                nombresProvincias += ", "

        nombresLimitrofes = ""
        for i in range(len(self.__limitrofes)):
            nombresLimitrofes += self.__limitrofes[i].getNombre()
            if i < len(self.__limitrofes) - 1:
                nombresLimitrofes += ", "

        texto = "País: " + self.__nombre + "\n"
        texto += "  Capital: " + self.__capital + "\n"
        texto += "  Superficie: " + str(self.__superficie) + " km2\n"
        texto += "  Continente: " + nombreContinente + "\n"
        texto += "  Provincias (" + str(len(self.__provincias)) + "): " + nombresProvincias + "\n"
        texto += "  Limítrofes (" + str(len(self.__limitrofes)) + "): " + nombresLimitrofes
        return texto
