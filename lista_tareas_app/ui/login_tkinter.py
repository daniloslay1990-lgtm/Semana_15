import tkinter as tk
from tkinter import messagebox


class VentanaLogin(tk.Tk):
    """
    Ventana de inicio de sesión
    """

    def __init__(self, auth_servicio, on_success):
        super().__init__()
        self.auth_servicio = auth_servicio
        self.on_success = on_success

        self.title("Inicio de Sesión")
        self.geometry("300x200")

        # Centrar ventana
        self.eval('tk::PlaceWindow . center')

        self._ui()

    def _ui(self):
        # Campo usuario
        tk.Label(self, text="Usuario:").pack(pady=(20, 5))
        self.ent_user = tk.Entry(self)
        self.ent_user.pack()

        # Campo contraseña
        tk.Label(self, text="Contraseña:").pack(pady=5)
        self.ent_pass = tk.Entry(self, show="*")
        self.ent_pass.pack()

        # Botón login
        tk.Button(self, text="Ingresar", command=self._login).pack(pady=20)

    def _login(self):
        """
        Evento del botón login
        """
        user = self.ent_user.get()
        pwd = self.ent_pass.get()

        # Validar credenciales
        if self.auth_servicio.validar(user, pwd):
            self.destroy()       # cerrar login
            self.on_success()    # abrir app principal
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")