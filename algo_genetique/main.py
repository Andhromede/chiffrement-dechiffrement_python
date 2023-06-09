import random, operator
from math import *



class Algo :

# -----------------------------------------------------------
# 1°) CREER LA POPULATION DE BASE
# ----------------------------------------------------------- 
    """
    Initialisation de la classe : tableau de points avec les coordonnées + la taille de la population
    """
    def __init__(self, points_a_visiter, taille_population):
        self.points_a_visiter = points_a_visiter
        self.taille_population = taille_population
        self.population = []

        for _ in range(taille_population):
            index_point = [ i for i in range(1, len(points_a_visiter))]
            random.shuffle(index_point)
            index_point.insert(0, 0)

            dico = {
                "chemin": index_point,
                "longueur": None,
            }

            self.population.append(dico)

# -----------------------------------------------------------
# 2°) CALCUL LA LONGUEUR TOTAL DE TOUS LES TRAJETS
# -----------------------------------------------------------
    def evaluation_population(self):
        distance = 0

        for item in self.population :
            for i in range(1, len(item['chemin'])):
                x1 =  self.points_a_visiter[i][0]
                y1 =  self.points_a_visiter[i][1]
                x2 = self.points_a_visiter[i-1][0]
                y2 = self.points_a_visiter[i-1][1]
                distance += sqrt((x2-x1)**2 + (y2-y1)**2)
                item["longueur"] = distance

        return self.population

# -----------------------------------------------------------
# 3°) SELECTION DES MEILLEURS (1/3) CHEMINS
# -----------------------------------------------------------
    def selection_naturel(self):
        self.population = sorted(self.population, key= operator.itemgetter("longueur"))
        self.population = self.population[::len(self.population)//3]
        print(self.population)

# -----------------------------------------------------------
# 4°) CROISEMENTS / MUTATIONS
# -----------------------------------------------------------





# -----------------------------------------------------------
# TEST
# -----------------------------------------------------------
dico = {
    0:[0, 0],
    1:[300.8, 202.54],
    2:[5432.6, 676.865],
    3:[65.9, 49.643],
    4:[65.9, 49.643],
}

dico2 = {
    1:[564.3, 563.75],
    2:[178.3, 458.926],
    3:[65.2, 24.153],
    4:[65.8, 92.465],
}

algo1 = Algo(dico, len(dico))
print(algo1.population)
print (algo1.evaluation_population())
print(algo1.selection_naturel())
