class Empleado:
    """Clase que representa un empleado con nombre, DNI y sueldo."""

    # Salario Mínimo Vital y Móvil (valor de referencia 2026)
    SALARIO_MINIMO = 450000

    def __init__(self, nombre, dni, sueldo):
        self.__nombre = nombre
        self.__dni = dni
        # Aplicar regla de negocio al construir
        if sueldo < Empleado.SALARIO_MINIMO:
            self.__sueldo = Empleado.SALARIO_MINIMO
        else:
            self.__sueldo = sueldo

    # --- Getters ---

    def getNombre(self):
        return self.__nombre

    def getDni(self):
        return self.__dni

    def getSueldo(self):
        return self.__sueldo

    # --- Setters ---

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setDni(self, dni):
        self.__dni = dni

    def setSueldo(self, sueldo):
        """Asigna el sueldo. Si es negativo o menor al mínimo, asigna el SMVM."""
        if sueldo < Empleado.SALARIO_MINIMO:
            self.__sueldo = Empleado.SALARIO_MINIMO
        else:
            self.__sueldo = sueldo

    # --- Métodos auxiliares ---

    def fueAjustadoAlMinimo(self, sueldoOriginal):
        """Retorna True si el sueldo original era menor al mínimo."""
        return sueldoOriginal < Empleado.SALARIO_MINIMO
