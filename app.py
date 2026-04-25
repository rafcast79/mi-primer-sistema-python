import os

archivo = "nombres.txt"

nombres = []

# Cargar datos
if os.path.exists(archivo):
    with open(archivo, "r") as f:
        for linea in f:
            nombres.append(linea.strip())

def guardar_todo():
    with open(archivo, "w") as f:
        for n in nombres:
            f.write(n + "\n")

while True:
    print("\n1. Agregar nombre")
    print("2. Ver nombres")
    print("3. Buscar nombre")
    print("4. Eliminar nombre")
    print("5. Editar nombre")
    print("6. Salir")

    opcion = input("Elige una opción: ").strip()

    # AGREGAR
    if opcion == "1":
        nombre = input("Escribe un nombre: ").strip()

        if nombre and nombre not in nombres:
            nombres.append(nombre)
            guardar_todo()
            print("✅ Nombre guardado")
        else:
            print("⚠️ Nombre inválido o repetido")

    # VER
    elif opcion == "2":
        print("\nLista de nombres:")
        for i, n in enumerate(nombres):
            print(f"{i+1}. {n}")

    # BUSCAR
    elif opcion == "3":
        buscar = input("Nombre a buscar: ").strip()

        encontrados = [n for n in nombres if buscar.lower() in n.lower()]

        if encontrados:
            print("🔍 Resultados:")
            for n in encontrados:
                print("-", n)
        else:
            print("❌ No encontrado")

    # ELIMINAR
    elif opcion == "4":
        nombre = input("Nombre a eliminar: ").strip()

        if nombre in nombres:
            nombres.remove(nombre)
            guardar_todo()
            print("🗑️ Eliminado")
        else:
            print("❌ No existe")

    # EDITAR
    elif opcion == "5":
        nombre = input("Nombre a editar: ").strip()

        if nombre in nombres:
            nuevo = input("Nuevo nombre: ").strip()

            if nuevo:
                index = nombres.index(nombre)
                nombres[index] = nuevo
                guardar_todo()
                print("✏️ Actualizado")
            else:
                print("⚠️ Nombre vacío")
        else:
            print("❌ No existe")

    # SALIR
    elif opcion == "6":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")