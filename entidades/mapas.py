from PIL import Image, ImageTk
import tkinter as tk

class Mapa:
    def __init__(self, ruta_imagen):
        self.imagen_mapa = Image.open(ruta_imagen)
        self.imagen_mapa = self.imagen_mapa.resize((800, 600), Image.ANTIALIAS)
        self.imagen_mapa = ImageTk.PhotoImage(self.imagen_mapa)

    def mostrar(self):
        ventana_mapa = tk.Toplevel()
        ventana_mapa.title("Mapa de Eventos")
        ventana_mapa.geometry("800x600")

        label_imagen = tk.Label(ventana_mapa, image=self.imagen_mapa)
        label_imagen.pack()

        ventana_mapa.mainloop()
