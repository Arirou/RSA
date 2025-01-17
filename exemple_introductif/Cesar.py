import time

# fonction qui permet de transformer un message en str en un message codé en Cesar
def coder(texte: str, clef: int):
    ascii_decode = [ord(i) for i in texte]  # pour passer de str à ASCII
    texte_decode = ascii_decode
    for i in range(len(texte)):
        texte_decode[i] = ascii_decode[i] + clef
    chaine = ''
    for i in texte_decode:  # pour passer d'ASCII à str
        chaine += chr(i)
    return chaine

# fonction qui permet de décoder n'importe quel code Cesar et de voir toutes les possibilités
def decoder_sans_clef(texte: str):
    start_time = time.time()
    tableau = []
    for i in range(25):
        decode = ""
        for j in range(len(texte)):
            ascii = ord(texte[j]) + i
            if ascii >= 90:
                decode += chr(ascii - 25)
            else:
                decode += chr(ascii)
        tableau.append(decode)
    end_time = time.time()
    print("texte de départ :")
    print(texte)
    for i in range(len(tableau)):
        print(tableau[i])
    return

def main():
    print(coder("BONJOUR", 3))  # le résultat doit être ERQMRXU
    decoder_sans_clef("ERQMRXU")  # le résultat doit être le troisième si on commence à 0
    decoder_sans_clef("LGUWKUWPGNGXGFGDWVVTQKUCOCWDGWIGGVLGHCKUNGOQFWNGFGOQPUKGWTFGNCVVTGRNWURTGEKUGOGPVNGUWLGVUWTNGTUC")

    quitter = input("Voulez-vous quitter ? (oui/non) : ")
    if quitter.lower() != 'oui':
        main()

main()
