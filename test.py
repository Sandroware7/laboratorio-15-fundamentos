# class Perro:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def ladrar(self):
#         return f"{self.name} esta ladrando"

# mi_perro = Perro("peluso", 4)

# print(mi_perro.name)
# print(mi_perro.ladrar())

# class Coche:
#     def __init__(self, marca, modelo="Genérico"):
#         self.marca = marca or "generico"
#         self.modelo = modelo

#     def vistaRapida(self):
#         print(f"Marca: {self.marca}, Modelo: {self.modelo}")

# class DetallesCoche(Coche):
#     def __init__(self, marca, modelo, año):
#         super().__init__(marca, modelo)
#         self.año = año

#     def datos(self):
#         print(f"Se trata de un vehiculo marca {self.marca}, modelo {self.modelo}, año {self.año}")

# coche1 = DetallesCoche("Toyota", "Yaris", 2005)
# coche2 = DetallesCoche("Ford", "Fiesta", 1988)

# coche1.vistaRapida()
# coche2.vistaRapida()
# coche1.datos()
# coche2.datos()


class Usuario:
    def __init__(self, name,age, email):
        self.name = name
        self.age = age
        self.email = email

    def saludar(self):
        return f"Hola, mi nombre es {self.name}."





# name = "registro.txt"

# with open(name, "w") as log_file:
#     log_file.write("Nombre: Ellio\n")
#     log_file.write("Edad: 28\n")
#     log_file.write("Ciudad: Ayacucho\n")
# with open(name, "r") as log_file:
#     for line in log_file:
#         print(line.rstrip())


# name = "user_data.txt"

# with open(name, "w") as file:
#     file.write("Name: Sandro.\n")
#     file.write("Age: 23.\n")
#     file.write("City: Lima.\n")


# with open(name, "a") as file:
#     file.write("Estado civil: Soltero.\n")
#     file.write("Nacionalidad: Peruano.\n")


# with open(name, "r") as file:
#     # for line in file:
#     #     print(line.rstrip())


#     # linea = file.readline()
#     # while linea:
#     #     print(linea, end="")
#     #     linea = file.readline()


#     lineas = file.readlines()
#     for linea in lineas:
#         print(linea, end="")


# name = "User_data.txt"

# with open(name, "a") as file:
#     while True:
#         lastname = input("Enter lastname: ")
#         score1 = input("Enter the score 1: ")
#         score2 = input("Enter the score 2: ")
#         score3 = input("Enter the score 3: ")
#         file.write(f"{lastname},{score1},{score2},{score3}\n")
#         continuar = input("Do you want to register someone else? (y/n): ")
#         if continuar.lower() != "y":
#             break

# print("\nDatos registrados:")
# with open(name, "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         # lastname, score1, score2, score3 = line.strip().split(", ")
#         print(f"Apellido: {lastname}, Nota 1: {score1}, Nota 2: {score2}, Nota 3: {score3}")


# 01
# name = "Data.txt"
# with open(name, "w") as file:
#     file.write("Nombre: Sandro")

# with open(name, "r") as file:
#     contenido=file.read()
#     print(contenido)


# 02
# import datetime as dt

# name = input("Ingrese su nombre: ")
# course = input("Ingrese su curso: ")
# score1 = float(input("Ingrese la primera nota: "))
# score2 = float(input("Ingrese la segunda nota: "))

# average = (score1 + score2) / 2

# condition = "Aprobado" if average >= 11 else "Desaprobado"

# actual_date = dt.date.today()

# print("\n--- Registro ---")
# print(f"Fecha: {actual_date}")
# print(f"Nombre: {name}")
# print(f"Condición: {condition}")

# archive = "registro_notas.txt"
# with open(archive, "a") as file:
#     file.write(f"Fecha: {actual_date}\n")
#     file.write(f"Nombre: {name}\n")
#     file.write(f"Curso: {course}\n")
#     file.write(f"Promedio: {average}\n")
#     file.write(f"Condición: {condition}\n")

# # print(f"\nLos datos se han guardado en el archivo '{archive}'.")

# with open(archive, "r") as file:
#     lineas = file.readlines()
#     for line in lineas:
#         print(line, end="")


# # 02
# import datetime as dt

# archive="student_data.txt"

# def registrar_datos():
#     name = input("Ingrese su nombre: ")
#     course = input("Ingrese su curso: ")
#     score1 = float(input("Ingrese la primera nota: "))
#     score2 = float(input("Ingrese la segunda nota: "))

#     average = (score1 + score2) / 2

#     condition = "Aprobado" if average >= 11 else "Desaprobado"

#     actual_date = dt.date.today()

#     print("\n-Registro-")
#     print(f"Fecha: {actual_date}")
#     print(f"Nombre: {name}")
#     print(f"Condición: {condition}")


#     with open(archive, "a") as file:
#         file.write(f"Fecha: {actual_date}\n")
#         file.write(f"Nombre: {name}\n")
#         file.write(f"Curso: {course}\n")
#         file.write(f"Promedio: {average}\n")
#         file.write(f"Condición: {condition}\n")

#     print(f"\nLos datos se han guardado en el archivo '{archive}'.")


# # 03
#     with open(archive, "r") as file:
#         lines = file.readlines()
#         for line in lines[-5:]:
#             print(line.rstrip())


# # 04
# def mostrar_todo():
#     try:
#         with open(archive, "r") as file:
#             contenido = file.read()
#             print("\n--- Contenido del archivo ---")
#             print(contenido if contenido else "El archivo está vacío.")

#     except FileNotFoundError:
#         print("\nEl archivo no existe. Registre datos primero.")




# def mostrar_ultimos_registros():
#     try:
#         with open(archive, "r") as file:
#             lines = file.readlines()
#             registros = [line for line in lines if line.strip() != "-" * 30]
#             if registros:
#                 print("\n--- Últimos registros ---")
#                 for line in registros[-6:]:
#                     print(line, end="")
#             else:
#                 print("El archivo no contiene registros.")
#     except FileNotFoundError:
#         print("\nEl archivo no existe. Registre datos primero.")


# def menu():
#     while True:
#         print("\n--- Menú ---")
#         print("1. Registrar datos")
#         print("2. Mostrar todos los registros")
#         print("3. Mostrar los últimos registros")
#         print("4. Salir")

#         opcion = input("Seleccione una opción: ")
#         if opcion == "1":
#             registrar_datos()
#         elif opcion == "2":
#             mostrar_todo()
#         elif opcion == "3":
#             mostrar_ultimos_registros()
#         elif opcion == "4":
#             print("¡Hasta luego!")
#             break
#         else:
#             print("Opción inválida. Intente de nuevo.")


# menu()
