
class Evento:
    def __init__(self, id, nombre, artista, genero, id_ubicacion, hora_inicio, hora_fin, descripcion, imagen):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen
    
class Ubicacion:
    def __init__(self, id, nombre, direccion, coordenadas):
        self.id = (id)
        self.nombre = (nombre)
        self.direccion = (direccion)
        self.coordenadas = [(coordenada) for coordenada in coordenadas]

    def obtener_coordenadas(self):
        return self.coordenadas

    def __str__(self):
        return f"Ubicación: {self.nombre}\nDirección: {self.direccion}\nCoordenadas: {self.coordenadas}"

class Usuario:
    def __init__(self, nombre, correo_electronico, ubicacion_actual):
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.ubicacion_actual = ubicacion_actual

    def agregar_evento(self, id_evento):
        self.historial_eventos.append((id_evento))

    def eliminar_evento(self, id_evento):
        if id_evento in self.historial_eventos:
            self.historial_eventos.remove((id_evento))

    def obtener_historial_eventos(self):
        return self.historial_eventos

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido}\nHistorial de eventos: {self.historial_eventos}"
    
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