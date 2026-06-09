from Empleado import Empleado


class Empresa:
    """Clase gestora que administra una lista de empleados."""

    def __init__(self):
        self.__empleados = []

    # --- Métodos de gestión ---

    def registrarEmpleado(self, empleado):
        """Registra un empleado si su DNI no está repetido.
        Retorna True si se registró, False si el DNI ya existe."""
        if self.__existeDni(empleado.getDni()):
            return False
        self.__empleados.append(empleado)
        return True

    def obtenerEmpleadoQueMasGana(self):
        """Retorna el objeto Empleado con mayor sueldo, o None si no hay empleados."""
        if len(self.__empleados) == 0:
            return None
        mayor = self.__empleados[0]
        for i in range(1, len(self.__empleados)):
            if self.__empleados[i].getSueldo() > mayor.getSueldo():
                mayor = self.__empleados[i]
        return mayor

    def obtenerSueldoPromedio(self):
        """Retorna el sueldo promedio como float, o 0.0 si no hay empleados."""
        if len(self.__empleados) == 0:
            return 0.0
        suma = 0
        for empleado in self.__empleados:
            suma += empleado.getSueldo()
        return suma / len(self.__empleados)

    def obtenerCantidadEmpleados(self):
        """Retorna la cantidad de empleados registrados."""
        return len(self.__empleados)

    def getEmpleados(self):
        """Retorna la lista de empleados."""
        return self.__empleados

    # --- Método privado ---

    def __existeDni(self, dni):
        """Retorna True si ya existe un empleado con ese DNI."""
        for empleado in self.__empleados:
            if empleado.getDni() == dni:
                return True
        return False
