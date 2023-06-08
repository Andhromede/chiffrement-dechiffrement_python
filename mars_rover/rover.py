from math import *
from itertools import permutations


# formule: d = r2 (X2-X1)2 + (Y2-Y1)2 + (Z2-Z1)2

dico = {
    0:[0, 0],
    1:[300.8, 202.54],
    2:[5432.6, 676.865],
    3:[65.9, 49.643],
}

# nb_possibilite = 2 * len(dico)
# longueur = len(dico)
# tmp= ""
# liste = []


# CALCUL TTES LES POSSIBILITES D'UNE CHAINE ET LES RENVOIS
"""
Renvoi un tableau contenant toutes les possibilités d'une chaine 
   
Args : 
    dictionnaire : un tableau de chiffres ou de lettres
    nbr : le nombre de chiffres à afficher dans chacuns des résultats

Ex :
    tableau_initial = [1, 2, 3]
    resultat_fonction = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
"""
def calcul_possibilites(dictionnaire, nbr):
    tableau_possibilite = []
    temp = permutations(dictionnaire, nbr)
    for i in list(temp):
    	if (i[1] != 0):
            tableau_possibilite.append(i)
            # print(tableau_possibilite)
    return tableau_possibilite


# print(calcul_possibilites(dico, 4))





# # CALCUL LES DISTANCES ENTRE DES POINTS
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












# CALCUL LES DISTANCES ENTRE DES POINTS
# def calcul_distance(xa, xb, ya, yb):
#     DistanceAB=sqrt((xb-xa)**2+(yb-ya)**2)
#     # print("la distance exacte entre A et B est de racine de",round(DistanceAB**2))
#     # print("la distance approximative entre A et B est d'environ","%.2f" %(DistanceAB))
#     return "%.2f" %(DistanceAB)



last_number = 0
tableau_distance = {}




print(dico)

for i in dico :
    # print(i)
    
    for j in dico:
        print(j)
        last_number = dico[i]
        distance = calcul_distance(dico[i][0], dico[i][0], last_number[0], last_number[1])
        # distance = calcul_distance(dico[i][0], dico[i][0], last_number[0], last_number[1])

        # if distance != 0:
        tableau_distance[f"{i}/{i-1}"]= distance

print(tableau_distance)





# xa=float(300.8)
# xb=float(202.54)
# ya=float(5432.6)
# yb=float(676.865)
# print(calcul_distance(xa, xb, ya, yb))