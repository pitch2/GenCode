liste=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
       'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


mot =''
def demande():
    global mot
    mot=input("Saisir:")
    mot=list(mot.strip())
    print(mot)




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
                mdpcrypt = mdpcrypt + str(liste[n+6])
                n=n+1

            else:
                n=n+1
                
        k=k+1
    print(mdpcrypt)
    k=0
    n=0
    


def decrypt():
    global mot
    global mdpcrypt
    _mdp=''
    _mdp=mdpcrypt
    k=0
    n=0
    mdpcrypt=''
    for _ in range(len(mot)):
        n=0
        for _ in range(len(liste)):
    
            if liste[n]==_mdp[k]:
                mdpcrypt = mdpcrypt + str(liste[n-6])
                n=n+1

            else:
                n=n+1
        k=k+1
    print(mdpcrypt)
    k=0
    n=0
    mdpcrypt=''
    _mdp=''



def to():
    crypt()
    decrypt()


i=[1]

def test():
    nbr=[1,2,3,4,5,7,8,9]
    #checking if element 7 is present
    # in the given list or not
    i=[1,6,8]
    n=0
    # if element present then return
    # exist otherwise not exist
    for _ in range (len(i)):
        if i[n] in nbr:
            print("exist")
        else:
            print("not exist")
            n=n+1



    
    
