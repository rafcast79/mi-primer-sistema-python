import tkinter as tk
import mysql.connector

# conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="V6078sHxfrQi",
    database="mi_sistema"
)
cursor = conexion.cursor()

# función guardar
def guardar_nombre():
    nombre = entrada.get().strip()

    if nombre == "":
        etiqueta_resultado.config(text="❌ Nombre vacío")
    else:
        sql = "INSERT INTO nombres (nombre) VALUES (%s)"
        cursor.execute(sql, (nombre,))
        conexion.commit()

        etiqueta_resultado.config(text="✅ Guardado")
        entrada.delete(0, tk.END)

def ver_nombres():
    lista_nombres.delete(0, tk.END)

    cursor.execute("SELECT * FROM nombres")
    resultados = cursor.fetchall()

    for fila in resultados:
        lista_nombres.insert(tk.END, f"{fila[0]} - {fila[1]}")

def eliminar_nombre():
    seleccion = lista_nombres.get(tk.ACTIVE)

    if not seleccion:
        etiqueta_resultado.config(text="❌ Selecciona un nombre")
        return

    id_nombre = seleccion.split(" - ")[0]

    sql = "DELETE FROM nombres WHERE id = %s"
    cursor.execute(sql, (id_nombre,))
    conexion.commit()

    etiqueta_resultado.config(text="🗑️ Eliminado")

    ver_nombres()

def seleccionar_nombre(event):
    seleccion = lista_nombres.get(tk.ACTIVE)

    if seleccion:
        nombre = seleccion.split(" - ")[1]
        entrada.delete(0, tk.END)
        entrada.insert(0, nombre)

def editar_nombre():
    seleccion = lista_nombres.get(tk.ACTIVE)

    if not seleccion:
        etiqueta_resultado.config(text="❌ Selecciona un nombre")
        return

    id_nombre = seleccion.split(" - ")[0]
    nuevo_nombre = entrada.get().strip()

    if nuevo_nombre == "":
        etiqueta_resultado.config(text="❌ Nombre vacío")
        return

    sql = "UPDATE nombres SET nombre = %s WHERE id = %s"
    cursor.execute(sql, (nuevo_nombre, id_nombre))
    conexion.commit()

    etiqueta_resultado.config(text="✏️ Actualizado")

    ver_nombres()

def buscar_nombre():
    texto_buscar = entrada_buscar.get().strip()

    if texto_buscar == "":
        etiqueta_resultado.config(text="❌ Escribe algo para buscar")
        return

    lista_nombres.delete(0, tk.END)

    sql = "SELECT * FROM nombres WHERE nombre LIKE %s"
    cursor.execute(sql, (f"%{texto_buscar}%",))
    resultados = cursor.fetchall()

    if not resultados:
        etiqueta_resultado.config(text="😢 No encontrado")
        return

    for fila in resultados:
        lista_nombres.insert(tk.END, f"{fila[0]} - {fila[1]}")

    etiqueta_resultado.config(text="🔍 Resultados")

# ventana
ventana = tk.Tk()
ventana.title("Mi primer sistema 😎")

entrada_buscar = tk.Entry(ventana)
entrada_buscar.pack(pady=5)

# botón buscar
boton_buscar = tk.Button(ventana, text="Buscar", command=buscar_nombre)
boton_buscar.pack(pady=5)

# campo texto
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# botón
boton = tk.Button(ventana, text="Guardar", command=guardar_nombre)
boton.pack(pady=5)

boton_ver = tk.Button(ventana, text="Ver nombres", command=ver_nombres)
boton_ver.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_nombre)
boton_eliminar.pack(pady=5)

boton_editar = tk.Button(ventana, text="Editar", command=editar_nombre)
boton_editar.pack(pady=5)

# resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=5)

lista_nombres = tk.Listbox(ventana)
lista_nombres.pack(pady=5)

lista_nombres.bind("<<ListboxSelect>>", seleccionar_nombre)

# ejecutar
ventana.mainloop()
