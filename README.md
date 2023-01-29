# GenCode

[Website](##)


Ce script python génère un mot de passe d'une longueur et d'un niveau de complexité spécifiés par l'utilisateur. L'utilisateur peut choisir de saisir son propre mot de passe ou d'en faire générer automatiquement par le script. Le mot de passe généré est enregistré dans un fichier texte avec le nom du site Web auquel il est destiné. 
Il utilise également le module Fernet du package de cryptographie pour le cryptage et le décryptage, ainsi que le module secrets pour générer des caractères aléatoires pour le mot de passe.

Pour utilisé ce programme il vous faudras le module ``cryptography`` ainsi que ``secret`` et ``string``:

    $ pip install cryptography
String et Secrets sont normalement installé avec python automatique :
*    [String](https://docs.python.org/fr/3/library/string.html)
*    [Secrets](https://docs.python.org/3/library/secrets.html)

---
    
#### Guide d'utilisation du module GenCode

**Initialisation**
*   Lancer le programme "Première_Utilisation".
*   Vous faites ```Oui``` ensuite, 3 fichiers seronts crée dans votre repertoire il y aura 
    *   vosmotsdepasse.txt
    *   vmpd_crypté.txt
    *   unlock.key
    *   vous ne devez pas toucher à ces 3 fichiers, sinon vous risquez de perdre toutes vos données
*   Vous pouvez fermer la/les fênetres

**Utilisation**
*   Vous pouvez maintenant lancer le programme "*GenCode*" ou "*GenCodeLite*".
    *   Le GenCode vous permet d'avoir tous les avantages du programme (visualisation des mots de passe crypté, choix de     complexité...)
    *   La version GenCodeLite vous permet d'allez vite dans la création de votre nouveau mot de passe. Deux question et il     est crée avec tous les caractères.
* Vous avez la posibilité de voir vos mots de passe enregistré, à la fin de la fin du programme, tous est indiqué.

**Problèmes**
Si vous avez des problèmes au moment de l'utilisation du programme un site à été pour tous les [problèmes](##).
Un programme est disponible pour récuperer tous les mots de passe dans un autre fichier.

