from exercice import *
#Données d'exemple


X= np.array([2.1, 2.5, 3.6, 4.0, 5.1])
Y= np.array([8.0, 9.5, 10.5, 12.0, 14.0])

n = len(X)
#Etape1: Calcul du coefficient de corrélation r

r = correlation_coefficient(X, Y)

#Etape2: Transformatin de Fisher

Z= fisher_transformation(r)

#Etape3: Test pour H0 : p = p0 (avec p0 = 0 et p0 = 0.6)

rho_0_1 = 0.0
rho_0_2 = 0.6

Z0_1 = fisher_transformation(rho_0_1)
Z0_2 = fisher_transformation(rho_0_2)

w_1 = test_statistic(Z, Z0_1, n)
w_2 = test_statistic(Z, Z0_2, n)

p_1 = p_value(w_1)
p_2 = p_value(w_2)

#Etape5: Comparaison des résultats


print(f"Coefficient de corrélation r : {r}")
print(f"Statistique z de Fisher: {Z}")
print(f"Test pour p0 = 0: w = {w_1}, p_value = {p_1}")
print(f"Test pour p0 = 0.6: w = {w_2}, p_value = {p_2}")


if p_1 < 0.05:
    print("Pour p0 = 0, la corrélation est significative (p<0.05).")
else:
    print("Pour p0 = 0, la corrélation n'est pas significative.")
if p_2 < 0.05:
    print("Pour p0 = 0.6, la corrélation est significative (p< 0.05).")
else:
    print("Pour p0 = 0.6, la corrélation n'est pas significative.")
