usuarios = []
siguiente_id_usuario = 1

class Usuario:
    def __init__(self, id_usuario, nombre_usuario, contrasena, correo, historial_eventos):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.correo = correo
        self.historial_eventos = historial_eventos

def registrar_usuario():
    global siguiente_id_usuario
    nombre_usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")
    correo = input("Correo: ")
    usuario = Usuario(siguiente_id_usuario, nombre_usuario, contrasena, correo, [])
    usuarios.append(usuario)
    print("Usuario registrado exitosamente. ID de usuario:", siguiente_id_usuario)
    siguiente_id_usuario += 1

def autenticar_usuario():
    nombre_usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")
    for usuario in usuarios:
        if usuario.nombre_usuario == nombre_usuario and usuario.contrasena == contrasena:
            print("Inicio de sesión exitoso.")
            return usuario
    print("Nombre de usuario o contraseña incorrectos.")
    return None

def mostrar_informacion_usuario(usuario):
    print("Información del usuario:")
    print("ID de usuario:", usuario.id_usuario)
    print("Nombre de usuario:", usuario.nombre_usuario)
    print("Correo:", usuario.correo)
    print("Historial de eventos:", usuario.historial_eventos)