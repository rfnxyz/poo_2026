class Continente:
    """Clase que representa un continente con una colección de países."""

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__paises = []

    # --- Getters ---

    def getNombre(self):
        return self.__nombre

    def getPaises(self):
        return self.__paises

    def getCantidadPaises(self):
        return len(self.__paises)

    # --- Setters ---

    def setNombre(self, nombre):
        self.__nombre = nombre

    # --- Métodos de vinculación ---

    def agregarPais(self, pais):
        """Agrega un país al continente y establece la relación bidireccional."""
        self.__paises.append(pais)
        pais.setContinente(self)

    # --- toString ---

    def toString(self):
        nombresPaises = ""
        for i in range(len(self.__paises)):
            nombresPaises += self.__paises[i].getNombre()
            if i < len(self.__paises) - 1:
                nombresPaises += ", "

        texto = "Continente: " + self.__nombre + "\n"
        texto += "  Países (" + str(len(self.__paises)) + "): " + nombresPaises
        return texto
