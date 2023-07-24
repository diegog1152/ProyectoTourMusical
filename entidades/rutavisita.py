class RutaVisita:
    def __init__(self, id, nombre, destinos):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def agregar_destino(self, id_destino):
        self.destinos.append(id_destino)

    def eliminar_destino(self, id_destino):
        if id_destino in self.destinos:
            self.destinos.remove(id_destino)

    def obtener_destinos(self):
        return self.destinos

    def __str__(self):
        return f"Ruta de visita: {self.nombre}\nDestinos: {self.destinos}"