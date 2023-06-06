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
        noeud = Arbre(valeur)
        self.children.append(noeud)
        return noeud


    def is_feuille(self):
        return False if len(self.children) > 0 else True


    def profondeur_arbre(self, valeur):
        profondeur = 0

        if len(self.children) > 0 :
            for child in self.children:
                print(self.children)




# for i in(range(1, 3)):
#     arbre1.add_child(i)

racine = Arbre(0)
# noeud1 = racine.add_child(1)
# noeud2 = racine.add_child(2)

# noeud3 = noeud1.add_child(4)
# noeud4 = noeud2.add_child(4)


def creation_noeud(noeud):
    for i in (range(0, 2)):
        noeud.add_child(i)
    return noeud

test = creation_noeud(racine)
print(racine.children)

# print(noeud1.children)


