import os

print("Bienvenu dans AjoutCode")
parent_directory = os.path.dirname(os.getcwd())
file_path = os.path.join(parent_directory, "mots_de_passes.txt")  


for _ in range (99):
    nom_site = input("Le nom du site: ")
    id = input("Votre identifiant: ")
    pwd = input("Votre mot de passe: ")

    informations = f"\nSite: {nom_site} \nIdentifiant: {id}\nMot de passe: {pwd}\n"
    with open(file_path, "a") as file:
        file.write(informations)

    print("\n------------------------------\n")