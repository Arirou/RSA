def permuter(bloc, permutation):
    return ''.join(bloc[i] for i in permutation)


def chiffrer(texte, permutation):
    taille_bloc = len(permutation)
    texte_chiffre = []

    # Compléter le dernier bloc si nécessaire
    while len(texte) % taille_bloc != 0:
        texte += ' '

    # Appliquer la permutation à chaque bloc
    for i in range(0, len(texte), taille_bloc):
        bloc = texte[i:i + taille_bloc]
        texte_chiffre.append(permuter(bloc, permutation))

    return ''.join(texte_chiffre)


def dechiffrer(texte_chiffre, permutation):
    # Inverser la permutation
    permutation_inverse = [0] * len(permutation)
    for i, p in enumerate(permutation):
        permutation_inverse[p] = i

    return chiffrer(texte_chiffre, permutation_inverse)


# Exemple d'utilisation
def main():
    texte = "bonjour monde"
    permutation = [2, 0, 3, 1]  # Exemple de permutation pour des blocs de taille 4

    print("Texte original:", texte)

    texte_chiffre = chiffrer(texte, permutation)
    print("Texte chiffré :", texte_chiffre)

    texte_dechiffre = dechiffrer(texte_chiffre, permutation)
    print("Texte déchiffré:", texte_dechiffre)

    quitter = input("Voulez-vous quitter ? (oui/non) : ")
    if quitter.lower() != 'oui':
        main()


main()