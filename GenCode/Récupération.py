from cryptage import *

get_key()

def recup():
    print("Visionnage des mots de passes")

    decrypt_file("code_encrypted.txt", "mots_de_passes.txt")

recup()
