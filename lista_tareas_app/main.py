from servicios.tarea_servicio import TareaServicio
from servicios.auth_servicio import AuthServicio
from ui.app_tkinter import AppTareas
from ui.login_tkinter import VentanaLogin


def main():
    """
    Orquestador principal del sistema
    """

    auth = AuthServicio()
    servicio = TareaServicio()

    def iniciar():
        # Se ejecuta después del login
        app = AppTareas(servicio)
        app.mainloop()

    # Primero mostrar login
    login = VentanaLogin(auth, iniciar)
    login.mainloop()


if __name__ == "__main__":
    main()