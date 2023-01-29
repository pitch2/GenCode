import secrets
import string
from cryptage import *
#module perso


def neto():
    with open("vosmotsdepasse.txt", "w") as file:
        file.truncate()


def neto_mot():
    with open("vmpd_crypté.txt", "w") as file:
        file.truncate()

nom_site = input("Quel est le nom de votre site web? ")
nbrdecar = int(input("Nombre de caractère voulu: "))

def gencode_lite(nom_site ,nbrdecar ):
    cryptage()
    decryptage()
    neto_mot()

    pwd = ''
    

    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    lds = letters + digits + special_chars

    for _ in range(nbrdecar):
        pwd += ''.join(secrets.choice(lds))


    print("Le code de", nom_site, "est", pwd)

    f =open("vosmotsdepasse.txt" , "r")
    f.close()
    f = open("vosmotsdepasse.txt", "a")
    f.write("nom du site: "+str(nom_site))
    f.write(" | code: "+str(pwd))
    f.write("\nxxx\n")
    f.close()

    cryptage()
    neto()


gencode_lite(nom_site, nbrdecar)


