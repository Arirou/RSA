from random import choice

from RSA.Partie_C import cryptage as crypt, decryptage as decrypt

p = 7
q = 11
N = 77
e = 13
d = 37
clef_publ = (N, e)
clef_priv = (N, d)
clef_pri = (37687171, 18267121)
clef_pub = (37687171, 12689281)


def transformation2(ch):
    bloc = []
    ch1 = ch
    for i in range(0, len(ch1), 2):
        bloc += [ch[i:i + 2]]
    return bloc


def transformation3(ch):
    bloc = []
    ch1 = ch
    for i in range(0, len(ch1), 3):
        bloc += [ch[i:i + 3]]
    return bloc


def ch_ascii(ch):
    bloc = transformation2(ch)
    code_ascii = []
    bloc_nb = []
    for i in range(len(bloc)):
        for j in range(len(bloc[i])):
            x = str(ord(bloc[i][j]))
            if len(x) < 3:
                while len(x) < 3:
                    x = '0' + x
            code_ascii += [x]
    code_ascii = transformation2(code_ascii)
    for i in range(len(code_ascii)):
        nb = ''
        for j in range(len(code_ascii[i])):
            nb += str(code_ascii[i][j])
        bloc_nb += [(nb)]
    return bloc_nb


def cryptage(ch, clef):
    mot = ch_ascii(ch)
    crypter = []
    for i in range(len(mot)):
        crypter += [crypt(int(mot[i]), clef)]
    return crypter


def decryptage(liste_crypter, clef):
    decrypter = []
    for i in range(len(liste_crypter)):
        decrypter += [decrypt(liste_crypter[i], clef)]
    return decrypter


def ascii_ch(liste_coder):
    bloc_nb = []
    ch = []
    mot = ''
    mot_null = []
    for i in range(len(liste_coder)):
        nb = ''
        nb += str(liste_coder[i])
        bloc_nb += [nb]
        if len(bloc_nb[i]) == 3:
            break
        if len(bloc_nb[i]) > 3:
            while len(bloc_nb[i]) < 6:
                bloc_nb[i] = '0' + bloc_nb[i]
    for i in range(len(bloc_nb)):
        if len(bloc_nb[i]) == 4:
            ch += [transformation2(bloc_nb[i])]
        else:
            ch += [transformation3(bloc_nb[i])]
    for i in range(len(ch)):
        for j in range(len(ch[i])):
            if int(ch[i][j]) == 0:
                mot_null += [ch[i][j]]
            else:
                x = int(ch[i][j])
                mot += chr(x)
    return mot


# mot=str(input('entrer le mot a decripter: '))
# cry=cryptage(mot,clef_pub)
# decry=decryptage(cry,clef_pri)
# print(ascii_ch(decry))


liste_de_phrase_mot = ["salutations", "bonjour comment vas tu ?", "Je sais que je ne sais rien",
                       " il fait super beau aujourd'hui", "ça ça marche ?", "incroyable mais vrais",
                       "pourquoi les maths c'est difficile", "j'aime pas la pluit", "je t'aime beaucoup tu sais",
                       "chut ne dis rien!"]

a_transformer = choice(liste_de_phrase_mot)

print("decoupage du mot en groupe de 2 caractere :", transformation2(a_transformer))
print("codage en acsii:", ch_ascii(a_transformer))
print("cryptage avec la clé publique:", cryptage(a_transformer, clef_pub))
print("cryptage en chaine de caractere:", ascii_ch(cryptage(a_transformer, clef_pub)))
print("decryptage avec la clé privé:", decryptage(cryptage(a_transformer, clef_pub), clef_pri))
print("decryptage en chaine de caractere:", ascii_ch(decryptage(cryptage(a_transformer, clef_pub), clef_pri)))

