from Partie_A import exp_mod
from math import sqrt

def prim(n):
    """
    fonction qui permet de determiner si un nombre est le premier avec la methodes de primalité
    :param n: un entier
    :return: un Booleen
    """
    assert n>2
    for i in range (2,int(sqrt(n))):
        if n%i==0:
            return False
    return True


def fermat(n, Base):
    """
    fonction qui permet a determiner si un nombre est premier avec la methodes fermat
    :param n: un nombre
    :param Base: la base de teste
    :return: un booléen
    """
    reponse=True
    for i in range(len(Base)):
        if 1 <= Base[i] < n:
            if exp_mod(Base[i],n,n-1)==1:
                reponse=False
    return reponse

def nb_eluer(n):
    liste_eluer=[]
    for i in range(n):
        liste_eluer+=[i**2+i+41]
    return liste_eluer


def liste_pseudos_premiers(liste):
    liste_pseudos_premiers=[]
    for i in range (3,len(liste)+2):
        if prim(i)==True:
            liste_pseudos_premiers+=[i]
    return liste_pseudos_premiers



# print(prim(72))
# print(prim(65))
# Base = [2, 3, 5, 7]
# print(fermat(12, Base))
#print(nb_eluer(2))
liste=nb_eluer(107)
#print(liste)
#print(liste_pseudos_premiers(liste))