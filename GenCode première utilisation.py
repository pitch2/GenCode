class gencode():
    print("Bonjour, pour utilisé le service GenCode vous devez passer par cette étape")
    print("Voulez-vous initialisé le service")
    print("1-Oui")
    print("2-Non")
    print("3-Je désire des informations")

    choix_creation=int(input("Saisir votre choix: "))

    if choix_creation==1:
        f =open("mdp.txt" , "x")
        f.close
        f =open("mdp_hach.txt" , "x")
        f.close
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

