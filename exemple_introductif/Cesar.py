import time

#fonction qui permet de transformer un message en str en un message codé en Cesar
def coder(texte:str, clef:int):
    ascii_decode = [ord(i) for i in texte] #pour passer de str à ASCII
    texte_decode = ascii_decode
    for i in range(len(texte)):
        texte_decode[i] = ascii_decode[i]+clef
    chaine = ''
    for i in texte_decode: #pour passer d'ASCII à str
        chaine += chr(i)
    return chaine

#fonction qui permet de décoder n'importe quel code Cesar et de voir toutes les possibilités
def decoder_sans_clef(texte:str):
    start_time = time.time()
    ascii_coder = [ord(i) for i in texte] #pour passer de str à ASCII
    tableau_solution = [[0 for _ in range(len(texte))] for _ in range(26)] #création du tableau avec toutes les solutions en ASCII
    for i in range (26):
        for j in range(len(texte)):
            tableau_solution[i][j] = ascii_coder[j]-i #décode avec chaque lettre jusqu'à 26
    tableau_chaine = ['' for _ in range(26)] #création du tableau avec toutes les solutions en str
    for i in range(26):
        for j in tableau_solution[i]: #pour passer d'ASCII à str
            tableau_chaine[i] += chr(j)
    end_time = time.time()
    print(f"Temps d'exécution : {end_time - start_time:.9f} secondes")
    return tableau_chaine

print(coder("BONJOUR",3)) #le résultat doit être ERQMRXU
print(decoder_sans_clef("ERQMRXU")) #le résultat doit être le troisième si on commence à 0
print(decoder_sans_clef("lguwkuwpgngxgfgdwvvtqkucocwdgwiggvlghckungoqfwngfgoqpukgwtfgncvvtgrnwurtgekugogpvnguwlgvuwtngtuc"))