from Empleado import Empleado
from Empresa import Empresa


class Main:
    """Clase principal que gestiona toda la interacción con el usuario."""

    def __init__(self):
        self.__empresa = Empresa()

    def ejecutar(self):
        opcion = 0
        while opcion != 4:
            print()
            print("========================================")
            print("   SISTEMA DE GESTIÓN DE EMPLEADOS")
            print("========================================")
            print("1. Registrar empleado")
            print("2. Mostrar empleado que más gana")
            print("3. Mostrar sueldo promedio")
            print("4. Salir")
            print("----------------------------------------")
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                self.__registrarEmpleado()
            elif opcion == 2:
                self.__mostrarEmpleadoQueMasGana()
            elif opcion == 3:
                self.__mostrarSueldoPromedio()
            elif opcion == 4:
                print()
                print("¡Hasta luego!")
            else:
                print("Opción no válida. Intente de nuevo.")

    def __registrarEmpleado(self):
        print()
        print("--- Registrar nuevo empleado ---")
        nombre = input("Nombre: ")
        dni = input("DNI: ")
        sueldo = float(input("Sueldo: "))

        empleado = Empleado(nombre, dni, sueldo)

        if empleado.fueAjustadoAlMinimo(sueldo):
            print("El sueldo ingresado es menor al mínimo ($" + str(Empleado.SALARIO_MINIMO) + ").")
            print("Se asignó automáticamente el Salario Mínimo Vital y Móvil.")

        if self.__empresa.registrarEmpleado(empleado):
            print("Empleado '" + empleado.getNombre() + "' registrado exitosamente.")
        else:
            print("Error: Ya existe un empleado con DNI " + dni + ".")

    def __mostrarEmpleadoQueMasGana(self):
        print()
        empleado = self.__empresa.obtenerEmpleadoQueMasGana()
        if empleado == None:
            print("No hay empleados registrados.")
        else:
            print("--- Empleado que más gana ---")
            print("Nombre: " + empleado.getNombre())
            print("DNI:    " + empleado.getDni())
            print("Sueldo: $" + str(empleado.getSueldo()))

    def __mostrarSueldoPromedio(self):
        print()
        if self.__empresa.obtenerCantidadEmpleados() == 0:
            print("No hay empleados registrados.")
        else:
            promedio = self.__empresa.obtenerSueldoPromedio()
            print("--- Sueldo promedio ---")
            print("Cantidad de empleados: " + str(self.__empresa.obtenerCantidadEmpleados()))
            print("Sueldo promedio: $" + str(round(promedio, 2)))


# --- Punto de entrada ---
main = Main()
main.ejecutar()
