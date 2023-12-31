import tkinter as tk
import json
from evento import Evento
from ubicacion import Ubicacion
from review import Review
from tkintermapview import map_widget
from PIL import Image, ImageTk
from mapas import Mapa

def cargar_eventos_desde_json():
    with open('data/eventos.json', 'r') as archivo:
        eventos_data = json.load(archivo)
    eventos = [Evento(**evento) for evento in eventos_data]
    return eventos

def cargar_ubicaciones_desde_json():
    with open('data/ubicaciones.json', 'r') as archivo:
        ubicaciones_data = json.load(archivo)
    ubicaciones = [Ubicacion(**ubicacion) for ubicacion in ubicaciones_data]
    return ubicaciones

def cargar_reviews_desde_json():
    with open('data/reviews.json', 'r') as archivo:
        reviews_data = json.load(archivo)
    reviews = [Review(**review) for review in reviews_data]
    return reviews

def guardar_review(review):
    reviews = cargar_reviews_desde_json()
    reviews.append(review)

    reviews_data = [{"id_evento": r.id_evento, "calificacion": r.calificacion, "comentario": r.comentario, "animo": r.animo} for r in reviews]
    with open('data/reviews.json', 'w') as archivo:
        json.dump(reviews_data, archivo, indent=4)

def mostrar_pantalla_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Tour Musical")
    ventana_principal.geometry("960x720")
    
    def mostrar_eventos():
        ventana_eventos = tk.Toplevel()
        ventana_eventos.title("Eventos Disponibles")
        ventana_eventos.geometry("800x600")
        eventos = cargar_eventos_desde_json()

        def mostrar_escribir_review(evento):
            ventana_review = tk.Toplevel()
            ventana_review.title("Escribir Review")
            ventana_review.geometry("300x200")

            label_evento = tk.Label(ventana_review, text=f"Evento: {evento.nombre}", font=("Arial", 12, "bold"))
            label_evento.pack()

            label_calificacion = tk.Label(ventana_review, text="Calificación:")
            label_calificacion.pack()
            entry_calificacion = tk.Entry(ventana_review)
            entry_calificacion.pack()

            label_comentario = tk.Label(ventana_review, text="Comentario:")
            label_comentario.pack()
            entry_comentario = tk.Entry(ventana_review)
            entry_comentario.pack()

            label_animo = tk.Label(ventana_review, text="Ánimo:")
            label_animo.pack()
            entry_animo = tk.Entry(ventana_review)
            entry_animo.pack()

            btn_guardar = tk.Button(ventana_review, text="Guardar Review", command=lambda: guardar_nueva_review(evento, entry_calificacion.get(), entry_comentario.get(), entry_animo.get()))
            btn_guardar.pack()
            
        
        for evento in eventos:
            label_evento = tk.Label(ventana_eventos, text=evento.nombre, font=("Arial", 12, "bold"), bg="#E5E5E5", fg="#2F242C")
            label_evento.pack()

            label_descripcion = tk.Label(ventana_eventos, text=evento.descripcion, font=("Arial", 10), bg="#E5E5E5", fg="#2F242C")
            label_descripcion.pack()

            label_artista = tk.Label(ventana_eventos, text=f"Artista: {evento.artista}", font=("Arial", 10), bg="#E5E5E5", fg="#2F242C")
            label_artista.pack()

            btn_ver_mas = tk.Button(ventana_eventos, text="Ver más", command=lambda e=evento: mostrar_info_evento(e))
            btn_ver_mas.pack()

            btn_escribir_review = tk.Button(ventana_eventos, text="Escribir Review", command=lambda e=evento: mostrar_escribir_review(e))
            btn_escribir_review.pack()

    def mostrar_info_evento(evento):
        ventana_info_evento = tk.Toplevel()
        ventana_info_evento.title(evento.nombre)
        ventana_info_evento.geometry("300x300")

        imagen = Image.open(evento.imagen)
        imagen = imagen.resize((200, 200), Image.ANTIALIAS)
        imagen = ImageTk.PhotoImage(imagen)

        label_imagen = tk.Label(ventana_info_evento, image=imagen)
        label_imagen.image = imagen
        label_imagen.pack()

        label_artista = tk.Label(ventana_info_evento, text=f"Artista: {evento.artista}")
        label_artista.pack()

        label_genero = tk.Label(ventana_info_evento, text=f"Género: {evento.genero}")
        label_genero.pack()

        label_hora_inicio = tk.Label(ventana_info_evento, text=f"Hora de inicio: {evento.hora_inicio}")
        label_hora_inicio.pack()

        label_descripcion = tk.Label(ventana_info_evento, text=f"Descripción: {evento.descripcion}")
        label_descripcion.pack()

    def mostrar_mapa():
        ruta_imagen_mapa = 'views/Mapa.jpg'  # Reemplaza con la ruta de tu imagen del mapa
        mapa = Mapa(ruta_imagen_mapa)
        mapa.mostrar()

        btn_mapa = tk.Button(ventana_principal, text="Mostrar Mapa", font=("Arial", 14), width=15, command=mostrar_mapa)
        btn_mapa.pack(padx=10, pady=10)

    def mostrar_reviews():
        ventana_reviews = tk.Toplevel()
        ventana_reviews.title("Reviews de Eventos")
        ventana_reviews.geometry("800x600")

        reviews = cargar_reviews_desde_json()

        for review in reviews:
            label_review = tk.Label(ventana_reviews, text=f"Evento: {review.id_evento}", font=("Arial", 12, "bold"))
            label_review.pack()

            label_calificacion = tk.Label(ventana_reviews, text=f"Calificación: {review.calificacion}")
            label_calificacion.pack()

            label_comentario = tk.Label(ventana_reviews, text=f"Comentario: {review.comentario}")
            label_comentario.pack()

            label_animo = tk.Label(ventana_reviews, text=f"Ánimo: {review.animo}")
            label_animo.pack()

    def guardar_nueva_review(evento, calificacion, comentario, animo):
        nueva_review = Review(evento.id, calificacion, comentario, animo)
        guardar_review(nueva_review)
        # Opcional: Recargar la sección de reviews para mostrar la nueva review inmediatamente
        mostrar_reviews()

    btn_eventos = tk.Button(ventana_principal, text="Eventos", font=("Arial", 14), width=15, command=mostrar_eventos)
    btn_eventos.pack(side=tk.LEFT, padx=10, pady=10)

    btn_mapa = tk.Button(ventana_principal, text="Mapa", font=("Arial", 14), width=15, command=mostrar_mapa)
    btn_mapa.pack(side=tk.LEFT, padx=10, pady=10)

    btn_reviews = tk.Button(ventana_principal, text="Reviews", font=("Arial", 14), width=15, command=mostrar_reviews)
    btn_reviews.pack(side=tk.LEFT, padx=10, pady=10)

    ventana_principal.mainloop()

mostrar_pantalla_principal()