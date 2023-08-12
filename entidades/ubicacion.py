import json
class Coordenadas:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud

class Ubicacion:
    def __init__(self, id, nombre, direccion, coordenadas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "coordenadas": {
                "latitud": self.coordenadas.latitud,
                "longitud": self.coordenadas.longitud
            }
        }

    @classmethod
    def from_json(cls, data):
        coordenadas_data = data["coordenadas"]
        coordenadas = Coordenadas(coordenadas_data["latitud"], coordenadas_data["longitud"])
        return cls(data["id"], data["nombre"], data["direccion"], coordenadas)
