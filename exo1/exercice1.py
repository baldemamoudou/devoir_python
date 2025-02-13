

def Fibonnacci():
    a, b = 0, 1    #initialisation des 2 premiers termes de la suite de fibonnacci

    n = int(input("donnez un nombre \n")) #on demande a l utilisateur d entrer un nombre dont il veut la suite de fibonnacci

    for i in range(n):
        print("itération", i,"a vaut",a) #affiche l iteration actuelle et la valeur de a

        somme = a + b #calcul du prochain terme de la suite

        a = b #a prend b
        b = somme #b prend la nouvellle valeur calculee


    print("la suite de fibonnacci pour ce nombre est :")
    print("f(",n,") = ",a)

