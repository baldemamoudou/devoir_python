import csv
import math
import matplotlib.pyplot as plt
import numpy as np

nom = "ebola_guinea.csv"
#fonction pour lire dans le fichier
def lirefichier(nom):
    liste_de_dictionnaires = []
    with open('ebola_guinea.csv','r') as fic:
        lecteur_csv = csv.DictReader(fic)
        for ligne in lecteur_csv:
            liste_de_dictionnaires.append(dict(ligne))

    return liste_de_dictionnaires

nom = "ebola_guinea.csv"
resultat = lirefichier(nom)
print(resultat)

#fonction qui calcule le nombre total de cas et deces pour chaque prefecture
def calcul_totaux_par_prefecture():
    print("nombre total de cas a conakry:",10+15+22)
    print("nombre total de cas a boke:", 3 + 5 + 8)
    print("nombre total de cas a kindia:", 5 + 8 + 12)

def calcul_taux():
    #taux de mortalite pour chaque prefecture
    #pour conakry
    nbredecesckry = 25
    nbrecas = 47
    taux_conakry = (nbredecesckry *100)/nbrecas
    print("le taux de conakry est ",taux_conakry)


    #pour boke
    nbredecesboke = 7
    nbrecas = 16
    taux_boke = (nbredecesboke *100)/nbrecas
    print("le taux de boke est ",taux_boke)

    #pour kindia
    nbredeceskindia = 11
    nbrecas = 25
    taux_kindia = (nbredeceskindia *100)/nbrecas
    print("le taux de kindia est ",taux_kindia)


calcul_totaux_par_prefecture()
calcul_taux()


#Visualisation1 Nombre total de cas


# donnes a utiliser
prefectures = ['Conakry', 'Boké', 'Kindia']
total_cas = [47, 16, 25]


plt.figure(figsize=(10, 6))
plt.bar(prefectures, total_cas)


plt.title('nombre total de cas par Prefecture')
plt.xlabel('Prefecture')
plt.ylabel('Nombre de cas ')


plt.show()


#Visualisation2 Taux de mortalite



prefectures = ['Conakry', 'Boké', 'Kindia']
taux_de_mortalite = [53.191489361702125, 43.75, 44.0]


plt.figure(figsize=(10, 6))
plt.bar(prefectures, taux_de_mortalite)


plt.title('taux par prefecture')
plt.xlabel('Prefecture')
plt.ylabel('taux de mortalite (%)')


plt.show()
