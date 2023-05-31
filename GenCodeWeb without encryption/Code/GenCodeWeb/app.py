import secrets
import string
import pyperclip
from flask import Flask, render_template, request
import os
import webbrowser
url = "http://127.0.0.1:5000"
webbrowser.open(url)


parent_directory = os.path.dirname(os.getcwd())  # Obtenir le chemin du répertoire parent
file_path = os.path.join(parent_directory, "mots_de_passes.txt")  # Chemin complet du fichier dans le répertoire parent

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_password():
    nom_site = request.form['nom_site']
    id = request.form['id']
    choix = int(request.form['choix'])
    long = int(request.form['long'])

    pwd = ''

    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    lds = letters + digits + special_chars
    ld = letters + digits
    ds = digits + special_chars
    ls = letters + special_chars
    l = letters
    d = digits
    s = special_chars

    if long>=9:
        print("Le mot de passe est fort")
    elif long<=9:
        if long>=7:
            print("Le mot de passe est assez complexe mais pas suffissant")
        elif long<=6:
            print("Le mot de passe est faible")
    else:
        return "Le mot de passe doit contenir au moins 1 caractère et être d'une longueur maximale de 30 caractères"

    for _ in range(long):
        if choix ==1:
            pwd += ''.join(secrets.choice(lds))
        elif choix ==2:
            pwd +=''.join(secrets.choice(ls))
        elif choix ==3:
            pwd +=''.join(secrets.choice(ds))        
        elif choix ==4:
            pwd +=''.join(secrets.choice(ld))   
        elif choix ==5:
            pwd +=''.join(secrets.choice(l))   
        elif choix ==6:
            pwd +=''.join(secrets.choice(d))      
        elif choix ==7:
            pwd +=''.join(secrets.choice(s))   
        else:
            return "Choix invalide"

    informations = f"\nSite: {nom_site} \nIdentifiant: {id}\nMot de passe: {pwd}"
    with open(file_path, "a") as file:
        file.write(informations)

    pyperclip.copy(pwd)

    return f"Le mot de passe pour {nom_site} est {pwd} et a été copié dans le presse-papiers"



if __name__ == '__main__':
    app.run()


if __name__ == '__main__':
    app.run(debug=True)

