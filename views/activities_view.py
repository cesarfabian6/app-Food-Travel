import tkinter as tk
from tkinter import ttk
import random
import datetime
import json

class ActivitiesView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.show_main_view = show_main_view
        
        # Configurar la tipografía y los colores
        self.configure_typography()
        self.configure_colors()
        
        # Crear y configurar los widgets de la vista de actividades
        label = tk.Label(self, text="Lista de Actividades", font=("Roboto Condensed", 16), fg=self.primary_color)
        label.pack(pady=10)

        self.activity_list = ttk.Treeview(self, columns=("ID", "Nombre", "Destino", "Hora Inicio"), show="headings", style="Custom.Treeview")
        self.activity_list.heading("ID", text="ID")
        self.activity_list.heading("Nombre", text="Nombre")
        self.activity_list.heading("Destino", text="Destino")
        self.activity_list.heading("Hora Inicio", text="Hora Inicio")
        self.activity_list.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.load_activities()

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

    def load_activities(self):
        try:
            with open("data/activities.json", "r") as json_file:
                activities = json.load(json_file)
                for activity in activities:
                    self.activity_list.insert("", "end", values=(activity["id"], activity["nombre"], activity["destino"], activity["hora_inicio"]))
        except FileNotFoundError:
            print("El archivo de actividades no se encontró.") 
    
def show_main_view():
    activities_view.pack_forget()
    main_view.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    activities_view = ActivitiesView(root)
    activities_view.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
