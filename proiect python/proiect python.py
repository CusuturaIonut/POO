import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Clasa Carte pentru stocarea informatiilor despre carti
class Carte:
    def __init__(self, id_carte, titlu, autor):
        self.id_carte = id_carte
        self.titlu = titlu
        self.autor = autor

    def __str__(self):
        return f"ID: {self.id_carte}, Titlu: {self.titlu}, Autor: {self.autor}"

# Clasa Biblioteca pentru gestionarea cartilor
class Biblioteca:
    def __init__(self):
        self.carti = []

    def adauga_carte(self, carte):
        self.carti.append(carte)

    def sterge_carte(self, id_carte):
        for carte in self.carti:
            if carte.id_carte == id_carte:
                self.carti.remove(carte)
                return True
        return False

    def obtine_carti(self):
        return self.carti

# Clasa GUI pentru crearea ferestrei sistemului de management al bibliotecii
class SistemManagementBiblioteca:
    def __init__(self, root, biblioteca):
        self.biblioteca = biblioteca
        self.root = root
        self.root.title("Biblioteca online")
        self.root.geometry("600x970")  
        self.root.config(bg="#f4f6f9")  
        self.creeaza_widgeturi()

    def creeaza_widgeturi(self):
        # Font buton si eticheta
        font_style = ("Segoe UI", 12)
        header_font = ("Segoe UI", 14, "bold")

        # Fundal si text
        background_color = "#f4f6f9"  
        button_color = "#1f77b4"  
        button_hover_color = "#0d65a4"  
        label_color = "#34495e"  
        frame_color = "#ffffff"  

        # Adaugare carti
        self.frame_adauga_carte = tk.LabelFrame(self.root, text="Adaugă Carte", padx=20, pady=20, font=header_font, bg=frame_color)
        self.frame_adauga_carte.grid(row=0, column=0, padx=30, pady=20, sticky="nsew")

        self.id_carte_label = tk.Label(self.frame_adauga_carte, text="ID Carte:", font=font_style, fg=label_color, bg=frame_color)
        self.id_carte_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.id_carte_entry = tk.Entry(self.frame_adauga_carte, font=font_style, bg="white", fg="black", relief="solid", bd=1)
        self.id_carte_entry.grid(row=0, column=1, padx=10, pady=10)

        self.titlu_label = tk.Label(self.frame_adauga_carte, text="Titlu:", font=font_style, fg=label_color, bg=frame_color)
        self.titlu_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.titlu_entry = tk.Entry(self.frame_adauga_carte, font=font_style, bg="white", fg="black", relief="solid", bd=1)
        self.titlu_entry.grid(row=1, column=1, padx=10, pady=10)

        self.autor_label = tk.Label(self.frame_adauga_carte, text="Autor:", font=font_style, fg=label_color, bg=frame_color)
        self.autor_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.autor_entry = tk.Entry(self.frame_adauga_carte, font=font_style, bg="white", fg="black", relief="solid", bd=1)
        self.autor_entry.grid(row=2, column=1, padx=10, pady=10)

        self.adauga_carte_button = tk.Button(self.frame_adauga_carte, text="Adaugă Carte", font=font_style, bg=button_color, fg="white", activebackground=button_hover_color, relief="flat", command=self.adauga_carte)
        self.adauga_carte_button.grid(row=3, columnspan=2, pady=20)

        # Stergere carti
        self.frame_sterge_carte = tk.LabelFrame(self.root, text="Șterge Carte", padx=20, pady=20, font=header_font, bg=frame_color)
        self.frame_sterge_carte.grid(row=1, column=0, padx=30, pady=20, sticky="nsew")

        self.id_carte_sterge_label = tk.Label(self.frame_sterge_carte, text="ID Carte de șters:", font=font_style, fg=label_color, bg=frame_color)
        self.id_carte_sterge_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.id_carte_sterge_entry = tk.Entry(self.frame_sterge_carte, font=font_style, bg="white", fg="black", relief="solid", bd=1)
        self.id_carte_sterge_entry.grid(row=0, column=1, padx=10, pady=10)

        self.sterge_carte_button = tk.Button(self.frame_sterge_carte, text="Șterge Carte", font=font_style, bg=button_color, fg="white", activebackground=button_hover_color, relief="flat", command=self.sterge_carte)
        self.sterge_carte_button.grid(row=1, columnspan=2, pady=20)

        # Sectiunea pentru vizualizarea cartilor (Lista Cartilor)
        self.frame_lista_carti = tk.LabelFrame(self.root, text="Lista Cărților", padx=20, pady=20, font=header_font, bg=frame_color)
        self.frame_lista_carti.grid(row=2, column=0, padx=30, pady=20, sticky="nsew")

        # Treeview pentru lista cartilor
        self.treeview = ttk.Treeview(self.frame_lista_carti, columns=("ID", "Titlu", "Autor"), show="headings", selectmode="browse")
        self.treeview.grid(row=0, column=0, padx=10, pady=10)

        # Configuram coloanele din Treeview
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Titlu", text="Titlu")
        self.treeview.heading("Autor", text="Autor")

        self.treeview.column("ID", width=100, anchor="center")
        self.treeview.column("Titlu", width=200, anchor="w")
        self.treeview.column("Autor", width=150, anchor="w")

        # Adaugam un buton pentru a vedea lista de carti
        self.vezi_lista_button = tk.Button(self.frame_lista_carti, text="Actualizare lista carti", font=font_style, bg=button_color, fg="white", activebackground=button_hover_color, relief="flat", command=self.vezi_lista_carti)
        self.vezi_lista_button.grid(row=1, column=0, pady=10)

    def adauga_carte(self):
        try:
            id_carte = int(self.id_carte_entry.get())
            titlu = self.titlu_entry.get()
            autor = self.autor_entry.get()

            if not titlu or not autor:
                messagebox.showerror("Eroare", "Completează corect toate câmpurile.")
                return

            carte = Carte(id_carte, titlu, autor)
            self.biblioteca.adauga_carte(carte)

            # Curatam campurile dupa adaugarea cartii
            self.id_carte_entry.delete(0, tk.END)
            self.titlu_entry.delete(0, tk.END)
            self.autor_entry.delete(0, tk.END)

            messagebox.showinfo("Succes", f"Cartea '{titlu}' a fost adăugată cu succes!")
        except ValueError:
            messagebox.showerror("Eroare", "Te rog să introduci un ID valid pentru carte.")

    def sterge_carte(self):
        try:
            id_carte = int(self.id_carte_sterge_entry.get())
            if self.biblioteca.sterge_carte(id_carte):
                messagebox.showinfo("Succes", f"Cartea cu ID {id_carte} a fost ștearsă!")
                self.vezi_lista_carti()  # Actualizam lista dupa stergere
            else:
                messagebox.showerror("Eroare", f"Cartea cu ID {id_carte} nu există.")
            self.id_carte_sterge_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Eroare", "Te rog să introduci un ID valid pentru carte.")

    def vezi_lista_carti(self):
        # Curatam lista anterioara
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Adaugam noile carti in Treeview
        carti = self.biblioteca.obtine_carti()
        for carte in carti:
            self.treeview.insert("", "end", values=(carte.id_carte, carte.titlu, carte.autor))

# Rularea aplicatiei
if __name__ == "__main__":
    biblioteca = Biblioteca()
    root = tk.Tk()
    app = SistemManagementBiblioteca(root, biblioteca)
    root.mainloop()
