import tkinter as tk

def agregar():
    # Función a ejecutar cuando se presiona el botón "Agregar"
    pass  # Aquí puedes agregar la lógica para la funcionalidad de agregar

def comentar():
    # Función a ejecutar cuando se presiona el botón "Comentar"
    pass  # Aquí puedes agregar la lógica para la funcionalidad de comentar

def subir_cambios():
    # Función a ejecutar cuando se presiona el botón "Subir cambios"
    pass  # Aquí puedes agregar la lógica para la funcionalidad de subir cambios

# Crear la ventana principal
root = tk.Tk()
root.title("Control de Versiones")

# Definir el tamaño de la ventana
window_width = 350
window_height = 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Establecer tamaño mínimo de la ventana
root.minsize(300, 250)

# Crear estilo de fuente
font_style = ("Times New Roman", 15)

# Campo de texto junto al botón "Agregar"
texto_agregar = tk.StringVar()
entrada_texto_agregar = tk.Entry(root, textvariable=texto_agregar, font=font_style)
entrada_texto_agregar.grid(row=0, column=0, padx=10, pady=10)  # Añadir espacio horizontal y vertical

# Botón "Agregar"
btn_agregar = tk.Button(root, text="Agregar", command=agregar, font=font_style)
btn_agregar.grid(row=0, column=1, padx=10, pady=10)  # Añadir espacio horizontal y vertical

# Campo de texto junto al botón "Comentar"
texto_comentar = tk.StringVar()
entrada_texto_comentar = tk.Entry(root, textvariable=texto_comentar, font=font_style)
entrada_texto_comentar.grid(row=1, column=0, padx=10, pady=10)  # Añadir espacio horizontal y vertical

# Botón "Comentar"
btn_comentar = tk.Button(root, text="Comentar", command=comentar, font=font_style)
btn_comentar.grid(row=1, column=1, padx=10, pady=10)  # Añadir espacio horizontal y vertical

# Botón "Subir cambios"
btn_subir_cambios = tk.Button(root, text="Subir cambios", command=subir_cambios, font=font_style)
btn_subir_cambios.grid(row=2, column=0, columnspan=2, pady=20)  # Añadir espacio vertical y centrar

# Ejecutar el bucle principal
root.mainloop()
