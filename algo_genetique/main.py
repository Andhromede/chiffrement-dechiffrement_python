import random, operator
from math import *
# from random import randint, shuffle

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
                pts = self.points_a_visiter
                # calcul la distance total de chaque chemin
                distance += sqrt((pts[i-1][0]-pts[i][0])**2 + (pts[i-1][1]-pts[i][1])**2)
                item["longueur"] = distance

        return self.population


# -----------------------------------------------------------
# 3°) SELECTION DES MEILLEURS (1/3) CHEMINS
# -----------------------------------------------------------
    def selection_naturel(self):
        # classe le dictionnaire en fonction de la longueur des chemins (ordre croissant)
        self.population = sorted(self.population, key= operator.itemgetter("longueur"))
        # self.population = sorted(self.population, key= lambda dico:dico["distance"])
        
        # garde le 1er tier du tableau ci dessus
        self.population = self.population[::len(self.population)//3]
        return self.population


# -----------------------------------------------------------
# 4°) CROISEMENTS / MUTATIONS
# -----------------------------------------------------------
    # def evolution_naturel(self):
    #     for item in self.population :
    #         debut_sequence = (item["chemin"][0 : (len(item["chemin"])//2)])
    #         fin_sequence = (item["chemin"][len(item["chemin"])//2 : len(item["chemin"])])

    #         melange = debut_sequence
    #         # print(debut_sequence)
    #         print(melange)
    #         print(fin_sequence)
            
    #         for i in fin_sequence:
    #             for j in melange:
    #                 if i != j :
    #                     melange += j

    #         print (melange)

    def mutation(self) -> None :
        for i in range(3, len(self.population)) :
            if random.randint(1, 100) <= 5:
                chemin = self.population[i]
                nb_aleatoire = random.randint(1, len(chemin["chemin"])-1)
                nb_aleatoire2 = random.randint(1, len(chemin["chemin"])-1)
                # on switch les 2 nombres
                chemin["chemin"][nb_aleatoire], chemin["chemin"][nb_aleatoire2] =\
                    chemin["chemin"][nb_aleatoire2], chemin["chemin"][nb_aleatoire] 


    def croisement(self) -> None:
        i = 0
        while len(self.population) != self.taille_population :
            # selection des parents
            chemin_papa = self.population[i]["chemin"]
            chemin_maman = self.population[i+1]["chemin"]
            chemin_enfant = chemin_papa[:: len(chemin_papa)//2]

            # creation des "enfants"
            for point in chemin_maman:
                if point not in chemin_enfant:
                    chemin_enfant.append(point)

            # ajoute l'enfant a la population
            self.population.append({
                "chemin": chemin_enfant,
                "longueur": None,
            })

            i+=1
        return self.population

    def calculer_meilleur_chemin(self, nb_iteration):
        self.evaluation_population()
        for _ in range(nb_iteration):
            self.selection_naturel()
            self.croisement()
            self.mutation()

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

print(algo1.croisement())