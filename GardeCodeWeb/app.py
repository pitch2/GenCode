from flask import Flask, render_template, request
import atexit
from cryptage import *
import os
import webbrowser
url = "http://127.0.0.1:5000"
webbrowser.open(url)

app = Flask(__name__)

decrypt_file("code_encrypted.txt", "mots_de_passes.txt")

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
file_path = os.path.join(parent_dir, "mots_de_passes.txt")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lire_mots_de_passes', methods=['POST'])
def lire_mots_de_passes():
    choix = request.form.get('choix')
    choix_type = int(request.form.get('choix_type'))

    if choix == "1":
        with open(file_path, "r") as f:
            passwords = f.read()
        return render_template('results.html', passwords=passwords)

    elif choix == "2":
        if choix_type == 1:
            site = request.form.get('site')
            with open(file_path, "r") as f:
                lines = f.readlines()
            codes = []
            for i, line in enumerate(lines):
                if line.startswith("Site:"):
                    nom_site = line.strip().split(':')[1].strip()
                    if nom_site == site:
                        identifiant = lines[i+1].strip().split(':')[1].strip()
                        mdp = lines[i+2].strip().split(':')[1].strip()
                        codes.append((identifiant, mdp))
            if len(codes) == 0:
                message = "Aucun mot de passe trouvé pour ce site."
                return render_template('results.html', message=message)
            else:
                return render_template('results.html', codes=codes)

        elif choix_type == 2:
            nom_utilisateur = request.form.get('nom_utilisateur')
            with open(file_path, "r") as f:
                lines = f.readlines()
            codes = []
            for i, line in enumerate(lines):
                if line.startswith("Identifiant:"):
                    identifiant = line.strip().split(':')[1].strip()
                    if identifiant == nom_utilisateur:
                        nom_site = lines[i-1].strip().split(':')[1].strip()
                        mdp = lines[i+1].strip().split(':')[1].strip()
                        codes.append((nom_site, mdp))
            if len(codes) == 0:
                message = "Aucun mot de passe trouvé pour cet identifiant."
                return render_template('results.html', message=message)
            else:
                return render_template('results.html', codes=codes)

        elif choix_type == 3:
            mdp = request.form.get('mdp')
            with open(file_path, "r") as f:
                lines = f.readlines()
            codes = []
            for i, line in enumerate(lines):
                if line.startswith("Mot de passe:"):
                    mot_de_passe = line.strip().split(':')[1].strip()
                    if mot_de_passe == mdp:
                        nom_site = lines[i-2].strip().split(':')[1].strip()
                        identifiant = lines[i-1].strip().split(':')[1].strip()
                        codes.append((nom_site, identifiant))
            if len(codes) == 0:
                message = "Aucun mot de passe trouvé pour ce mot de passe."
                return render_template('results.html', message=message)
            else:
                return render_template('results.html', codes=codes)
            

if __name__ == '__main__':
    app.run()
