import json

class Usuario:
    def __init__(self, id_usuario, nombre_usuario, contrasena, correo, historial_eventos):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.correo = correo
        self.historial_eventos = historial_eventos

    def to_json(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "contrasena": self.contrasena,
            "correo": self.correo,
            "historial_eventos": self.historial_eventos
        }

    @classmethod
    def from_json(cls, data):
        return cls(
            data["id_usuario"],
            data["nombre_usuario"],
            data["contrasena"],
            data["correo"],
            data["historial_eventos"]
        )

    @staticmethod
    def cargar_desde_json(fuente_datos):
        usuarios = []
        try:
            with open(fuente_datos, "r") as archivo_json:
                usuarios_data = json.load(archivo_json)
                for usuario_data in usuarios_data:
                    usuario = Usuario.from_json(usuario_data)
                    usuarios.append(usuario)
        except FileNotFoundError:
            return []
        return usuarios

    def guardar_en_json(self, fuente_datos):
        with open(fuente_datos, "a") as archivo_json:
            json.dump(self.to_json(), archivo_json)
            archivo_json.write('\n')

