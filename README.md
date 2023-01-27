# gencode

Ce script python génère un mot de passe d'une longueur et d'un niveau de complexité spécifiés par l'utilisateur. L'utilisateur peut choisir de saisir son propre mot de passe ou d'en faire générer automatiquement par le script. Le mot de passe généré est enregistré dans un fichier texte avec le nom du site Web auquel il est destiné. Il utilise également le module Fernet du package de cryptographie pour le cryptage et le décryptage, ainsi que le module secrets pour générer des caractères aléatoires pour le mot de passe.

Ceci est mon premier gros projet en python soiyer indulgent

Pour utilisé ce programme il vous faudras le module ``cryptographie``:


    $ pip install cryptography
