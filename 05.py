
import datetime as dt

# Función para registrar ventas
def registrar_venta():
    ventas = []
    for i in range(3):  # Se registran 3 ventas por día
        print(f"\nVenta {i + 1}")
        producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad vendida: "))

        # Cálculos
        subtotal = precio * cantidad
        igv = subtotal * 0.18  # Asumimos que el IGV es 18%
        total = subtotal + igv

        # Fecha de la venta
        fecha = dt.date.today()

        # Almacenamos los datos de la venta
        ventas.append({
            "producto": producto,
            "precio": precio,
            "cantidad": cantidad,
            "subtotal": subtotal,
            "igv": igv,
            "total": total,
            "fecha": fecha
        })

    # Guardamos las ventas en un archivo
    with open("ventas.txt", "a") as file:
        for venta in ventas:
            file.write(f"\nFecha: {venta['fecha']}\n")
            file.write(f"Producto: {venta['producto']}\n")
            file.write(f"Precio: {venta['precio']}\n")
            file.write(f"Cantidad: {venta['cantidad']}\n")
            file.write(f"Subtotal: {venta['subtotal']:.2f}\n")
            file.write(f"IGV (18%): {venta['igv']:.2f}\n")
            file.write(f"Total: {venta['total']:.2f}\n")
            file.write("-" * 30 + "\n")
    
    print("\nLas ventas han sido registradas.")

# Función para mostrar todas las ventas registradas
def mostrar_ventas():
    try:
        with open("ventas.txt", "r") as file:
            contenido = file.read()
            if contenido:
                print("\n--- Ventas Registradas ---")
                print(contenido)
            else:
                print("No hay ventas registradas aún.")
    except FileNotFoundError:
        print("\nEl archivo no existe. Registre ventas primero.")

# Función principal con el menú
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar ventas")
        print("2. Mostrar todas las ventas registradas")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            mostrar_ventas()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar el menú
menu()
