from Cancha import Cancha
from Turno import Turno


class Main:
    """Clase principal que gestiona toda la interacción con el usuario."""

    def __init__(self):
        self.__canchas = []
        for i in range(1, 4):
            self.__canchas.append(Cancha(i))

    def ejecutar(self):
        """Bucle principal del menú."""
        opcion = 0
        while opcion != 4:
            self.__mostrarMenu()
            opcion = self.__leerEntero("Seleccione una opción: ")
            if opcion == 1:
                self.__verEstadoCanchas()
            elif opcion == 2:
                self.__registrarReserva()
            elif opcion == 3:
                self.__cancelarReserva()
            elif opcion == 4:
                print("\n¡Hasta luego!")
            else:
                print("\nOpción inválida. Intente nuevamente.")

    # --- Menú ---

    def __mostrarMenu(self):
        print("\n" + "=" * 60)
        print("      COMPLEJO DEPORTIVO - GESTIÓN DE RESERVAS")
        print("=" * 60)
        print("1. Ver estado actual de las canchas (por fecha)")
        print("2. Registrar una nueva reserva")
        print("3. Cancelar una reserva existente")
        print("4. Salir")
        print("-" * 60)

    # --- Opción 1: Ver estado de las canchas por fecha ---

    def __verEstadoCanchas(self):
        print("\n--- Ver Estado de las Canchas ---")
        fecha = self.__leerFecha()
        if fecha == None:
            return

        dia = fecha[0]
        mes = fecha[1]
        anio = fecha[2]

        fechaTexto = self.__formatearFecha(dia, mes, anio)

        print("\n" + "=" * 60)
        print("     ESTADO DE LAS CANCHAS - " + fechaTexto)
        print("=" * 60)

        # Encabezado
        print("\n{:<12} {:<16} {:<16} {:<16}".format(
            "Hora", "Cancha 1", "Cancha 2", "Cancha 3"))
        print("-" * 60)

        # Recorrer cada hora del horario de atención
        hora = Cancha.HORA_APERTURA
        while hora <= Cancha.HORA_CIERRE:
            linea = str(hora) + ":00 hs"
            while len(linea) < 12:
                linea += " "

            for i in range(len(self.__canchas)):
                turno = self.__canchas[i].obtenerTurno(dia, mes, anio, hora)
                if turno != None:
                    celda = turno.getNombrePersona()
                else:
                    celda = "LIBRE"
                while len(celda) < 16:
                    celda += " "
                linea += celda

            print(linea)
            hora = hora + 1

        print("-" * 60)

        # Resumen
        totalHoras = Cancha.HORA_CIERRE - Cancha.HORA_APERTURA + 1
        for i in range(len(self.__canchas)):
            cancha = self.__canchas[i]
            ocupados = cancha.contarTurnosPorFecha(dia, mes, anio)
            libres = totalHoras - ocupados
            print("Cancha " + str(cancha.getNumero()) + ": "
                  + str(ocupados) + " ocupados, "
                  + str(libres) + " libres")

    # --- Opción 2: Registrar reserva ---

    def __registrarReserva(self):
        print("\n--- Registrar Nueva Reserva ---")

        # Seleccionar cancha
        numCancha = self.__leerEntero("Número de cancha (1-3): ")
        if numCancha < 1 or numCancha > 3:
            print("Número de cancha inválido.")
            return

        # Ingresar fecha
        fecha = self.__leerFecha()
        if fecha == None:
            return
        dia = fecha[0]
        mes = fecha[1]
        anio = fecha[2]

        # Ingresar hora
        hora = self.__leerEntero("Hora del turno ("
                                 + str(Cancha.HORA_APERTURA) + " a "
                                 + str(Cancha.HORA_CIERRE) + "): ")
        if hora < Cancha.HORA_APERTURA or hora > Cancha.HORA_CIERRE:
            print("Hora fuera del horario de atención ("
                  + str(Cancha.HORA_APERTURA) + ":00 a "
                  + str(Cancha.HORA_CIERRE) + ":00).")
            return

        # Ingresar nombre
        nombre = input("Nombre de la persona: ")
        if nombre == "":
            print("El nombre no puede estar vacío.")
            return

        # Intentar reservar
        turno = Turno(nombre, hora, dia, mes, anio)
        cancha = self.__canchas[numCancha - 1]
        resultado = cancha.reservarTurno(turno)

        fechaTexto = self.__formatearFecha(dia, mes, anio)
        if resultado:
            print("Reserva exitosa: Cancha " + str(numCancha)
                  + " el " + fechaTexto
                  + " a las " + str(hora) + ":00 hs para " + nombre + ".")
        else:
            print("Error: Turno ocupado. La cancha " + str(numCancha)
                  + " ya tiene una reserva el " + fechaTexto
                  + " a las " + str(hora) + ":00 hs.")

    # --- Opción 3: Cancelar reserva ---

    def __cancelarReserva(self):
        print("\n--- Cancelar Reserva ---")

        # Seleccionar cancha
        numCancha = self.__leerEntero("Número de cancha (1-3): ")
        if numCancha < 1 or numCancha > 3:
            print("Número de cancha inválido.")
            return

        # Ingresar fecha
        fecha = self.__leerFecha()
        if fecha == None:
            return
        dia = fecha[0]
        mes = fecha[1]
        anio = fecha[2]

        # Ingresar hora
        hora = self.__leerEntero("Hora del turno a cancelar ("
                                 + str(Cancha.HORA_APERTURA) + " a "
                                 + str(Cancha.HORA_CIERRE) + "): ")
        if hora < Cancha.HORA_APERTURA or hora > Cancha.HORA_CIERRE:
            print("Hora fuera del horario de atención.")
            return

        # Intentar cancelar
        cancha = self.__canchas[numCancha - 1]
        resultado = cancha.cancelarTurno(dia, mes, anio, hora)

        fechaTexto = self.__formatearFecha(dia, mes, anio)
        if resultado:
            print("Reserva cancelada exitosamente: Cancha " + str(numCancha)
                  + " el " + fechaTexto
                  + " a las " + str(hora) + ":00 hs.")
        else:
            print("Error: No existe reserva en la cancha " + str(numCancha)
                  + " el " + fechaTexto
                  + " a las " + str(hora) + ":00 hs.")

    # --- Métodos auxiliares ---

    def __leerFecha(self):
        """Lee día, mes y año por separado. Retorna una lista [dia, mes, anio]
        o None si algún dato es inválido."""
        dia = self.__leerEntero("Día (1-31): ")
        if dia < 1 or dia > 31:
            print("Día inválido.")
            return None

        mes = self.__leerEntero("Mes (1-12): ")
        if mes < 1 or mes > 12:
            print("Mes inválido.")
            return None

        anio = self.__leerEntero("Año (ej: 2026): ")
        if anio < 1:
            print("Año inválido.")
            return None

        return [dia, mes, anio]

    def __formatearFecha(self, dia, mes, anio):
        """Formatea una fecha como dd/mm/aaaa."""
        diaTexto = str(dia)
        if dia < 10:
            diaTexto = "0" + diaTexto
        mesTexto = str(mes)
        if mes < 10:
            mesTexto = "0" + mesTexto
        return diaTexto + "/" + mesTexto + "/" + str(anio)

    def __leerEntero(self, mensaje):
        """Lee un entero desde teclado. Retorna -1 si la entrada no es válida."""
        entrada = input(mensaje)
        if entrada.isdigit():
            return int(entrada)
        return -1


# --- Punto de entrada ---
main = Main()
main.ejecutar()
