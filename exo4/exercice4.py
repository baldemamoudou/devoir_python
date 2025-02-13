import numpy as np
import matplotlib.pyplot as plt
import pandas as pd # Pour afficher la matrice des résultats sous forme de tableau

#Etape1: Initialisation des paramètres
beta = 2 # Nombre de nouveaux hôtes produits par hôte
alpha = 0.05 # Zone d'attaque du parasitoïde
g = 1 # Nombre de nouveaux parasitoïdes produits par hôte parasité

# Taille initiales des populations
H0 = 20 # Population initiale des hôtes
P0 = 2 # Population initiale des parasitoïdes
# Nombre de génération
generation = 30

#Etape2: Configuration des vecteurs pour stocker les valeurs
H = np.zeros(generation) # Vecteur pour les hôtes
P = np.zeros(generation) # Vecteur pour les parasitoïdes
H[0] = H0
P[0] = P0


#Etape3: Programmation du modèle réel (boucle pour calculer l'évolution des populations)

for t in range(1, generation):
    H[t] = beta * H[t-1] * np.exp(-alpha * P[t-1]) # Equation pour les hôtes
    P[t] = g * H[t-1] * (1 - np.exp(-alpha * P[t-1])) # Equation pour les parasitoïdes


#Affichage sous forme de tableau (matrice des résultats)
data = {"Génération": np.arange(generation), "Hôtes (H)": H, "Parasitoïdes (P)": P}
df = pd.DataFrame(data)
print(df)


#Etape4: Affichage graphique des résultats

plt.figure(figsize=(10, 5))
plt.plot(range(generation), H, label="Hôtes (H)", marker="o", linestyle="-", color="blue")
plt.plot(range(generation), P, label="Parasitoïdes (P)", marker="s", linestyle="dashed", color="red")
plt.xlabel("Générations")
plt.ylabel("Taille de la population")
plt.title("Modèle de Nicholson-Bailey: Evolution des populations")
plt.legend()
plt.grid()
plt.show()