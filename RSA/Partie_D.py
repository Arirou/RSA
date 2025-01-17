import os
import sys
from random import choice

# Détection si le programme est exécuté en tant qu'exécutable PyInstaller
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(__file__)

try:
    from Partie_C import cryptage as crypt, decryptage as decrypt
except ImportError:
    from .Partie_C import cryptage as crypt, decryptage as decrypt

# Clés publiques et privées
clef_pri = (37687171, 18267121)
clef_pub = (37687171, 12689281)

# Fonction pour découper une chaîne en blocs de 2 caractères
def transformation2(ch):
    bloc = []
    for i in range(0, len(ch), 2):
        bloc.append(ch[i:i + 2])
    return bloc

# Fonction pour découper une chaîne en blocs de 3 caractères
def transformation3(ch):
    bloc = []
    for i in range(0, len(ch), 3):
        bloc.append(ch[i:i + 3])
    return bloc

# Fonction pour convertir une chaîne en une liste de codes ASCII formatés
def ch_ascii(ch):
    bloc = transformation2(ch)
    code_ascii = []
    bloc_nb = []
    for i in range(len(bloc)):
        for j in range(len(bloc[i])):
            x = str(ord(bloc[i][j]))
            while len(x) < 3:
                x = '0' + x
            code_ascii.append(x)
    code_ascii = transformation2(code_ascii)
    for i in range(len(code_ascii)):
        nb = ''.join(code_ascii[i])
        bloc_nb.append(nb)
    return bloc_nb

# Fonction de cryptage
def cryptage(ch, clef):
    mot = ch_ascii(ch)
    crypter = []
    for i in range(len(mot)):
        crypter.append(crypt(int(mot[i]), clef))
    return crypter

# Fonction de décryptage
def decryptage(liste_crypter, clef):
    decrypter = []
    for i in range(len(liste_crypter)):
        decrypter.append(decrypt(liste_crypter[i], clef))
    return decrypter

# Fonction pour reconstruire la chaîne originale à partir des valeurs ASCII cryptées
def ascii_ch(liste_coder):
    bloc_nb = []
    ch = []
    mot = ''
    mot_null = []
    for i in range(len(liste_coder)):
        nb = str(liste_coder[i])
        bloc_nb.append(nb)
        while len(bloc_nb[i]) < 6:
            bloc_nb[i] = '0' + bloc_nb[i]
    for i in range(len(bloc_nb)):
        if len(bloc_nb[i]) == 4:
            ch.append(transformation2(bloc_nb[i]))
        else:
            ch.append(transformation3(bloc_nb[i]))
    for i in range(len(ch)):
        for j in range(len(ch[i])):
            if int(ch[i][j]) == 0:
                mot_null.append(ch[i][j])
            else:
                mot += chr(int(ch[i][j]))
    return mot

# Liste de phrases à transformer
liste_de_phrase_mot = [
    "salutations", "bonjour comment vas tu ?", "Je sais que je ne sais rien",
    "il fait super beau aujourd'hui", "ça ça marche ?", "incroyable mais vrais",
    "pourquoi les maths c'est difficile", "j'aime pas la pluie", "je t'aime beaucoup tu sais",
    "chut ne dis rien!"
]

# Fonction principale pour exécuter le programme
def run_program():
    a_transformer = choice(liste_de_phrase_mot)

    print("Découpage du mot en groupe de 2 caractères :", transformation2(a_transformer))
    print("Codage en ASCII :", ch_ascii(a_transformer))
    print("Cryptage avec la clé publique :", cryptage(a_transformer, clef_pub))
    print("Cryptage en chaîne de caractères :", ascii_ch(cryptage(a_transformer, clef_pub)))
    print("Décryptage avec la clé privée :", decryptage(cryptage(a_transformer, clef_pub), clef_pri))
    print("Décryptage en chaîne de caractères :", ascii_ch(decryptage(cryptage(a_transformer, clef_pub), clef_pri)))

    replay = input("Voulez-vous relancer le programme ? (oui/non) : ")
    if replay.lower() == 'oui':
        run_program()

# Lancement du programme
if __name__ == '__main__':
    run_program()
