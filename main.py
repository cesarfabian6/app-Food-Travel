import tkinter as tk
from tkinter import font
from tkinter import ttk
import random
import datetime

# Importar las vistas personalizadas
from views.activities_view import ActivitiesView
from views.destinations_view import DestinationsView
from views.route_view import RouteView
from views.user_view import UserView
from views.main_view import MainView

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurar la tipografía y colores
        self.configure_typography()
        self.configure_colors()

        # Configurar estilo ttk
        self.style = ttk.Style()

        # Configurar la ventana principal
        self.title("Foodie Tour App")
        self.geometry("800x600")

        # Crear los botones de navegación
        self.create_navigation_buttons()

        # Mostrar la vista principal al inicio
        self.show_main_view()

    def configure_typography(self):
        self.default_font = tk.font.nametofont("TkDefaultFont")
        self.default_font.configure(family="Open Sans")
        self.option_add("*Font", self.default_font)

        self.header_font = tk.font.Font(family="Roboto Condensed", size=16, weight="bold")
        self.title_font = tk.font.Font(family="Open Sans", size=14, weight="bold")

    def configure_colors(self):
        self.primary_color = "#FF5722"
        self.secondary_color = "#607D8B"
        self.accent_color = "#4CAF50"
        self.background_color = "#EEEEEE"

        self.configure(bg=self.background_color)

    def create_navigation_buttons(self):
        self.navigation_frame = tk.Frame(self, bg=self.primary_color)
        self.navigation_frame.pack(fill=tk.X, padx=10, pady=5)

        self.activities_button = tk.Button(self.navigation_frame, text="Ver Actividades", command=self.show_activities_view)
        self.activities_button.pack(side=tk.LEFT, padx=5)

        self.destinations_button = tk.Button(self.navigation_frame, text="Ver Destinos", command=self.show_destinations_view)
        self.destinations_button.pack(side=tk.LEFT, padx=5)

        self.route_button = tk.Button(self.navigation_frame, text="Ver Rutas", command=self.show_route_view)
        self.route_button.pack(side=tk.LEFT, padx=5)

        self.user_button = tk.Button(self.navigation_frame, text="Ver Usuario", command=self.show_user_view)
        self.user_button.pack(side=tk.LEFT, padx=5)

    def show_main_view(self):
        self.clear_current_view()
        self.main_label = tk.Label(self, text="Bienvenido a Foodie Tour App", font=self.header_font, bg=self.background_color)
        self.main_label.pack(pady=20)
    
    def show_activities_view(self):
        self.clear_current_view()
        self.activities_view = ActivitiesView(self)
        self.activities_view.pack(fill=tk.BOTH, expand=True)
        self.activities_view.show_main_view(self)  # Pasar la instancia de ActivitiesView
    
    def show_destinations_view(self):
        self.clear_current_view()
        self.destinations_view = DestinationsView(self)
        self.destinations_view.pack(fill=tk.BOTH, expand=True)

    def show_route_view(self):
        self.clear_current_view()
        self.route_view = RouteView(self, self.show_main_view)
        self.route_view.pack(fill=tk.BOTH, expand=True)

    def show_user_view(self):
        self.clear_current_view()
        self.user_view = UserView(self, self.show_main_view)  # Pasa el argumento show_main_view aquí
        self.user_view.pack(fill=tk.BOTH, expand=True)

    def clear_current_view(self):
        for widget in self.winfo_children():
            if widget != self.navigation_frame:
                widget.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()