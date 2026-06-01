class Provincia:
    """Clase que representa una provincia."""

    def __init__(self, nombre):
        self.__nombre = nombre

    # --- Getters ---

    def getNombre(self):
        return self.__nombre

    # --- Setters ---

    def setNombre(self, nombre):
        self.__nombre = nombre

    # --- toString ---

    def toString(self):
        return self.__nombre
