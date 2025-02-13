bos = [2.67, 1.00, 1.21, 3.09, 3.43, 4.71, 3.88, 3.08, 4.10, 2.62, 1.01, 5.93]
mer = [6.83, 3.63, 7.20, 2.68, 2.05, 2.96, 1.04, 0.00, 0.03, 6.71, 8.28, 6.85]
mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
prec_bos_totale = 0
prec_mer_totale = 0
compteur = 0
compteur1 = 0
compteur2 = 0
for i in (bos):
    prec_bos_totale = prec_bos_totale+i
print("les précipitations totales pour l'année à boston est \n", round(prec_bos_totale, 2))
prec_bos_moy = prec_bos_totale/12
print("les précipitations moyennes mensuels à boston est \n", round(prec_bos_moy, 2))
for i in (bos):
    if i > prec_bos_moy:
        compteur += 1
print("les précipitations ont été supérieurs à la moyenne à boston pendant", compteur, "mois")


print("****************************************************************************************")

for i in (mer):
    prec_mer_totale = prec_mer_totale+i
print("les précipitations totales pour l'année à seattle est \n ", round(prec_mer_totale, 2))
prec_mer_moy = prec_mer_totale/12
print("les précipitations moyennes mensuels à seattle est \n", round(prec_mer_moy, 2))
for i in (mer):
    if i > prec_mer_moy:
        compteur1 += 1
print("les précipitations ont été supérieurs à la moyenne à seattle pendant", compteur1, "mois")


print("****************************************************************************************")
for i, j in zip(bos, mer):
    if i < j:
        #print(i)
        compteur2 += 1
        m = bos.index(i)
        print(mois[m])
print("les précipitations à boston ont été inférieurs à celle de seattle pendant", compteur2, "mois")
