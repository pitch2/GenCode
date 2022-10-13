
liste=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
       'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



mot=['m','o','m','{','o']
mdpcrypt=' '

def crypt():
    mdpcrypt=''
    k=0
    n=0
    for _ in range (len(mot)):
        n=0
        for _ in range (len(liste)):
    
            if liste[n]==mot[k]:
                mdpcrypt = mdpcrypt + liste[n+6]
                n=n+1

            else:
                n=n+1
        k=k+1
    print(mdpcrypt)

mot2=['s','u','s','u']

def decrypt():
    motdecrypt=''
    k=0
    n=0
    for _ in range (len(mot2)):
        n=0
        for _ in range (len(liste)):
    
            if liste[n]==mot2[k]:
                motdecrypt = motdecrypt + liste[n-6]
                n=n+1

            else:
                n=n+1
        k=k+1
    print(motdecrypt)
