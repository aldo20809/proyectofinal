import tkinter as tk
from tkinter import simpledialog, messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agencia de Autos - Menú Principal")
ventana.geometry("400x400")

# Lista para almacenar automóviles
automoviles = []

# Función para agregar un automóvil
def agregar_automovil():
    # Crear una nueva ventana para agregar un automóvil
    ventana_agregar = tk.Toplevel(ventana)
    ventana_agregar.title("Agregar Automóvil")
    ventana_agregar.geometry("300x300")
    
    # Etiquetas y campos de entrada para los datos del automóvil
    tk.Label(ventana_agregar, text="Marca del automóvil:").pack()
    entrada_marca = tk.Entry(ventana_agregar)
    entrada_marca.pack(pady=5)
    
    tk.Label(ventana_agregar, text="Modelo del automóvil:").pack()
    entrada_modelo = tk.Entry(ventana_agregar)
    entrada_modelo.pack(pady=5)
    
    tk.Label(ventana_agregar, text="Año del automóvil:").pack()
    entrada_año = tk.Entry(ventana_agregar)
    entrada_año.pack(pady=5)
    
    tk.Label(ventana_agregar, text="Precio del automóvil:").pack()
    entrada_precio = tk.Entry(ventana_agregar)
    entrada_precio.pack(pady=5)
    
    # Función para guardar los datos ingresados
    def guardar_automovil():
        marca = entrada_marca.get()
        modelo = entrada_modelo.get()
        año = entrada_año.get()
        precio = entrada_precio.get()

        # Validación de los datos
        if marca and modelo and año and precio:
            automoviles.append({'marca': marca, 'modelo': modelo, 'año': año, 'precio': precio})
            resultado.config(text=f"Automóvil agregado:\nMarca: {marca}, Modelo: {modelo}, Año: {año}, Precio: ${precio}")
            ventana_agregar.destroy()  # Cerrar la ventana de agregar automóvil
        else:
            resultado.config(text="Error: Ingrese datos válidos en todos los campos.")

    # Botón para guardar el automóvil
    tk.Button(ventana_agregar, text="Guardar Automóvil", command=guardar_automovil).pack(pady=10)

# Función para ver automóviles (ejemplo simple)
def ver_automoviles():
    resultado.config(text="\n".join([f"{i+1}. {auto['marca']} {auto['modelo']} ({auto['año']}) - ${auto['precio']}" for i, auto in enumerate(automoviles)]))

# Función para actualizar un automóvil
def actualizar_automovil():
    if not automoviles:
        messagebox.showinfo("Información", "No hay automóviles para actualizar.")
        return

    indice = simpledialog.askinteger("Actualizar Automóvil", "Ingrese el número del automóvil a actualizar:")
    if indice and 0 < indice <= len(automoviles):
        auto = automoviles[indice - 1]

        # Pedir nuevos valores
        nueva_marca = simpledialog.askstring("Actualizar Marca", "Nueva Marca:", initialvalue=auto['marca'])
        nuevo_modelo = simpledialog.askstring("Actualizar Modelo", "Nuevo Modelo:", initialvalue=auto['modelo'])
        nuevo_año = simpledialog.askstring("Actualizar Año", "Nuevo Año:", initialvalue=auto['año'])
        nuevo_precio = simpledialog.askstring("Actualizar Precio", "Nuevo Precio:", initialvalue=auto['precio'])

        # Actualizar los valores si se ingresaron
        if nueva_marca: auto['marca'] = nueva_marca
        if nuevo_modelo: auto['modelo'] = nuevo_modelo
        if nuevo_año: auto['año'] = nuevo_año
        if nuevo_precio: auto['precio'] = nuevo_precio

        resultado.config(text=f"Automóvil actualizado:\nMarca: {auto['marca']}, Modelo: {auto['modelo']}, Año: {auto['año']}, Precio: ${auto['precio']}")
    else:
        messagebox.showerror("Error", "Índice de automóvil inválido.")

# Función para eliminar un automóvil
def eliminar_automovil():
    if not automoviles:
        messagebox.showinfo("Información", "No hay automóviles para eliminar.")
        return

    indice = simpledialog.askinteger("Eliminar Automóvil", "Ingrese el número del automóvil a eliminar:")
    if indice and 0 < indice <= len(automoviles):
        auto = automoviles.pop(indice - 1)
        resultado.config(text=f"Automóvil eliminado:\nMarca: {auto['marca']}, Modelo: {auto['modelo']}, Año: {auto['año']}, Precio: ${auto['precio']}")
    else:
        messagebox.showerror("Error", "Índice de automóvil inválido.")

# Etiqueta de bienvenida
etiqueta_bienvenida = tk.Label(ventana, text="Bienvenido a la Agencia de Autos")
etiqueta_bienvenida.pack(pady=10)

# Botón para agregar automóvil
boton_agregar = tk.Button(ventana, text="Agregar Automóvil", command=agregar_automovil)
boton_agregar.pack(pady=5)

# Botón para ver automóviles
boton_ver = tk.Button(ventana, text="Ver Automóviles", command=ver_automoviles)
boton_ver.pack(pady=5)

# Botón para actualizar automóvil
boton_actualizar = tk.Button(ventana, text="Actualizar Automóvil", command=actualizar_automovil)
boton_actualizar.pack(pady=5)

# Botón para eliminar automóvil
boton_eliminar = tk.Button(ventana, text="Eliminar Automóvil", command=eliminar_automovil)
boton_eliminar.pack(pady=5)

# Etiqueta para mostrar el resultado o mensajes
resultado = tk.Label(ventana, text="")
resultado.pack(pady=20)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
