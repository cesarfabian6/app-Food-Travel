import tkinter as tk
from tkinter import ttk

class MainView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        # Configurar la tipografía y los colores
        self.configure_typography()
        self.configure_colors()

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

        label = tk.Label(self, text="Menú Principal", font=("Roboto Condensed", 24), fg="#FF5722")
        label.pack(pady=20)
        
        activities_button = tk.Button(self, text="Ver Actividades", command=self.master.show_activities_view)
        activities_button.pack(pady=10)

    def show_activities_view(self):
        self.pack_forget()
        self.master.show_activities_view()
