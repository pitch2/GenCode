import secrets
import string

#module perso
from cryptage import *

with open('unlock.key', 'rb') as unlock:
     key = unlock.read()



def gencode():
    cryptage()
    decryptage()
    neto_mot()

    
    pwd = ''

    nom_site= input("Saisir le nom du site: ")

    print("Voulez-vous un code:")
    print("     1- de vous même")    
    print("     2- automatique")
    
    choix= int(input("Choix: "))
    
    if choix==1:

        pwd=input("Saisir le mdp :")
        
        f =open("vosmotsdepasse.txt" , "r")
        f.close()

        f = open("vosmotsdepasse.txt", "a")
        f.write("nom du site: "+str(nom_site))
        f.write(" | code: "+str(pwd))
        f.close()

        cryptage()
        neto()
        
    elif choix==2:
    
    

        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation
        
        lds = letters + digits + special_chars
        ld = letters + digits
        ds = digits + special_chars
        ls = letters + special_chars
        l = letters
        d = digits
        s = special_chars


    

        long = int(input("\nLongueur du mots de passe désiré: "))    

        if long>=9:
            print("Le mot de passe est fort")
        elif long<=9:
            if long>=7:
                print("Le mot de passe est assez complexe mais pas suffissant")
            elif long<=6:
                print("Le mot de passe est faible")
        else:
            return gencode()
        
        

        for _ in range(2):
            print("\n")
    
    
    
        if long>=1:
        
            print("1- Mots de passe avec, lettres, chiffres, caractères spéciaux ")
            print("2- Mots de passe avec, lettres, caractères spéciaux")
            print("3- Mots de passe avec, chiffres, caractères spéciaux")
            print("4- Mots de passe avec, lettres, chiffre")
            print("5- Mots de passe avec, lettres")
            print("6- Mots de passe avec, chiffres")
            print("7- Mots de passe avec, caractères spéciaux")
            
            for _ in range(2):
                print("\n")

            choix=int(input("Saisir le numéro du choix : "))
            
                
                
            
            for _ in range(long):
                if choix ==1:
                    pwd += ''.join(secrets.choice(lds))
                    
                elif choix ==2:
                    pwd +=''.join(secrets.choice(ls))

                elif choix ==3:
                    pwd +=''.join(secrets.choice(ds))        

                elif choix ==4:
                    pwd +=''.join(secrets.choice(ld))   
                    
                elif choix ==5:
                    pwd +=''.join(secrets.choice(l))   
            
                elif choix ==6:
                    pwd +=''.join(secrets.choice(d))      

                elif choix ==7:
                    pwd +=''.join(secrets.choice(s))   
                    
                                
                else:
                    for _ in range(10):
                        print("| | | | | | | |")
                    return gencode()
            
            print(pwd)
            

        else:
            print("Le nombre de caractères doit être supérieur ou égale à 1")
            for _ in range(10):
                print("| | | | | | | |")
            return gencode()
        
        

        f =open("vosmotsdepasse.txt" , "r")
        f.close()

        f = open("vosmotsdepasse.txt", "a")
        f.write("nom du site: "+str(nom_site))
        f.write(" | code: "+str(pwd))
        f.write("\nxxx\n")
        f.close()

        cryptage()
        neto()



    else:
        print("Le choix doit 1 ou 2")
        for _ in range(10):
            print("| | | | | | | |")
        return gencode()        

    for _ in range(3):
        print("\n")
    print("Le code ainsi que le nom du site on été ecris dans le fichier mdp \n")
    print("Voulez vous resaisir un code ?")
    print("     1-Oui")
    print("     2-Non")
    print("     3-Information sur le code et autre")    
    print("     4-Je veux lire tous mes mots de passe")
    choix_cont=int(input("Votre choix: "))
    if choix_cont==1:
        return gencode()

    elif choix_cont==2:
        print("A bientôt")

    elif choix_cont==3:
        print("...")
        #--à completer--#


    elif choix_cont==4:
        print("Vos mots de passe sont dans le fichier vosmotsdepasse.txt ")
        print("Pour le bon fonctionnement du programmme, et pour la sécurité de vos mots de passe, nous devons resécurisé vos mots de passe")
        print("     1-J'ai fini")
        choix_cryptage_fin=int(input("Votre choix : "))
        if choix_cryptage_fin==1:
            neto()
            print("A bientôt")
    else:
        print("A bientôt")
        neto()

 

def neto():
    with open("vosmotsdepasse.txt", "w") as file:
        file.truncate()


def neto_mot():
    with open("vmpd_crypté.txt", "w") as file:
        file.truncate()

