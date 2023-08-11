import json

class Evento:
    def __init__(self, id, nombre, artista, genero, id_ubicacion, hora_inicio, descripcion, imagen):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.descripcion = descripcion
        self.imagen = imagen

    def __str__(self):
        return f"{self.nombre}"

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "artista": self.artista,
            "genero": self.genero,
            "id_ubicacion": self.id_ubicacion,
            "hora_inicio": self.hora_inicio,
            "descripcion": self.descripcion,
            "imagen": self.imagen
        }

    @classmethod
    def from_json(cls, data):
        return cls(data["id"], data["nombre"], data["artista"], data["genero"], data["id_ubicacion"],
                   data["hora_inicio"], data["descripcion"], data["imagen"])

    @classmethod
    def cargar_eventos_desde_json(cls):
        ruta_archivo = "data/eventos.json"  # Ruta relativa al archivo desde evento.py
        eventos = []
        with open(ruta_archivo, "r") as archivo:
            data = json.load(archivo)
            for evento_data in data:
                evento = cls.from_json(evento_data)
                eventos.append(evento)
        return eventos


