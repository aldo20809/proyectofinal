import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agencia de Autos - Menú Principal")
ventana.geometry("400x400")

# Lista para almacenar automóviles
automoviles = []

# Función para agregar un automóvil
def agregar_automovil():
    ventana_agregar = tk.Toplevel(ventana)
    ventana_agregar.title("Agregar Automóvil")
    ventana_agregar.geometry("300x300")
    
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
    
    def guardar_automovil():
        marca = entrada_marca.get()
        modelo = entrada_modelo.get()
        año = entrada_año.get()
        precio = entrada_precio.get()
        if marca and modelo and año and precio:
            automoviles.append({'marca': marca, 'modelo': modelo, 'año': año, 'precio': precio})
            resultado.config(text=f"Automóvil agregado:\nMarca: {marca}, Modelo: {modelo}, Año: {año}, Precio: ${precio}")
            ventana_agregar.destroy()
        else:
            resultado.config(text="Error: Ingrese datos válidos en todos los campos.")

    tk.Button(ventana_agregar, text="Guardar Automóvil", command=guardar_automovil).pack(pady=10)

# Función para mostrar la imagen de un auto deportivo
def mostrar_imagen(imagen_path):
    ventana_imagen = tk.Toplevel(ventana)
    ventana_imagen.title("Imagen del Automóvil")
    ventana_imagen.geometry("600x400")
    
    imagen = Image.open(imagen_path)
    imagen = imagen.resize((400, 300), Image.ANTIALIAS)
    imagen_tk = ImageTk.PhotoImage(imagen)
    
    etiqueta_imagen = tk.Label(ventana_imagen, image=imagen_tk)
    etiqueta_imagen.image = imagen_tk
    etiqueta_imagen.pack(pady=20)

# Función para mostrar las imágenes de una marca específica
def mostrar_imagenes_marca(marca):
    ventana_marca = tk.Toplevel(ventana)
    ventana_marca.title(f"Imágenes de {marca}")
    ventana_marca.geometry("300x400")
    
    imagenes = {
        "Ferrari": ["path_to_ferrari_image1.jpg", "path_to_ferrari_image2.jpg", "path_to_ferrari_image3.jpg",
                    "path_to_ferrari_image4.jpg", "path_to_ferrari_image5.jpg", "path_to_ferrari_image6.jpg",
                    "path_to_ferrari_image7.jpg", "path_to_ferrari_image8.jpg", "path_to_ferrari_image9.jpg",
                    "path_to_ferrari_image10.jpg"],
        "Lamborghini": ["path_to_lamborghini_image1.jpg", "path_to_lamborghini_image2.jpg", "path_to_lamborghini_image3.jpg",
                        "path_to_lamborghini_image4.jpg", "path_to_lamborghini_image5.jpg", "path_to_lamborghini_image6.jpg",
                        "path_to_lamborghini_image7.jpg", "path_to_lamborghini_image8.jpg", "path_to_lamborghini_image9.jpg",
                        "path_to_lamborghini_image10.jpg"],
        # Agrega más marcas y sus imágenes aquí...
    }
    
    if marca in imagenes:
        for imagen_path in imagenes[marca]:
            tk.Button(ventana_marca, text=imagen_path.split('/')[-1], command=lambda p=imagen_path: mostrar_imagen(p)).pack(pady=5)

# Función para ver automóviles
def ver_automoviles():
    ventana_ver = tk.Toplevel(ventana)
    ventana_ver.title("Marcas de Autos Deportivos")
    ventana_ver.geometry("300x400")
    
    marcas = ["Ferrari", "Lamborghini", "Porsche", "Aston Martin", "McLaren", "Bugatti", "Maserati", "Koenigsegg", "Pagani", "Lotus"]
    
    for marca in marcas:
        tk.Button(ventana_ver, text=marca, command=lambda m=marca: mostrar_imagenes_marca(m)).pack(pady=5)

# Función para actualizar un automóvil
def actualizar_automovil():
    if not automoviles:
        messagebox.showinfo("Información", "No hay automóviles para actualizar.")
        return

    indice = simpledialog.askinteger("Actualizar Automóvil", "Ingrese el número del automóvil a actualizar:")
    if indice and 0 < indice <= len(automoviles):
        auto = automoviles[indice - 1]
        nueva_marca = simpledialog.askstring("Actualizar Marca", "Nueva Marca:", initialvalue=auto['marca'])
        nuevo_modelo = simpledialog.askstring("Actualizar Modelo", "Nuevo Modelo:", initialvalue=auto['modelo'])
        nuevo_año = simpledialog.askstring("Actualizar Año", "Nuevo Año:", initialvalue=auto['año'])
        nuevo_precio = simpledialog.askstring("Actualizar Precio", "Nuevo Precio:", initialvalue=auto['precio'])
        
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

# Botones
tk.Button(ventana, text="Agregar Automóvil", command=agregar_automovil).pack(pady=5)
tk.Button(ventana, text="Ver Automóviles", command=ver_automoviles).pack(pady=5)
tk.Button(ventana, text="Actualizar Automóvil", command=actualizar_automovil).pack(pady=5)
tk.Button(ventana, text="Eliminar Automóvil", command=eliminar_automovil).pack(pady=5)

# Etiqueta para mostrar el resultado o mensajes
resultado = tk.Label(ventana, text="")
resultado.pack(pady=20)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
