import json
import tkinter as tk
from tkinter import messagebox
from ProyectoTourMusical.entidades.usuarios import Usuario, cargar_usuarios_desde_json

def mostrar_pantalla_inicio():
    ventana_inicio = tk.Tk()
    ventana_inicio.title("Tour Musical - Inicio")
    ventana_inicio.geometry("400x300")

    def iniciar_sesion():
        usuarios = cargar_usuarios_desde_json()

        nombre_usuario = entry_nombre_usuario.get()
        contrasena = entry_contrasena.get()

        for usuario in usuarios:
            if usuario.nombre_usuario == nombre_usuario and usuario.contrasena == contrasena:
                messagebox.showinfo("Inicio de Sesión", f"Bienvenido, {usuario.nombre_usuario}!")
                ventana_inicio.destroy()
                return

        messagebox.showerror("Error de Inicio de Sesión", "Nombre de usuario o contraseña incorrectos.")

    def registrarse():
        usuarios = cargar_usuarios_desde_json()

        siguiente_id_usuario = len(usuarios) + 1
        nombre_usuario = entry_nombre_usuario.get()
        contrasena = entry_contrasena.get()
        correo = entry_correo.get()

        nuevo_usuario = Usuario(siguiente_id_usuario, nombre_usuario, contrasena, correo, [])
        usuarios.append(nuevo_usuario)

        with open("ProyectoTourMusical/data/usuarios.json", "w") as archivo_json:
            usuarios_data = [usuario.to_json() for usuario in usuarios]
            json.dump(usuarios_data, archivo_json)

        messagebox.showinfo("Registro", "Usuario registrado exitosamente.")

    label_bienvenida = tk.Label(ventana_inicio, text="Bienvenido a Tour Musical", font=("Arial", 16, "bold"))
    label_bienvenida.pack(pady=20)

    label_nombre_usuario = tk.Label(ventana_inicio, text="Nombre de usuario:")
    label_nombre_usuario.pack()

    entry_nombre_usuario = tk.Entry(ventana_inicio)
    entry_nombre_usuario.pack()

    label_contrasena = tk.Label(ventana_inicio, text="Contraseña:")
    label_contrasena.pack()

    entry_contrasena = tk.Entry(ventana_inicio, show="*")
    entry_contrasena.pack()

    label_correo = tk.Label(ventana_inicio, text="Correo:")
    label_correo.pack()

    entry_correo = tk.Entry(ventana_inicio)
    entry_correo.pack()

    btn_iniciar_sesion = tk.Button(ventana_inicio, text="Iniciar Sesión", command=iniciar_sesion)
    btn_iniciar_sesion.pack(pady=10)

    btn_registrarse = tk.Button(ventana_inicio, text="Registrarse", command=registrarse)
    btn_registrarse.pack(pady=10)

    ventana_inicio.mainloop()

mostrar_pantalla_inicio()
