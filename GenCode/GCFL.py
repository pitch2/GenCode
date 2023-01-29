
import secrets
import string
import tkinter as tk
import pyperclip
from cryptage import *
from tkinter import messagebox

with open('unlock.key', 'rb') as unlock:
     key = unlock.read()


def lancer():
    cryptage()
    decryptage()
    neto_mot()
    def generateur(nbrdecar):
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation
        lds = letters + digits + special_chars
        
        password = ''.join(secrets.choice(lds) for i in range(nbrdecar))
        return password

    def ecriture(site, password):
        f =open("vosmotsdepasse.txt" , "r")
        f.close()
        f = open("vosmotsdepasse.txt", "a")
        f.write("nom du site: "+str(site))
        f.write(" | code: "+str(password))
        f.write("\nxxx\n")
        f.close()
        
        #cryptage()
        #neto()

    def copie():
        site = site_entry.get()
        nbrdecar = int(nbr_entry.get())
        password = generateur(nbrdecar)
        ecriture(site, password)
        result_label.config(text=f"Site: {site} | Password: {password}")
        pyperclip.copy(password)
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

    generate_button = tk.Button(root, text="Générer et copié", command=copie)
    generate_button.grid(row=2, column=0, columnspan=2, pady=10)

    result_label = tk.Label(root, text="")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()


def neto():
    with open("vosmotsdepasse.txt", "w") as file:
        file.truncate()


def neto_mot():
    with open("vmpd_crypté.txt", "w") as file:
        file.truncate()
