#nb_clef = int(input("Entrez un nombre entier pour la clef de chiffrement : "))
#print(f"La clef de décalage sera de : {nb_clef}")

def coder(texte:str, clef:int):
    ascii_code = [ord(i) for i in texte] #pour passer de str à ASCII
    texte_code = ascii_code
    for i in range(len(texte)):
        texte_code[i] = ascii_code[i]+clef
    chaine = ''
    for i in texte_code: #pour passer d'ASCII à str
        chaine += chr(i)
    return chaine

print(coder("BONJOUR",3)) #le résultat doit être ERQMRXU