import secrets
import string
from cryptography.fernet import Fernet
from cry.cryptage import *

key = Fernet.generate_key()
with open('unlock.key', 'wb') as unlock:
    unlock.write(key)
    


letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

lds = letters + digits + special_chars
d=digits

def neto():
    with open("vosmotsdepasse.txt", "w") as file:
        file.truncate()



def premier_demarrage():
    pwd=''
    print("Bonjour, pour utilisé le service GenCode vous devez passer par cette étape\n\n")
    print("Voulez-vous initialisé le service\n")
    print("1-Oui")
    print("2-Non")
    print("3-Je désire des informations")

    choix_creation=int(input("Saisir votre choix: "))

    if choix_creation==1:

        '''
        f =open("mdp_archive.txt", "x")
        f.close
        '''

        f =open("vosmotsdepasse.txt", "x")
        f.close


        f =open("vmpd_crypté.txt", "x")
        f.close

        f = open("vosmotsdepasse.txt", "a")
        f.write("------------------------------------------")
        f.close()
        cryptage()
        neto()

        print("Si vous avez des problèmes au niveau du l'utilisation vous pouvez allez voir dans le fichier web intitulé 'Programme d’assistance  GenCode'")    
        print("L'initialisation du service est faite, vous pouvez fermer la console, et supprimé ce programme vous pouvez desormais utlise GenCode")
        
    elif choix_creation==2:
        print("A bientôt")
        print("------------------------------------------------------------------------------------")
        return premier_demarrage()
        
    elif choix_creation==3:
        print("Vous pouvez consulté la page Web 'Information et utilisation de GenCode'")
        print("------------------------------------------------------------------------------------")
        return premier_demarrage()
    
    else:
        print("Veuillez saisir 1,2 ou 3")
        print("------------------------------------------------------------------------------------")
        return premier_demarrage()


    '''
    print("Ensuite, pour lire vos mots de passe déja fais, vous devrez avoir ce code:")

    for _ in range(6):
        pwd += ''.join(secrets.choice(d))
    print(pwd)
    '''



premier_demarrage()



