from cryptography.fernet import Fernet

key = Fernet.generate_key()




def cryptage():
     f = Fernet(key)
     with open('pwd.txt', 'rb') as original_file:
          original = original_file.read()
     encrypted = f.encrypt(original)
     with open ('motdepasse.txt', 'wb') as encrypted_file:
          encrypted_file.write(encrypted)





def decryptage():
     f = Fernet(key)
     with open('motdepasse.txt', 'rb') as encrypted_file:
          encrypted = encrypted_file.read()
     decrypted = f.decrypt(encrypted)
     with open('motdepasse.txt', 'wb') as decrypted_file:
          decrypted_file.write(decrypted)





