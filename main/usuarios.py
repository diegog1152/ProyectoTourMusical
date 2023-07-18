import json

class Usuario:
    def __init__(self, id_usuario, nombre_usuario, contrasena, correo, historial_eventos):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.correo = correo
        self.historial_eventos = historial_eventos

    def guardar_en_json(self):
        usuario_data = {
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "contrasena": self.contrasena,
            "correo": self.correo,
            "historial_eventos": self.historial_eventos
        }

        # Abrir el archivo JSON y guardar los datos del usuario
        with open("usuarios.json", "a") as archivo_json:
            json.dump(usuario_data, archivo_json)
            archivo_json.write('\n')

    @staticmethod
    def cargar_usuarios_desde_json():
        usuarios = []
        try:
            with open("usuarios.json", "r") as archivo_json:
                for linea in archivo_json:
                    usuario_data = json.loads(linea)
                    usuario = Usuario(
                        usuario_data["id_usuario"],
                        usuario_data["nombre_usuario"],
                        usuario_data["contrasena"],
                        usuario_data["correo"],
                        usuario_data["historial_eventos"]
                    )
                    usuarios.append(usuario)
        except FileNotFoundError:
            # Si el archivo no existe, retorna una lista vacía
            return []
        return usuarios

def registrar_usuario():
    usuarios = Usuario.cargar_usuarios_desde_json()

    siguiente_id_usuario = len(usuarios) + 1
    nombre_usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")
    correo = input("Correo: ")

    usuario = Usuario(siguiente_id_usuario, nombre_usuario, contrasena, correo, [])
    usuario.guardar_en_json()

    print("Usuario registrado exitosamente. ID de usuario:", siguiente_id_usuario)

def autenticar_usuario():
    usuarios = Usuario.cargar_usuarios_desde_json()

    nombre_usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")

    for usuario in usuarios:
        if usuario.nombre_usuario == nombre_usuario and usuario.contrasena == contrasena:
            print("Inicio de sesión exitoso.")
            return usuario

    print("Nombre de usuario o contraseña incorrectos.")
    return None
