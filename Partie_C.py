
from Partie_B import liste_pseudos_premiers, nb_eluer
from random import choice,randint
from Partie_A import  lpowmod

# Clef publique
def pgcd(a, b):
    while b > 0:
        reste = a % b
        a, b = b, reste
    return a


def clef_publique(p, q):
    N = p * q
    N1 = (p - 1) * (q - 1)
    e = choice(liste_pseudos_premiers(nb_eluer(107)))
    if e < N1 and pgcd(e, N1) == 1:
        return (N, e)
    if e >= N1 or pgcd(e, N1) != 1:
        return clef_publique(p, q)


def cryptage(x, clef):
    e = clef[1]
    N = clef[0]
    y=lpowmod(x,e,N)
    return y


# print('le pgcd de 7 et 11 :',pgcd(7,11))
# print('la clef publique de 7 et 11 :',clef_publique(7,11))
# print('cryptage de C par 3:',cryptage(3,(77,59)))

#---------------------------------------------------------------------#

# Clef privée

def clef_privee(p, q, e):

    N = p * q
    N1 = (p - 1) * (q - 1)
    d=randint(2,N**2)

    assert pgcd(e, N1)==1
    while e*d%N1-1!=0:
        d =randint(2,N**2)
    return (N, d)


def decryptage(y, clef):
    N = clef[0]
    d = clef[1]
    x=lpowmod(y,d,N)
    return x
# clef_pri=(37687171,18267121)
# clef_pub=(37687171,12689281)
# print('la clef priver de 7 et 11:', clef_privee(7, 11, 59))
# clef = (77,59)
# print(decryptage(cryptage(3, clef),clef_privee(7, 11,59)))
