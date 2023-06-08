from math import *
from itertools import permutations

# ============================================================
dico = {
    0:[0, 0],
    1:[300.8, 202.54],
    2:[5432.6, 676.865],
    3:[65.9, 49.643],
}

# ============================================================
# CALCUL TTES LES POSSIBILITES D'UNE CHAINE ET LES RENVOIS
# ============================================================
def calcul_possibilites(dictionnaire, nbr):
    """
    Renvoi un tableau contenant toutes les possibilités d'une chaine 
   
    Args : 
    dictionnaire : un tableau de chiffres ou de lettres
    nbr : le nombre de chiffres à afficher dans chacuns des résultats

    Ex :
    tableau_initial = [1, 2, 3]
    resultat_fonction = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    """

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
    """Send back the distance between two points

    Args:
        x1 (float): coordinate x of the first point
        y1 (float): coordinate y of the first point
        x2 (float): coordinate x of the second point
        y2 (float): coordinate y of the second point

    Returns:
        float: Return the distance
    """

    distance = sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance


# ============================================================
# CALCUL DES DISTANCES SELON TOUTES LES POSSIBILITES
# ============================================================
tab_possibilites = calcul_possibilites(dico, len(dico))
result = 0
tab_result={}

for item in tab_possibilites :
    for j in item:
        result += calcul_distance(dico[item[j]][0], dico[item[j]][1], dico[item[j-1]][0], dico[item[j-1]][1])
    tab_result[item] = result
print(tab_result)





