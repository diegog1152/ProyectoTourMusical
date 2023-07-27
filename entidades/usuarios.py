import json

class Usuario:
    def __init__(self, id, nombre_usuario, contrasena, correo, historial_eventos=None):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.correo = correo
        self.historial_eventos = historial_eventos or []

    def guardar_en_json(self, archivo_json):
        try:
            with open(archivo_json, "r") as archivo:
                usuarios = json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            usuarios = []

        usuarios.append(self.to_json())

        with open(archivo_json, "w") as archivo:
            json.dump(usuarios, archivo)

    @staticmethod
    def from_json(data):
        try:
            return Usuario(
                data["id"],
                data["nombre_usuario"],
                data["contrasena"],
                data["correo"],
                data.get("historial_eventos", [])  # Use data.get() to handle missing key
            )
        except KeyError as e:
            raise ValueError(f"El objeto JSON no tiene la clave requerida: {e}")

    def to_json(self):
        return {
            "id": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "contrasena": self.contrasena,
            "correo": self.correo,
            "historial_eventos": self.historial_eventos
        }

    @staticmethod
    def cargar_desde_json(archivo_json):
        try:
            with open(archivo_json, "r") as archivo:
                datos_usuarios = json.load(archivo)
                usuarios = [Usuario.from_json(datos) for datos in datos_usuarios]
        except (FileNotFoundError, json.JSONDecodeError):
            usuarios = []
        return usuarios


