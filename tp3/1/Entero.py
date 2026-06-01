class Entero:
    """Clase que representa un número entero con encapsulamiento."""

    def __init__(self, valor):
        self.__valor = valor

    # --- Getters y Setters ---

    def getValor(self):
        return self.__valor

    def setValor(self, valor):
        self.__valor = valor

    # --- Métodos de negocio ---

    def esPar(self):
        """Retorna True si el número es par."""
        return self.__valor % 2 == 0

    def esImpar(self):
        """Retorna True si el número es impar."""
        return self.__valor % 2 != 0

    def factorial(self):
        """Retorna el factorial del número. Si es negativo retorna -1."""
        if self.__valor < 0:
            return -1
        resultado = 1
        for i in range(1, self.__valor + 1):
            resultado *= i
        return resultado

    def esPrimo(self):
        """Retorna True si el número es primo."""
        if self.__valor <= 1:
            return False
        for i in range(2, self.__valor):
            if self.__valor % i == 0:
                return False
        return True
