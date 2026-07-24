"""
Punto de entrada de la aplicación.
Inicializa la configuración visual de CustomTkinter y lanza
la vista de inicio de sesión como ventana principal.
"""
import customtkinter as ctk
from views.login_view import LoginView


def main() -> None:
    """Configura la apariencia de la app y arranca el flujo desde LoginView."""
    ctk.set_appearance_mode("light")
    app = LoginView()
    app.mainloop()


if __name__ == "__main__":
    main()
    