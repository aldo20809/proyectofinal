import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agencia de Autos - Menú Principal")
ventana.geometry("400x300")

# Función para agregar un automóvil
def agregar_automovil():
 resultado.config(text="Función de agregar automóvil no implementada.")

# Función para ver automóviles
def ver_automoviles():
 resultado.config(text="Función de ver automóviles no implementada.")

# Función para actualizar un automóvil
def actualizar_automovil():
  resultado.config(text="Función de actualizar automóvil no implementada.")

# Función para eliminar un automóvil
def eliminar_automovil():
  resultado.config(text="Función de eliminar automóvil no implementada.")

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