# CHR = 1 -> A
# ORD = A -> 1

# =========================================================
# CHIFFREMENT 
# =========================================================
def chiffrement(message, nbr):
    msgChiffree = ""

    for i in range(len(message)):
        msgChiffree += chr(ord(message[i])+nbr)

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
    # primaryKey = dechiffrement(messageAdechiffrer, 27)

    tab = {}

    for char in messageAdechiffrer:
        if char in tab:
            tab[char] += 1
        else :
            tab[char] = 1
       

    lettreCourante = max(tab, key=tab.get)
    print(lettreCourante)

    asciiLettreCourante = ord(lettreCourante)
    ecart = - (ord(" ") - asciiLettreCourante)
    print(ecart)

    # return primaryKey

print(calculFrequence(messageAdechiffrer))
        





