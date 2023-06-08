from itertools import permutations
import random
from math import *


# ============================================================
# CREER LA POPULATION DE BASE
# ============================================================
dico = {}

def genere_aleatoire():
    for i in range(5):
        dico[i] = (round(random.uniform(00.00, 500.99), 2)), (round(random.uniform(00.00, 500.99), 2))
    return dico


# ============================================================
# CALCUL LES POSSIBILITES D'UNE CHAINE ET LES RENVOIS
# ============================================================
def calcul_possibilites(dictionnaire, nbr):
    tableau_possibilite = []
    temp = permutations(dictionnaire, nbr)
    for i in list(temp):
    	if (i[0] == 0):
            tableau_possibilite.append(i)
    return tableau_possibilite


# ============================================================
# CALCUL LES DISTANCES ENTRE DES POINTS
# ============================================================
def calcul_distance(x1:float,y1:float,x2:float,y2:float) ->float:
    distance = sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance


# ============================================================
# CALCUL DES DISTANCES SELON TOUTES LES POSSIBILITES
# ============================================================
def calcul_tableau_distance(tab_possibilites):
    tab_possibilites = calcul_possibilites(dico, len(dico))
    result = 0
    tab_result={}

    for item in tab_possibilites :
        for j in item:
            result += calcul_distance(dico[item[j]][0], dico[item[j]][1], dico[item[j-1]][0], dico[item[j-1]][1])
        tab_result[item] = result
    return tab_result






