import string

# Générer la matrice
alphabet = string.ascii_uppercase
n = len(alphabet)

# Construction de la matrice
matrice = [[alphabet[(i + j) % n] for j in range(n)] for i in range(n)]

# Afficher la matrice
for ligne in matrice:
    print(" ".join(ligne))
