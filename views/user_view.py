import tkinter as tk
from tkinter import ttk
import json

class UserView(tk.Frame):
    def __init__(self, master, show_main_view):
        super().__init__(master)
        self.show_main_view = show_main_view
        
        # Crear y configurar los widgets de la vista de usuarios
        label = tk.Label(self, text="Lista de Usuarios", font=("Roboto Condensed", 16))
        label.pack(pady=10)

        self.users_list = ttk.Treeview(self, columns=("ID", "Nombre", "Apellido"), show="headings")
        self.users_list.heading("ID", text="ID")
        self.users_list.heading("Nombre", text="Nombre")
        self.users_list.heading("Apellido", text="Apellido")
        self.users_list.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        self.load_users()
        
        back_button = tk.Button(self, text="Volver al Menú Inicial", command=self.show_main_view)
        back_button.pack(pady=10)

    # Cargar usuarios desde el archivo JSON
    def load_users(self):
        with open("data/users.json", "r") as json_file:
            users = json.load(json_file)

        for user in users:
            self.users_list.insert("", "end", values=(user["id"], user["nombre"], user["apellido"]))

    
def show_main_view():
    user_view.pack_forget()
    main_view.pack(fill=tk.BOTH, expand=True)



if __name__ == "__main__":
    root = tk.Tk()

    user_view = UserView(root, show_main_view)
    user_view.pack(fill=tk.BOTH, expand=True)

    main_view = MainView(root, show_user_view)
    
    root.mainloop()