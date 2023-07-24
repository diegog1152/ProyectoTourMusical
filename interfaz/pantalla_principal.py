import tkinter as tk
from evento import cargar_eventos_desde_json
from ubicacion import cargar_ubicaciones_desde_json
from review import cargar_reviews_desde_json
from PIL import Image, ImageTk
from tkintermapview import MapView

def mostrar_pantalla_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Tour Musical")
    ventana_principal.geometry("800x600")

    def mostrar_eventos():
        ventana_eventos = tk.Toplevel()
        ventana_eventos.title("Eventos Disponibles")
        ventana_eventos.geometry("400x500")
        eventos = cargar_eventos_desde_json()

        for evento in eventos:
            imagen = Image.open(evento.imagen)
            imagen = imagen.resize((150, 150), Image.ANTIALIAS)
            imagen = ImageTk.PhotoImage(imagen)

            label_evento = tk.Label(ventana_eventos, text=evento.nombre, font=("Arial", 12, "bold"), bg="#E5E5E5", fg="#2F242C")
            label_evento.pack()

            label_imagen = tk.Label(ventana_eventos, image=imagen, bg="#E5E5E5")
            label_imagen.image = imagen
            label_imagen.pack()

            label_descripcion = tk.Label(ventana_eventos, text=evento.descripcion, font=("Arial", 10), bg="#E5E5E5", fg="#2F242C")
            label_descripcion.pack()

            btn_ver_mas = tk.Button(ventana_eventos, text="Ver más", command=lambda e=evento: mostrar_info_evento(e))
            btn_ver_mas.pack()

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
        ventana_mapa = tk.Toplevel()
        ventana_mapa.title("Mapa de Eventos")
        ventana_mapa.geometry("800x600")

        eventos = cargar_eventos_desde_json()
        ubicaciones = cargar_ubicaciones_desde_json()

        map_view = MapView(ventana_mapa, zoom=12)
        map_view.pack(fill=tk.BOTH, expand=True)

        for ubicacion in ubicaciones:
            for evento in eventos:
                if evento.id_ubicacion == ubicacion.id:
                    map_view.add_marker(ubicacion.coordenadas[0], ubicacion.coordenadas[1], evento.nombre)

    def mostrar_reviews():
        ventana_reviews = tk.Toplevel()
        ventana_reviews.title("Reviews de Eventos")
        ventana_reviews.geometry("400x500")

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

    btn_eventos = tk.Button(ventana_principal, text="Eventos", command=mostrar_eventos)
    btn_eventos.pack()

    btn_mapa = tk.Button(ventana_principal, text="Mapa", command=mostrar_mapa)
    btn_mapa.pack()

    btn_reviews = tk.Button(ventana_principal, text="Reviews", command=mostrar_reviews)
    btn_reviews.pack()

    ventana_principal.mainloop()

mostrar_pantalla_principal()
