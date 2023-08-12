import tkinter as tk
from tkinter import ttk
import folium
from folium.plugins import Search
import webbrowser

class RouteView(tk.Frame):
    def __init__(self, master, show_main_view):
        super().__init__(master)
        self.show_main_view = show_main_view

        self.configure_typography()
        self.configure_colors()

        self.create_widgets()

    def configure_typography(self):
        self.heading_font = ("Roboto Condensed", 16, "bold")
        self.text_font = ("Open Sans", 12)

    def configure_colors(self):
        self.primary_color = "#FF5722"
        self.secondary_color = "#607D8B"
        self.accent_color = "#4CAF50"
        self.background_color = "#EEEEEE"
        self.style = ttk.Style()
        self.style.configure("Custom.TLabel", background=self.background_color, foreground=self.primary_color)
        self.master.configure(bg=self.background_color)

    def create_widgets(self):
        label = ttk.Label(self, text="Planificación de Visitas", font=self.heading_font, style="Custom.TLabel")
        label.pack(pady=20)

        self.route_name_label = ttk.Label(self, text="Nombre de la Ruta:", font=self.text_font)
        self.route_name_label.pack()

        self.route_name_entry = ttk.Entry(self, font=self.text_font)
        self.route_name_entry.pack()

        self.destinations_label = ttk.Label(self, text="Destinos:", font=self.text_font)
        self.destinations_label.pack()

        self.destinations_listbox = tk.Listbox(self, font=self.text_font, selectmode=tk.MULTIPLE)
        # ... Agregar destinos a la lista ...

        self.destinations_listbox.pack()
        # Botón para abrir el mapa
        open_map_button = tk.Button(self, text="Abrir Mapa", command=self.open_map)
        open_map_button.pack()

        self.create_route_button = ttk.Button(self, text="Crear Ruta", command=self.create_route)
        self.create_route_button.pack(pady=10)

        back_button = tk.Button(self, text="Volver al Menú Inicial", command=self.master.show_main_view, bg=self.primary_color, fg="white")
        back_button.pack(pady=10)
        
    def create_route(self):
        # Implementar la lógica para crear la ruta aquí
        pass
        
        # Crear un mapa usando folium
        self.map = folium.Map(location=[-24.785424608907356, -65.41586729846487], zoom_start=15)
        
        # Crear el complemento de búsqueda y agregarlo al mapa
        search = Search(layer=self.map, geom_type='Point', placeholder='Buscar lugares...')
        self.map.add_child(search)

    def open_map(self):
        # Abrir el mapa en el navegador web
        self.map.save('map.html')
        webbrowser.open('map.html')

        # Guardar el mapa como archivo HTML
        map.save("map.html")

        # Abrir el archivo HTML en el navegador web
        webbrowser.open("map.html")

if __name__ == "__main__":
    root = tk.Tk()
    route_view = RouteView(root, None)
    route_view.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
