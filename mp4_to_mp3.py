import tkinter as tk
from tkinter import filedialog
import moviepy
from moviepy.editor import *
import webbrowser
import os





def convertir_mp4_a_mp3():
    # Abrir un cuadro de diálogo para seleccionar el archivo de entrada
    archivo_mp4 = filedialog.askopenfilename(filetypes=[("Archivos de video", "*.mp4")])

    if archivo_mp4:
        try:
            # Cargar el archivo de video
            video = VideoFileClip(archivo_mp4)

            # Obtener la ruta y el nombre del archivo de entrada
            ruta_archivo, nombre_archivo = os.path.split(archivo_mp4)

            # Extraer el audio del archivo de video
            audio = video.audio

            # Obtener el nombre del archivo de salida (con la extensión mp3)
            nombre_archivo_mp3 = os.path.join(ruta_archivo, os.path.splitext(nombre_archivo)[0] + ".mp3")

            # Guardar el audio extraído en formato mp3
            audio.write_audiofile(nombre_archivo_mp3)

            print("La conversión fue exitosa.")
            resultado_label.config(text="La conversión fue exitosa.")

        except Exception as e:
            print(f"Ocurrió un error: {e}")
            resultado_label.config(text="Ocurrió un error durante la conversión.")

def abrir_github():
    webbrowser.open_new("https://github.com/luiseer")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Convertidor de MP4 a MP3")
root.geometry("600x400")  # Tamaño personalizado de la ventana

# Definición de colores
colores = {
    "primario": "#24135f",
    "secundario": "#5b38d7",
    "gris": "#757575",
    "grisClaro": "#e1e1e1",
    "grisOscuro": "#333",
    "blanco": "#ffffff",
    "negro": "#212121"
}

# Cargar la imagen de fondo
imagen_fondo = tk.PhotoImage(file="logosimboloBasico_blanco.png")
fondo_label = tk.Label(root, image=imagen_fondo, padx=15, pady=15)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Etiqueta de bienvenida
bienvenida_label = tk.Label(root, text="Bienvenido al convertidor de MP4 a MP3 Reclusorios Sur CJF", bg=colores["grisOscuro"], fg=colores["blanco"])
bienvenida_label.pack(pady=10)

# Botón para iniciar la conversión
convertir_button = tk.Button(root, text="Convertir MP4 a MP3", command=convertir_mp4_a_mp3, bg=colores["secundario"], fg=colores["blanco"])
convertir_button.pack(pady=10)

# Botón para abrir el perfil de GitHub
github_button = tk.Button(root, text="Mi perfil de GitHub", command=abrir_github, bg=colores["secundario"], fg=colores["blanco"])
github_button.pack(pady=10)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="", bg=colores["grisOscuro"], fg=colores["blanco"])
resultado_label.pack()

# Ejecutar la aplicación
root.mainloop()
