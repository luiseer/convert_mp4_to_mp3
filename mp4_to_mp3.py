import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.video.io.VideoFileClip import VideoFileClip
import webbrowser
import os
import threading

def convert_mp4_to_mp3_cli(input_file, output_file=None):
    """
    Convert an MP4 file to MP3 from command line
    
    Args:
        input_file (str): Path to the MP4 file
        output_file (str, optional): Path for the output MP3 file. 
                                    If not provided, uses the same name with .mp3 extension
    
    Returns:
        str: Path to the created MP3 file
    """
    try:
        if not output_file:
            # Generate output filename based on input filename
            output_file = os.path.splitext(input_file)[0] + ".mp3"
        
        # Load the video and extract audio
        video = VideoFileClip(input_file)
        video.audio.write_audiofile(output_file)
        video.close()
        
        return output_file
    except Exception as e:
        print(f"Error converting file: {str(e)}")
        return None


def convertir_mp4_a_mp3():
    # Abrir cuadro de diálogo para seleccionar el archivo MP4
    archivo_mp4 = filedialog.askopenfilename(filetypes=[("Archivos de video", "*.mp4")])

    if archivo_mp4:
        threading.Thread(target=procesar_conversion, args=(archivo_mp4,)).start()


def procesar_conversion(archivo_mp4):
    try:
        # Cargar el archivo de video
        video = VideoFileClip(archivo_mp4)
        # Obtener la ruta y nombre del archivo
        ruta_archivo, nombre_archivo = os.path.split(archivo_mp4)
        nombre_salida = os.path.join(ruta_archivo, os.path.splitext(nombre_archivo)[0] + ".mp3")

        # Verificar si el archivo ya existe
        if os.path.exists(nombre_salida):
            respuesta = messagebox.askyesno("Archivo existente", "El archivo ya existe. ¿Deseas sobrescribirlo?")
            if not respuesta:
                return

        # Extraer el audio y guardarlo como MP3
        video.audio.write_audiofile(nombre_salida)
        video.close()  # Cerrar el archivo para liberar recursos

        # Mostrar mensaje de éxito
        resultado_label.config(text="Conversión exitosa")
        messagebox.showinfo("Éxito", "El archivo MP3 se ha guardado correctamente.")

    except Exception as e:
        resultado_label.config(text="Error en la conversión")
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


def abrir_github():
    webbrowser.open_new("https://github.com/luiseer")


# Configuración de la ventana principal
root = tk.Tk()
root.title("Convertidor de MP4 a MP3")
root.geometry("600x400")

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

# Cargar imagen de fondo (verifica que exista)
try:
    imagen_fondo = tk.PhotoImage(file="logosimboloBasico_blanco.png")
    fondo_label = tk.Label(root, image=imagen_fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    print("Advertencia: Imagen de fondo no encontrada.")

# Etiqueta de bienvenida
bienvenida_label = tk.Label(root, text="Convertidor de MP4 a MP3 - Reclusorios Sur CJF", bg=colores["grisOscuro"], fg=colores["blanco"])
bienvenida_label.pack(pady=10)

# Botón para convertir
convertir_button = tk.Button(root, text="Convertir MP4 a MP3", command=convertir_mp4_a_mp3, bg=colores["secundario"], fg=colores["blanco"])
convertir_button.pack(pady=10)

# Botón para abrir GitHub
github_button = tk.Button(root, text="Mi perfil de GitHub", command=abrir_github, bg=colores["secundario"], fg=colores["blanco"])
github_button.pack(pady=10)

# Etiqueta de resultado
resultado_label = tk.Label(root, text="", bg=colores["grisOscuro"], fg=colores["blanco"])
resultado_label.pack()

# Ejecutar aplicación
root.mainloop()
