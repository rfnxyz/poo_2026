class Turno:
    """Clase que representa un turno de reserva en una cancha."""

    def __init__(self, nombrePersona, hora, dia, mes, anio):
        self.__nombrePersona = nombrePersona
        self.__hora = hora
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio

    # --- Getters ---

    def getNombrePersona(self):
        return self.__nombrePersona

    def getHora(self):
        return self.__hora

    def getDia(self):
        return self.__dia

    def getMes(self):
        return self.__mes

    def getAnio(self):
        return self.__anio

    # --- Setters ---

    def setNombrePersona(self, nombrePersona):
        self.__nombrePersona = nombrePersona

    def setHora(self, hora):
        self.__hora = hora

    def setDia(self, dia):
        self.__dia = dia

    def setMes(self, mes):
        self.__mes = mes

    def setAnio(self, anio):
        self.__anio = anio

    # --- Métodos de negocio ---

    def mismaFechaYHora(self, dia, mes, anio, hora):
        """Retorna True si este turno coincide con la fecha y hora indicadas."""
        return (self.__dia == dia and self.__mes == mes
                and self.__anio == anio and self.__hora == hora)

    def getFechaTexto(self):
        """Retorna la fecha formateada como texto dd/mm/aaaa."""
        diaTexto = str(self.__dia)
        if self.__dia < 10:
            diaTexto = "0" + diaTexto
        mesTexto = str(self.__mes)
        if self.__mes < 10:
            mesTexto = "0" + mesTexto
        return diaTexto + "/" + mesTexto + "/" + str(self.__anio)

    # --- toString ---

    def toString(self):
        return (self.getFechaTexto() + " " + str(self.__hora)
                + ":00 hs - " + self.__nombrePersona)
