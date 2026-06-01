from Entero import Entero


class Main:
    """Clase principal que gestiona toda la interacción con el usuario."""

    def ejecutar(self):
        print("=== Prueba de la clase Entero ===")
        print()

        valor = int(input("Ingrese un número entero: "))
        entero = Entero(valor)

        print()
        print("Número ingresado: " + str(entero.getValor()))
        print()

        # --- esPar / esImpar ---
        if entero.esPar():
            print("¿Es par? Sí")
        else:
            print("¿Es par? No")

        if entero.esImpar():
            print("¿Es impar? Sí")
        else:
            print("¿Es impar? No")

        # --- factorial ---
        resultado = entero.factorial()
        if resultado == -1:
            print("El factorial no está definido para números negativos.")
        else:
            print("Factorial de " + str(entero.getValor()) + " = " + str(resultado))

        # --- esPrimo ---
        if entero.esPrimo():
            print("¿Es primo? Sí")
        else:
            print("¿Es primo? No")


# --- Punto de entrada ---
main = Main()
main.ejecutar()
