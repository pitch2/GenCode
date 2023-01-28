from cryptography.fernet import Fernet

with open('unlock.key', 'rb') as unlock:
    key = unlock.read()

def recup():
    print("Récupération des mots de passe")
    print("Vos mots de passe seront enregistré dans le fichiers 'mesmotsdepasseexporte.txt")

    f =open("mesmotsdepasseexporte.txt", "x")
    f.close

    f = Fernet(key)
    with open('vmpd_crypté.txt', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = f.decrypt(encrypted)
    with open('mesmotsdepasseexporte.txt', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)


recup()
