import secrets
import string
import pyperclip
from flask import Flask, render_template, request
from cryptage import *
import webbrowser
url = "http://127.0.0.1:5000"
webbrowser.open(url)


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
    encrypt_file(informations, "code_encrypted.txt")

    pyperclip.copy(pwd)

    return f"Le mot de passe pour {nom_site} est {pwd} et a été copié dans le presse-papiers"


@app.route('/passwords')
def view_passwords():
    decrypt_file("code_encrypted.txt", "code_visibles.txt")
    with open('code_visibles.txt', 'r') as f:
        passwords = f.read()
    clear_file_content("code_visibles.txt")
    return passwords

if __name__ == '__main__':
    app.run()


if __name__ == '__main__':
    app.run(debug=True)



