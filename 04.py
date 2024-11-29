import datetime as dt

# Definir la constante archive globalmente
archive = "registro_notas.txt"

def registrar_datos():
    name = input("Ingrese su nombre: ")
    course = input("Ingrese su curso: ")
    score1 = float(input("Ingrese la primera nota: "))
    score2 = float(input("Ingrese la segunda nota: "))

    average = (score1 + score2) / 2
    condition = "Aprobado" if average >= 11 else "Desaprobado"
    actual_date = dt.date.today()

    print("\n-Registro-")
    print(f"Fecha: {actual_date}")
    print(f"Nombre: {name}")
    print(f"Condición: {condition}")

    # Escribir los datos en el archivo
    with open(archive, "a") as file:
        file.write(f"Fecha: {actual_date}\n")
        file.write(f"Nombre: {name}\n")
        file.write(f"Curso: {course}\n")
        file.write(f"Promedio: {average:.2f}\n")
        file.write(f"Condición: {condition}\n")
        file.write("-" * 30 + "\n")  # Separador entre registros

    print(f"\nLos datos se han guardado en el archivo '{archive}'.")

    # Leer y mostrar los últimos 5 registros
    with open(archive, "r") as file:
        lines = file.readlines()
        for line in lines[-5:]:
            print(line.rstrip())


# Función para mostrar todos los registros del archivo
def mostrar_todo():
    try:
        with open(archive, "r") as file:
            contenido = file.read()
            print("\n--- Contenido del archivo ---")
            print(contenido if contenido else "El archivo está vacío.")
    except FileNotFoundError:
        print("\nEl archivo no existe. Registre datos primero.")


# Función para mostrar los últimos registros
def mostrar_ultimos_registros():
    try:
        with open(archive, "r") as file:
            lines = file.readlines()
            registros = [line for line in lines if line.strip() != "-" * 30]
            if registros:
                print("\n--- Últimos registros ---")
                for line in registros[-6:]:
                    print(line, end="")
            else:
                print("El archivo no contiene registros.")
    except FileNotFoundError:
        print("\nEl archivo no existe. Registre datos primero.")


# Función para el menú de opciones
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar datos")
        print("2. Mostrar todos los registros")
        print("3. Mostrar los últimos registros")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_datos()
        elif opcion == "2":
            mostrar_todo()
        elif opcion == "3":
            mostrar_ultimos_registros()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


# Llamada al menú
menu()
