# GenCode

[Website](##)


Ce script python génère un mot de passe d'une longueur et d'un niveau de complexité spécifiés par l'utilisateur. L'utilisateur peut choisir de saisir son propre mot de passe ou d'en faire générer automatiquement par le script. Le mot de passe généré est enregistré dans un fichier texte avec le nom du site Web auquel il est destiné. 
Il utilise également le module Fernet du package de cryptographie pour le cryptage et le décryptage, ainsi que le module secrets pour générer des caractères aléatoires pour le mot de passe.

Pour utilisé ce programme il vous faudras le module ``cryptography`` ainsi que ``secret`` et ``string``, ``Pyperclip``:

    $ pip install cryptography
    $ pip install pyperclip
   
String et Secrets sont normalement installé avec python automatique :
*    [String](https://docs.python.org/fr/3/library/string.html)
*    [Secrets](https://docs.python.org/3/library/secrets.html)
*    [Pyperclip](https://pypi.org/project/pyperclip/)
*    [Cryptography](https://cryptography.io/en/latest/fernet/)

---
    
#### Guide d'utilisation du module GenCode


**Utilisation**
*   Vous pouvez maintenant lancer le programme "*GenCode*" ou "*GenCodeLite*".
    *   Le GenCode vous permet d'avoir tous les avantages du programme (visualisation des mots de passe crypté, choix de     complexité...)
    *   La version GenCodeLite vous permet d'allez vite dans la création de votre nouveau mot de passe. Deux question et il     est crée avec tous les caractères.
* Vous avez la posibilité de voir vos mots de passe enregistré, à la fin de la fin du programme, tous est indiqué.

**Problèmes**
Vous pouvez me contactez sur @pichon_adrien sur Instagram pour des potentielles problèmes.
Un programme est disponible pour récuperer tous les mots de passe dans un autre fichier : [lien](https://www.mediafire.com/file/1wc63o3lwlnpz2q/Récupération.py/file).
Vous devrez mettre ce fichier dans le même dossier que GenCode.




**Bug**
Aucun à connu pour l'instant


Ce module peut être connecté avec [GardeCode](https://github.com/pitch2/GardeCode) un autre module sur mon github 

###  Liste des prochaines features :

- [ ] Refaire readme de chacunes des parties

---

Les autres parties de GenCode : 

- [GenCode Web](https://github.com/pitch2/GenCodeWeb)
- [GardeCode](https://github.com/pitch2/GardeCode)
- [GenCodeLite](https://github.com/pitch2/GenCode) (intégré à GenCode)
- [GenCodePack](https://github.com/pitch2/GenCodePack) (regroupe tous les outils qui fonctionnes ensemble)


