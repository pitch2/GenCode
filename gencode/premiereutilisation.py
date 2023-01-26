import secrets
import string
from cryptography.fernet import Fernet
from cryptage import *

key = Fernet.generate_key()
with open('unlock.key', 'wb') as unlock:
    unlock.write(key)
    


letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

lds = letters + digits + special_chars
d=digits

def neto():
    with open("mdp.txt", "w") as file:
        file.truncate()



def premier_demarrage():
    pwd=''
    print("Bonjour, pour utilisé le service GenCode vous devez passer par cette étape")
    print("Voulez-vous initialisé le service")
    print("1-Oui")
    print("2-Non")
    print("3-Je désire des informations")

    choix_creation=int(input("Saisir votre choix: "))

    if choix_creation==1:
        f =open("mdp_archive.txt", "x")
        f.close

        f =open("mdp.txt", "x")
        f.close

        f =open("motdepasse.txt", "x")
        f.close

        f = open("mdp.txt", "a")
        f.write("------------------------------------------")
        f.close()
        cryptage()
        neto()
        
        print("L'initialisation du service est faite, vous pouvez fermer la console, et supprimé ce programme vous pouvez desormais utlise GenCode")
        #--à completer (explication)--#
        
    elif choix_creation==2:
        print("A bientôt")
        
    elif choix_creation==3:
        print("Information concernant le programme:")
        #--à completer--#
        
    else:
        print("Veuillez saisir 1,2 ou 3")
        print("Veuillez relancer le script")


    print("Ensuite, pour lire vos mots de passe déja fais, vous devrez avoir ce code:")

    for _ in range(6):
        pwd += ''.join(secrets.choice(d))
    print(pwd)




premier_demarrage()



