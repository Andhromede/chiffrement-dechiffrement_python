# CHR = 1 -> A
# ORD = A -> 1

# =========================================================
# CHIFFREMENT 
# =========================================================
def chiffrement(message, nbr):
    msgChiffree = []

    for i in range(len(message)):
        msgChiffree.append(str(ord(message[i])-nbr))

    return msgChiffree

strChiffree = chiffrement("hello world !", 3)
print(strChiffree)

#=========================================================
# DECHIFFREMENT
# =========================================================

def dechiffrement(message, nbr):
    msgDechiffree = ""

    for i in range(len(message)):
        msgDechiffree += chr(int(message[i])+nbr)

    return msgDechiffree

print(dechiffrement(strChiffree, 3))

#=========================================================
# DECHIFFREMENT
# =========================================================