import random
import random as r

class Personne:
    def __init__(self,nom,proba_infection=0):
        self.nom = nom
        self.sante = "saine"
        self.proba_infection = proba_infection
    def infecter(self):
        self.sante = "infectee"
    def immuniser(self):
        self.sante = "immunisee"
        #self.immunise = 0
    def __str__(self):
        return f"le nom du patient est {self.nom} et sa sante est {self.sante}"

class Population:
    def __init__(self,taille_population,proba_infection):
        self.individu = [Personne(f"Individu{i+1}",proba_infection)for i in range (taille_population)]
    def introduire_infection(self,nombre_infectes):
        infectes = random.sample(self.individu,nombre_infectes)
        for i in infectes:
            i.infecter()


    def simuler_jour(self,proba_guerison):
        nouv_infection=[]
        for personne in self.individu:
            if personne.sante == "infectee":
                if random.random()<proba_guerison:
                    personne.immuniser()
                else:
                    for autre in self.individu:
                        if autre.sante == "saine" and random.random()<autre.proba_infection:
                            autre.infecter()


    def __str__(self):
        saines = sum(1 for p in self.individu if p.sante=="saine")
        infectees = sum(1 for p in self.individu if p.sante == "infectee")
        immunisee = sum(1 for p in self.individu if p.sante == "immunisees")

        return f"nombre de personnes saines: {saines} ,et nombre de personnes infectees : {infectees} et nombre de personnes  immunises {immunisee }"

#tache1
popu1 = Population(1000,0.1)
#tache2
nbre = 10
popu1.introduire_infection(nbre)
#tache3
proba_guerison = 0.05
nombre_jours = 30
print ("etat initial de la population:",popu1)
for jour in range(1,nombre_jours+1):
    popu1.simuler_jour(proba_guerison)
    print(f"Jour {jour}:{popu1}")