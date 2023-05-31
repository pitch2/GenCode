import os


def main():
    choix = input("Que voulez-vous faire? \n1 - Générer un nouveau mot de passe\n2 - Lire mes mots de passe\nChoix: ")
    if choix == "1":
        generer_mot_de_passe()
    elif choix == "2":
        lire_mots_de_passes()
    else:
        print("Erreur: choix invalide.")

def generer_mot_de_passe():
    site = input("Site: ")
    identifiant = input("Identifiant: ")
    mot_de_passe = input("Mots de passe: ")
    print("Le mot de passe généré est:", mot_de_passe)
    with open("mots_de_passes.txt", "a") as f:
        f.write("\nSite: " + site + "\nIdentifiant: " + identifiant + "\nMot de passe: " + mot_de_passe + "\n\n")

def lire_mots_de_passes():
    global choix_type
    choix = input("Que voulez-vous faire? \n1 - Lire tous les mots de passe\n2 - Chercher une information en particulier\nChoix: ")
    if choix == "1":
        with open("mots_de_passes.txt", "r") as f:
            print(f.read())

    elif choix == "2":
        print("1 - Avec le nom du site\n2 - Avec un nom d'utilisateur\n3 - Avec un nom mot de passe")
        choix_type = int(input("Choix: "))

        # Pour trouver avec le site
        if choix_type==1:
            site = input("Site: ")
            with open("mots_de_passes.txt", "r") as f:
                lignes = f.readlines()
            codes = []
            for i, ligne in enumerate(lignes):
                if ligne.startswith("Site:"):
                    nom_site = ligne.strip().split(':')[1].strip()
                    if nom_site == site:
                        identifiant = lignes[i+1].strip().split(':')[1].strip()
                        mdp = lignes[i+2].strip().split(':')[1].strip()
                        codes.append((identifiant, mdp))
            if len(codes) == 0:
                print("Aucun mot de passe trouvé pour ce site.")
            else:
                print(f"L'identifiant est {identifiant}")
                for nom_site, mdp in codes:
                    print(f"pour le site {nom_site} avec commme mot de passe {mdp}")
        

        # Pour trouver avec l'id
        if choix_type==2:
            nom_utilisateur = input("Nom utilisateur: ")
            with open("mots_de_passes.txt", "r") as f:
                lignes = f.readlines()
            codes = []
            for i, ligne in enumerate(lignes):
                if ligne.startswith("Identifiant:"):
                    identifiant = ligne.strip().split(':')[1].strip()
                    if identifiant == nom_utilisateur:
                        nom_site = lignes[i-1].strip().split(':')[1].strip()
                        mdp = lignes[i+1].strip().split(':')[1].strip()
                        codes.append((nom_site, mdp))
            if len(codes) == 0:
                print("Aucun mot de passe trouvé pour cet identifiant.")
            else:
                print(f"L'identifiant est {identifiant}")
                for nom_site, mdp in codes:
                    print(f"pour le site {nom_site} avec commme mot de passe {mdp}")


        # Pour trouver avec le mdp
        if choix_type==3:
            mdp = input("Mot de passe: ")
            with open("mots_de_passes.txt", "r") as f:
                lignes = f.readlines()
            codes = []
            for i, ligne in enumerate(lignes):
                if ligne.startswith("Mot de passe:"):
                    mot_de_passe = ligne.strip().split(':')[1].strip()
                    if mot_de_passe == mdp:
                        nom_site = lignes[i-2].strip().split(':')[1].strip()
                        identifiant = lignes[i-1].strip().split(':')[1].strip()
                        codes.append((nom_site, identifiant))
            if len(codes) == 0:
                print("Aucun mot de passe trouvé pour ce mot de passe.")
            else:
                print(f"L'identifiant est {identifiant} pour le site {nom_site} avec commme mot de passe {mdp}")


def init():
    f = open("mots_de_passes.txt", "w+")
    f.write("1")
    f.close()



open("mots_de_passes.txt", "w").close()  # creates an empty file
main()
