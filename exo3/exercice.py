import numpy as np

import scipy.stats as stats
#Etape1: Calcul du coefficient de corrélation entre X et Y

def correlation_coefficient(X, Y):
    return np.corrcoef(X, Y)[0, 1]

#Etape2: Calcul de la statistique z de Fisher

def fisher_transformation(r):
    return 0.5*np.log((1+r)/(1-r))

#Etape3: Calcul de la statistique w pour tester l'hypothèse nulle


def test_statistic(Z, Z0, n):
    return (Z-Z0)/np.sqrt(1 / (n-3))

#Etape4: Calcul de la valeur p du test

def p_value(w):
    return 2*(1 - stats.norm.cdf(abs(w)))



print("*******************************")



