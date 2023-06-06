# CHR = 1 -> A
# ORD = A -> 1

# =========================================================
# CHIFFREMENT 
# =========================================================
def chiffrement(message, nbr):
    msgChiffree = ""

    for i in range(len(message)):
        msgChiffree += chr(ord(message[i])+nbr)

    # for i in message:
    #     msgChiffree += chr(ord(i)+nbr)

    return msgChiffree

# strChiffree = chiffrement("hello world !", 3)
# print(strChiffree)

#=========================================================
# DECHIFFREMENT
# =========================================================

def dechiffrement(message, nbr):
    return chiffrement(message, -nbr)

# print(dechiffrement(strChiffree, 3))


#=========================================================
# DECHIFFREMENT
# =========================================================
messageAdechiffrer = "]\x8a\x89\x85\x8a\x90\x8d;\x88\x80\x8e;\x8f\x8dă\x8e;~\x83\x80\x8d\x8e;|\x8b\x8b\x8d\x80\x89|\x89\x8f\x8eI;aĄ\x87\x84~\x84\x8f|\x8f\x84\x8a\x89\x8e;û;\x91\x8a\x90\x8eG;\x91\x8a\x90\x8e;|\x91\x80\x95;\x8dĄ\x90\x8e\x8e\x84;û;~|\x8e\x8e\x80\x8d;~\x80;~\x8a\x7f\x80;<;e\x80;\x8e\x90\x84\x8e;\x81\x84\x80\x8d;\x7f\x80;\x91\x8a\x90\x8eI;h|\x84\x89\x8f\x80\x89|\x89\x8fG;\x91\x8a\x90\x8e;\x8b\x8a\x90\x91\x80\x95;~\x8a\x88\x88\x80\x89~\x80\x8d;\x87\x80;~\x8a\x7f\x80;\x7f\x80;q\x84\x82\x80\x89ă\x8d\x80"

def calculFrequence(messageAdechiffrer):
    tab = {}

    for char in messageAdechiffrer:
        if char in tab:
            tab[char] += 1
        else :
            tab[char] = 1

    # Permet de trouver le charactère le plus courant dans le dico
    lettreCourante = max(tab, key=tab.get)
    # Convertit le caractère en ASCII
    asciiLettreCourante = ord(lettreCourante)
    # Calcul l'écart (en ascii) entre le caractère courant et la barre espace
    ecart = - (ord(" ") - asciiLettreCourante)
    # ecart = ord(asciiLettreCourante - (" "))

    return dechiffrement(messageAdechiffrer, ecart)

# print(calculFrequence(messageAdechiffrer))
        

#=========================================================
# VIGENERE
# =========================================================

msgVigenere = """Frères humains qui après nous vivez
N'ayez les cœurs contre nous endurcis,
Car, se pitié de nous pauvres avez,
Dieu en aura plus tot de vous mercis.
Vous nous voyez cy attachez cinq, six
Quant de la chair, que trop avons nourrie,
Elle est pieça devoree et pourrie,
Et nous les os, devenons cendre et pouldre.
De nostre mal personne ne s'en rie :
Mais priez Dieu que tous nous vueille absouldre!"""

cle = [1, 2, 3, 4]


# ----------- CHIFFREMENT -----------
def chiffrer_vigenere(message:str, cle:tuple) -> str :
    message_code = ""
    index_cle = 0
    for lettre in message:
        message_code += chr(ord(lettre) + cle[index_cle])
        index_cle = (index_cle + 1) % len(cle)
    return message_code

# message_code_vigenere = chiffrer_vigenere(msgVigenere, cle)
# print(message_code_vigenere)


# ----------- DECHIFFREMENT -----------
def dechiffrer_vigenere(message_code:str, cle:str) -> str :
    # chiffrer_vigenere(message_code,[-elt for elt in cle])
    return chiffrer_vigenere(message_code, tuple([-elt for elt in cle]))

# message_decode_vigenere = dechiffrer_vigenere(message_code_vigenere, cle)
# print(message_decode_vigenere)    


