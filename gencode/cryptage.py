from cryptography.fernet import Fernet




with open('unlock.key', 'rb') as unlock:
     key = unlock.read()
print(key)


def cryptage():
     f = Fernet(key)
     with open('mdp.txt', 'rb') as original_file:
          original = original_file.read()
     encrypted = f.encrypt(original)
     with open ('motdepasse.txt', 'wb') as encrypted_file:
          encrypted_file.write(encrypted)
     with open("mdp.txt", "w") as file:
            file.truncate()

def decryptage():
    f = Fernet(key)
    with open('motdepasse.txt', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = f.decrypt(encrypted)
    with open('mdp.txt', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    with open("motdepasse.txt", "w") as file:
        file.truncate()


####


def cryptage_first():
    f = Fernet(key)
    with open('mdp.txt', 'rb') as original_file:
        original = original_file.read()
    encrypted = f.encrypt(original)
    with open ('mdp_archive.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    with open("mdp.txt", "w") as file:
        file.truncate()


def decryptage_first():
    f = Fernet(key)
    with open('mdp_archive.txt', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = f.decrypt(encrypted)
    with open('mdp.txt', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    with open("mdp_archive.txt", "w") as file:
        file.truncate()



