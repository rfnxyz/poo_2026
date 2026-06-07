class Cancha:
    """Clase que representa una cancha de fútbol con sus turnos reservados."""

    HORA_APERTURA = 14
    HORA_CIERRE = 23

    def __init__(self, numero):
        self.__numero = numero
        self.__turnos = []

    # --- Getters ---

    def getNumero(self):
        return self.__numero

    def getTurnos(self):
        return self.__turnos

    def getCantidadTurnos(self):
        return len(self.__turnos)

    # --- Setters ---

    def setNumero(self, numero):
        self.__numero = numero

    # --- Métodos de negocio ---

    def reservarTurno(self, turno):
        """Intenta reservar un turno. Retorna True si fue exitoso,
        False si ya existe una reserva para la misma fecha y hora."""
        for i in range(len(self.__turnos)):
            if self.__turnos[i].mismaFechaYHora(
                    turno.getDia(), turno.getMes(),
                    turno.getAnio(), turno.getHora()):
                return False
        self.__turnos.append(turno)
        return True

    def cancelarTurno(self, dia, mes, anio, hora):
        """Cancela un turno por fecha y hora. Retorna True si se encontró
        y eliminó, False si no existe turno en esa fecha y hora."""
        for i in range(len(self.__turnos)):
            if self.__turnos[i].mismaFechaYHora(dia, mes, anio, hora):
                self.__turnos.pop(i)
                return True
        return False

    def obtenerTurno(self, dia, mes, anio, hora):
        """Retorna el turno en la fecha y hora indicadas, o None si está libre."""
        for i in range(len(self.__turnos)):
            if self.__turnos[i].mismaFechaYHora(dia, mes, anio, hora):
                return self.__turnos[i]
        return None

    def obtenerTurnosPorFecha(self, dia, mes, anio):
        """Retorna una lista con los turnos de una fecha específica."""
        turnosFecha = []
        for i in range(len(self.__turnos)):
            turno = self.__turnos[i]
            if (turno.getDia() == dia and turno.getMes() == mes
                    and turno.getAnio() == anio):
                turnosFecha.append(turno)
        return turnosFecha

    def contarTurnosPorFecha(self, dia, mes, anio):
        """Retorna la cantidad de turnos ocupados en una fecha."""
        return len(self.obtenerTurnosPorFecha(dia, mes, anio))

    # --- toString ---

    def toString(self):
        texto = "Cancha " + str(self.__numero)
        texto += " (" + str(len(self.__turnos)) + " turnos reservados)"
        return texto
