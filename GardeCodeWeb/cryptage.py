import os
from cryptography.fernet import Fernet

# Fonction pour obtenir la clé de chiffrement/déchiffrement
def get_key():
    key_file = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "key.key")
    try:
        with open(key_file, "rb") as f:
            key = f.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)
    return key

# Fonction pour chiffrer un texte et l'ajouter à un fichier de sortie
def encrypt_file(text, file_name):
    key = get_key()
    f = Fernet(key)

    # Ouvre le fichier de sortie en mode "ajout binaire" ("ab")
    with open(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), file_name), "ab") as f_out:
        # Si le fichier de sortie n'est pas vide, ajoute un délimiteur (une nouvelle ligne) avant d'écrire le texte chiffré
        if os.path.getsize(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), file_name)) != 0:
            f_out.write(b"\n")
        # Chiffre le texte en utilisant la clé, puis écrit le texte chiffré dans le fichier de sortie
        text_to_write = f.encrypt(text.encode())
        f_out.write(text_to_write)




# Fonction pour déchiffrer un fichier chiffré et écrire le texte en clair dans un fichier de sortie
def decrypt_file(encrypted_file_name, decrypted_file_name):
    key = get_key()
    f = Fernet(key)

    # Ouvre le fichier chiffré en mode "lecture binaire" ("rb"), puis lit le contenu dans une variable
    with open(os.path.join(os.path.dirname(__file__), "../", encrypted_file_name), "rb") as f_in:
        encrypted_text = f_in.read()

    # Sépare le contenu en plusieurs textes chiffrés en utilisant le délimiteur approprié (une nouvelle ligne)
    encrypted_texts = encrypted_text.split(b"\n")

    # Récupère le chemin absolu du dossier parent
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

    # Ouvre le fichier de sortie en mode "ajout" ("a"), puis écrit le texte déchiffré dans le fichier
    with open(os.path.join(parent_dir, decrypted_file_name), "a") as f_out:
        for encrypted_text in encrypted_texts:
            # Déchiffre le texte chiffré en utilisant la clé, puis écrit le texte déchiffré dans le fichier de sortie
            decrypted_text = f.decrypt(encrypted_text).decode()
            f_out.write(decrypted_text)




# Fonction pour vider le contenu d'un fichier
def clear_file_content(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name), "w") as f:
        f.truncate(0)




# Exemple d'utilisation

#encrypt_file("coucouuuu\ngit\naaaa", "code_encrypted.txt")
#   
