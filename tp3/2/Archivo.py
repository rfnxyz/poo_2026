class Archivo:
    """Clase que gestiona la persistencia de empleados en un archivo de texto.
    No contiene interacción con el usuario (sin print ni input)."""

    def __init__(self, nombreArchivo):
        self.__nombreArchivo = nombreArchivo

    def getNombreArchivo(self):
        return self.__nombreArchivo

    def guardarEmpleados(self, empleados):
        """Guarda la lista de empleados en el archivo de texto.
        Cada línea tiene el formato: nombre;dni;sueldo
        Retorna True si se pudo guardar, False en caso contrario."""
        archivo = open(self.__nombreArchivo, "w")
        for i in range(len(empleados)):
            empleado = empleados[i]
            linea = (empleado.getNombre() + ";"
                     + empleado.getDni() + ";"
                     + str(empleado.getSueldo()))
            archivo.write(linea + "\n")
        archivo.close()
        return True

    def cargarLineas(self):
        """Lee el archivo y retorna una lista de listas [nombre, dni, sueldo].
        Retorna una lista vacía si el archivo no existe o está vacío."""
        datos = []
        # Verificar si el archivo existe intentando abrirlo en modo lectura
        existe = self.__existeArchivo()
        if not existe:
            return datos

        archivo = open(self.__nombreArchivo, "r")
        contenido = archivo.read()
        archivo.close()

        if contenido == "":
            return datos

        lineas = contenido.split("\n")
        for i in range(len(lineas)):
            linea = lineas[i]
            if linea != "":
                partes = linea.split(";")
                if len(partes) == 3:
                    nombre = partes[0]
                    dni = partes[1]
                    sueldo = float(partes[2])
                    datos.append([nombre, dni, sueldo])

        return datos

    def __existeArchivo(self):
        """Verifica si el archivo existe. Retorna True o False."""
        import os
        return os.path.exists(self.__nombreArchivo)
