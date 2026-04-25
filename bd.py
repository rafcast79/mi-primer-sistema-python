import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="V6078sHxfrQi",
    database="mi_sistema"
)

cursor = conexion.cursor()

print("✅ Conectado a MySQL")

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

        if nombre == "":
            print("❌ Nombre vacío")
        else:
            sql = "INSERT INTO nombres (nombre) VALUES (%s)"
            cursor.execute(sql, (nombre,))
            conexion.commit()   

            print("✅ Guardado")

    # VER
    elif opcion == "2":
        cursor.execute("SELECT * FROM nombres")
        resultados = cursor.fetchall()

        print("\n📋 Lista:")
        for fila in resultados:
            print(f"{fila[0]}. {fila[1]}")

    # BUSCAR
    elif opcion == "3":
        buscar = input("Nombre a buscar: ")

        sql = "SELECT * FROM nombres WHERE nombre LIKE %s"
        cursor.execute(sql, (f"%{buscar}%",))
        resultados = cursor.fetchall()

        if resultados:
            print("🔍 Resultados:")
            for fila in resultados:
                print(fila)
        else:
            print("❌ No encontrado")

    # ELIMINAR
    elif opcion == "4":
        id_eliminar = input("ID a eliminar: ")

        # Verificar si existe
        sql = "SELECT * FROM nombres WHERE id = %s"
        cursor.execute(sql, (id_eliminar,))
        resultado = cursor.fetchone()

        if resultado:
            confirmacion = input("¿Seguro que quieres eliminar? (s/n): ").lower()

            if confirmacion == "s":
                sql = "DELETE FROM nombres WHERE id = %s"
                cursor.execute(sql, (id_eliminar,))
                conexion.commit()

                print("🗑️ Eliminado")
            else:
                print("❌ Cancelado")
        else:
            print("⚠️ Ese ID no existe")

    # EDITAR
    elif opcion == "5":
        id_editar = input("ID a editar: ")
        nuevo_nombre = input("Nuevo nombre: ")

        sql = "UPDATE nombres SET nombre = %s WHERE id = %s"
        cursor.execute(sql, (nuevo_nombre, id_editar))
        conexion.commit()

        print("✏️ Actualizado")

    # SALIR
    elif opcion == "6":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")

conexion.close()