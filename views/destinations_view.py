import tkinter as tk
from tkinter import ttk
import random
import json

class DestinationsView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        # Configurar la tipografía y los colores
        self.configure_typography()
        self.configure_colors()
        
        # Crear y configurar los widgets de la vista de destinos culinarios
        label = tk.Label(self, text="Lista de Destinos Culinarios", font=("Roboto Condensed", 16), fg=self.primary_color)
        label.pack(pady=10)
        
        self.destinations_tree = ttk.Treeview(self, columns=("ID", "Nombre", "Tipo de Cocina", "Popularidad"), show="headings")
        self.destinations_tree.heading("ID", text="ID")
        self.destinations_tree.heading("Nombre", text="Nombre")
        self.destinations_tree.heading("Tipo de Cocina", text="Tipo de Cocina")
        self.destinations_tree.heading("Popularidad", text="Popularidad")
        self.destinations_tree.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        self.load_destinations()
        
        back_button = tk.Button(self, text="Volver al Menú Inicial", command=self.master.show_main_view, bg=self.primary_color, fg="white")
        back_button.pack(pady=10)

    def configure_typography(self):
        # Cargar fuentes tipográficas
        self.master.option_add("*Font", ("Open Sans", 10))
        self.master.option_add("TButton", ("Open Sans", 12))
        self.master.option_add("TLabel", ("Roboto Condensed", 16))
        
    def configure_colors(self):
        self.primary_color = "#FF5722"
        self.secondary_color = "#607D8B"
        self.accent_color = "#4CAF50"
        self.background_color = "#EEEEEE"
        self.style = ttk.Style()
        self.style.configure("Custom.Treeview.Heading", font=("Roboto Condensed", 12))
        self.style.configure("Custom.Treeview", background=self.background_color, foreground=self.secondary_color)
        self.master.configure(bg=self.background_color)

    def load_destinations(self):
        # Cargar destinos culinarios desde el archivo JSON
        with open("data/destinations.json", "r") as json_file:
            destinations = json.load(json_file)
            
            for destination in destinations:
                self.destinations_tree.insert("", "end", values=(
                    destination["id"],
                    destination["nombre"],
                    destination["tipo_cocina"],
                    destination["popularidad"],
                    destination["imagen"]
                ))
    

if __name__ == "__main__":
    root = tk.Tk()
    destinations_view = DestinationsView(root)
    destinations_view.pack(fill=tk.BOTH, expand=True)
    root.mainloop()