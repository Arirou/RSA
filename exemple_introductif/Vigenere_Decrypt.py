# Source : apprendre-en-ligne
# decrypte un texte avec le chiffre de Vigenere

def que_des_majuscules(texte,taille_bloc=5):
    # remplace les caracteres accentues, supprime les espaces et la ponctuation
    # renvoie une chaine de lettres majuscules
    chaine = ""
    i=0  # tient le compte des lettres du message transforme
    texte = texte.lower()
    for c in texte:
        if 97 <= ord(c) <= 122:
            chaine += chr(ord(c)-32)
        elif c in ("Ã¤","Ã ","Ã¢"):
            chaine += "A"
        elif c in ("Ã©","Ã¨","Ã«","Ãª"):
            chaine += "E"
        elif c in ("Ã®","Ã¯"):
            chaine += "I"
        elif c in ("Ã´","Ã¶"):
            chaine += "O"
        elif c in ("Ã¼","Ã»","Ã¹"):
            chaine += "U"
        elif c == "Ã§":
             chaine += "C"
        else:   # on ne tient pas compte du caractere lu
            i -= 1
        i+=1
        if taille_bloc>0 and i%taille_bloc==0 and i>0 and chaine[-1] != " ":
            chaine+=" "  # ajoute une espace tous les "taille_bloc" caracteres
    return chaine

def ic(texte):
    chaine = que_des_majuscules(texte,0)
    frequences = [0]*26
    n = len(chaine)
    for c in chaine:
        frequences[ord(c)-65] += 1
    indice = 0.0
    for ni in frequences:
        indice += ni*(ni-1)
    return indice/(n*(n-1))


def longueur_cle(texte):
    # devine la longueur de la cle avec l'indice de coincidence
    seuil = 0.06
    ok = False
    k = 0
    while not ok and k<20:
        partiel = ""
        k += 1
        j = 0
        while j < len(texte):
            partiel += texte[j]
            j += k
        ok = ic(partiel)>seuil
    return k

def decalage(c,k):
    # decale une lettre majuscule. Les autres caracteres ne sont pas modifies
    car = ord(c.upper())
    car += k
    while car>90:
        car -= 26
    while car<65:
        car += 26
    return chr(car)

def cesar(message,d):
    # effectue le decalage d sur les caracteres de message
    chiffre=''
    for c in message:
        chiffre += decalage(c,-d)
    return chiffre

def freq(texte):
    chaine = que_des_majuscules(texte,0)
    frequences = [0]*26
    n = len(chaine)
    for c in chaine:
        frequences[ord(c)-65] += 1
    return frequences

def cle_probable(texte,longueur_cle):
    cle = ""
    k = 0
    for k in range(longueur_cle):
        partiel = ""
        j = 0
        while k+j < len(texte):
            partiel += texte[k+j]
            j += longueur_cle
        long_message = len(partiel)
        ecart_min = 100000000
        for d in range(26):
            ecart = 0.0
            chiffre = cesar(partiel,d)
            frequences = freq(chiffre)
            for i in range(26):
                ecart += abs(frequences[i]/long_message-histogramme[i])
            if ecart<ecart_min:
                ecart_min = ecart
                decalage = d
        cle += chr(decalage+65)
    return cle

def vigenere(message,cle,crypte):
    # effectue le decalage en fonction de la cle sur les caracteres de message
    n = 0
    chiffre=''
    for c in message:
        k = ord(cle[n%len(cle)])-65
        if crypte:
            chiffre += decalage(c,k)
        else:
            chiffre += decalage(c,-k)
        n+=1
    return chiffre

histogramme = [0.084,0.0106,0.0303,0.0418,0.1726,0.0112,0.0127,0.0092,0.0734,0.0031,0.0005,0.0601,0.0296,0.0713,0.0526,0.0301,0.0099,0.0655,0.0808,0.0707,0.0574,0.0132,0.0004,0.0045,0.0030,0.0012]

# tests
texte = """cbntjdefhccavtvfdvfbpufdftgnzqwkysdufwcnfjguznzutvtlveonybyvldcf
upipfovtxgdglxfdcdgfibyvncywjogyhtrmtvpofkippewnzupgewykfrtthpvo
dctrleudqfjpeuogdsnifeuzincfdgwzpjfokdhtehfgoswrtegroyfhccavtvrf
kqotkqludsczolrpfnlvyopgdrhpflbdlolwefpdfduluprmztdefvmlecmakprt
ldszfcgyrfenpudorvjykyhpcmtitpwvblwefphvpsfwovecqthpcmpgdhfkjwkd
spufawtgwroekbitkfxctgnvsectbpjepupgxvusqosdcfdrwidznaqchleupunc
xdfwcnfjguzicoayjpcdmxvuckbipubegyhovmlhtbolwtprhtvnputsncf
"""
texte_maj = que_des_majuscules(texte,0)
longueur = longueur_cle(texte_maj)
if longueur==0:
    print("la longueur de la clÃ© n'a pas pu Ãªtre dÃ©terminÃ©e")
else:
    print("longueur probable de la clé :",longueur)
    cle = cle_probable(texte_maj,longueur)
    print(cle)
    texte_decode = vigenere(texte_maj,cle,False)
    print(texte_decode)