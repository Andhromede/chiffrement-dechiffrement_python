"""
class Arbre :
    Constructeur
    ajouter enfant
    afficher si ca n'est pas une feuille
    trouver profondeur d'arbre
    parcourir la profondeur 
    parcourir la largeur
"""


class Arbre:

    def __init__(self, valeur):
        self.valeur = valeur
        self.children = []


    def add_child(self, valeur):
        noeud = valeur
        self.children.append(noeud)
        return noeud
    # def add_child(self, noeud:Arbre) -> None:
    #     self.children.append(noeud)


    def is_leaf(self):
        return False if len(self.children) > 0 else True


    # profondeur de l'arbre
    # renvois la profondeur total d'un arbre cad un nombre indiquant le nbr d'enfant + arbre
    def profondeur_arbre(self):
        if self.is_leaf():
            return 1
        liste_profondeur = [child.profondeur_arbre() for child in self.children]
        return max(liste_profondeur) +1


    # Parcours en profondeur
    # Renvois une chaine de character avec tous les enfants dedans (de bas en haut)
    def dfs(self) -> list: 
        if self.is_leaf():
            return[self.valeur]
        
        liste_resultat = []

        for item in self.children:
            liste_resultat += item.dfs()
        liste_resultat.append(self.valeur)

        return liste_resultat


    # Parcours en largeur
    # Renvois une chaine de character avec le classement des enfants au fur et a mesure (de gauche a droite)
    def bfs(self) -> list:
        queue = [self]
        result = []

        while len(queue) != 0:
            elt = queue.pop(0)
            result.append(elt.valeur)

            for child in elt.children:
                queue.append(child)

        return result






racine = Arbre(0)
noeud1 = Arbre(1)
noeud2 = Arbre(2)
noeud3 = Arbre(3)
noeud4 = Arbre(4)
feuille1 = Arbre(5)
feuille2 = Arbre(6)
feuille3 = Arbre(7)

racine.add_child(noeud1)
racine.add_child(noeud2)
noeud1.add_child(noeud3)
noeud3.add_child(noeud4)
noeud2.add_child(feuille1)
noeud4.add_child(feuille2)
noeud1.add_child(feuille3)

# print(racine.profondeur_arbre())



# def creation_noeud(noeud):
#     for i in (range(0, 2)):
#         noeud.add_child(i)
#     return noeud






print(racine.children)

# print(noeud1.children)

print(racine.dfs())
print(racine.bfs())

