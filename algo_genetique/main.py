import random
from math import *


class Algo :
    
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


    def calcul_longueur(self):
        result = 0

        for item in self.population :
            # print(f"item = {item}")

            for point in item['chemin']:
                x1 =  self.points_a_visiter[point][0]
                x2 =  self.points_a_visiter[point][1]


                # # print(point)
                # print(len(self.points_a_visiter))
                # if point < len(self.points_a_visiter) :
                #     y1 = self.points_a_visiter[point][0]+ 1
                #     y2 = self.points_a_visiter[point][1]+ 1

                
                distance = sqrt((x2-x1)**2 + (y2-y1)**2)
                self.population[point]["longueur"] = distance

        # print (self.population)

                

    







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

test = Algo(dico, len(dico))
print (test.calcul_longueur())
