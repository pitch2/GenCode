from cryptography.fernet import Fernet


with open('unlock.key', 'rb') as unlock:
     key = unlock.read()



def cryptage():
    f = Fernet(key)
    with open('vosmotsdepasse.txt', 'rb') as original_file:
        original = original_file.read()
    encrypted = f.encrypt(original)
    with open ('vmpd_crypté.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decryptage():
    f = Fernet(key)
    with open('vmpd_crypté.txt', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = f.decrypt(encrypted)
    with open('vosmotsdepasse.txt', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)







