import secrets
import string
import tkinter as tk

from cryptage import *
from tkinter import messagebox

get_key()


def lancer():
    def generateur(nbrdecar):
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation
        lds = letters + digits + special_chars
        
        password = ''.join(secrets.choice(lds) for i in range(nbrdecar))
        return password

    def ecriture(site, id, password):
        informations = f"\nSite: {site} \nIdentifiant: {id}\nMot de passe: {password}"
        encrypt_file(informations, "code_encrypted.txt")


    def copie():
        site = site_entry.get()
        id = id_entry.get()
        nbrdecar = int(nbr_entry.get())
        password = generateur(nbrdecar)
        ecriture(site, id, password)
        result_label.config(text=f"\nSite: {site} | Identifiant: {id} | Mot de passe: {password}")
        messagebox.showinfo("GenCode", "Mot de passe copié")
        
    root = tk.Tk()
    root.title("GenCodeLite")

    site_label = tk.Label(root, text="Site:")
    site_label.grid(row=0, column=0, pady=10, padx=10)

    site_entry = tk.Entry(root)
    site_entry.grid(row=0, column=1, pady=10, padx=10)

    nbr_label = tk.Label(root, text="Longueur:")
    nbr_label.grid(row=1, column=0, pady=10, padx=10)

    nbr_entry = tk.Entry(root)
    nbr_entry.grid(row=1, column=1, pady=10, padx=10)

    id_label = tk.Label(root, text="Identifiant:")
    id_label.grid(row=2, column=0, pady=10, padx=10)

    id_entry = tk.Entry(root)
    id_entry.grid(row=2, column=1, pady=10, padx=10)

    generate_button = tk.Button(root, text="Générer et copié", command=copie)
    generate_button.grid(row=3, column=0, columnspan=2, pady=10)

    result_label = tk.Label(root, text="")
    result_label.grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()


lancer()
