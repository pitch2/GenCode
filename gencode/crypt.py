liste=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
       'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


mot =''
def demande():
    global mot
    mot=input("Saisir:")
    mot=list(mot.strip())
    print(mot)

mot=['m','o','m','8','~','o']


mdpcrypt=''
def crypt():
    global mot
    global mdpcrypt
    k=0
    n=0
    for _ in range (len(mot)):
        n=0
        for _ in range(len(liste)):
    
            if liste[n]==mot[k]:
                mdpcrypt = mdpcrypt + liste[n+6]
                n=n+1

            else:
                n=n+1
                
        k=k+1
    print(mdpcrypt)
    




def decrypt():
    global mot
    global mdpcrypt
    
    k=0
    n=0
    mdpcrypt=''
    for _ in range(len(mot)):
        n=0
        for _ in range(len(liste)):
    
            if liste[n]==mot[k]:
                mdpcrypt = mdpcrypt + liste[n-6]
                n=n+1

            else:
                n=n+1
        k=k+1
    print(mdpcrypt)


def to():
    crypt()
    decrypt()
