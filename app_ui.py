import tkinter as tk
from tkinter import messagebox
import mysql.connector

# conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="V6078sHxfrQi",
    database="mi_sistema"
)
cursor = conexion.cursor()

# -----------------------------------------------------------------------------
# Entiendo que aca, lo que tiene es la creacion de las variables de conexion a la base de datos, y el cursor para ejecutar las consultas SQL.
# -----------------------------------------------------------------------------

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
        entrada_buscar.delete(0, tk.END)

# funcion ver nombres
def ver_nombres():
    lista_nombres.delete(0, tk.END)

    cursor.execute("SELECT * FROM nombres")
    resultados = cursor.fetchall()

    for fila in resultados:
        lista_nombres.insert(tk.END, f"{fila[0]} - {fila[1]}")

# funcion eliminar nombre
def eliminar_nombre():
    seleccion = lista_nombres.get(tk.ACTIVE)

    if not seleccion:
        etiqueta_resultado.config(text="❌ Selecciona un nombre")
        return
    confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este nombre?")
    if not confirmar:
        return  

    id_nombre = seleccion.split(" - ")[0]

    sql = "DELETE FROM nombres WHERE id = %s"
    cursor.execute(sql, (id_nombre,))
    conexion.commit()

    etiqueta_resultado.config(text="🗑️ Eliminado")

    ver_nombres()

# funcion seleccionar nombre
def seleccionar_nombre(event):
    seleccion = lista_nombres.get(tk.ACTIVE)

    if seleccion:
        nombre = seleccion.split(" - ")[1]
        entrada.delete(0, tk.END)
        entrada.insert(0, nombre)

# funcion editar nombre
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
    entrada.delete(0, tk.END)
    ver_nombres()

# funcion buscar nombre
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
    entrada.delete(0, tk.END)
    entrada_buscar.delete(0, tk.END)
    etiqueta_resultado.config(text="🔍 Resultados")

# -----------------------------------------------------------------------------
# Entiendo que aca inician las ventanas y los elementos de la interfaz gráfica, como los frames, botones, campos de texto, etiquetas y listas.
# -----------------------------------------------------------------------------

# ventana
ventana = tk.Tk()
ventana.title("Mi primer sistema")

ventana.geometry("300x400")
ventana.resizable(False, False)

frame_busqueda = tk.Frame(ventana, bg="red")
frame_busqueda.pack(pady=10)

frame_acciones = tk.Frame(ventana, bg="blue")
frame_acciones.pack(pady=10)

frame_lista = tk.Frame(ventana, bg="green")
frame_lista.pack(pady=10)

entrada_buscar = tk.Entry(frame_busqueda)
entrada_buscar.pack(pady=5)

# botón buscar
boton_buscar = tk.Button(frame_busqueda, text="Buscar", command=buscar_nombre)
boton_buscar.pack(side="left", pady=5)

# campo texto
entrada = tk.Entry(frame_acciones)
entrada.pack(pady=5)

# botón guardar
boton = tk.Button(frame_acciones, text="Guardar", command=guardar_nombre)
boton.pack(side="left", pady=5)

# boton Mostrar todos
boton_mostrar = tk.Button(frame_acciones, text="Mostrar todos", command=ver_nombres)
boton_mostrar.pack(side="left", pady=5)

boton_eliminar = tk.Button(frame_acciones, text="Eliminar", command=eliminar_nombre)
boton_eliminar.pack(side="left", pady=5)

boton_editar = tk.Button(frame_acciones, text="Editar", command=editar_nombre)
boton_editar.pack(side="left", pady=5)

# resultado
etiqueta_resultado = tk.Label(frame_acciones, text="")
etiqueta_resultado.pack(pady=5)

lista_nombres = tk.Listbox(frame_lista, width=40, height=10)
lista_nombres.pack(pady=5)

lista_nombres.bind("<<ListboxSelect>>", seleccionar_nombre)

# ejecutar
ventana.mainloop()
