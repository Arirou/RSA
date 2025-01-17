

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
