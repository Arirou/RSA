import string

# Générer la matrice
alphabet = string.ascii_uppercase
n = len(alphabet)

# Construction de la matrice
matrice = [[alphabet[(i + j) % n] for j in range(n)] for i in range(n)]

# Afficher la matrice
for ligne in matrice:
    print(" ".join(ligne))

def chiffrer(message, cle):
    newMessage = ""
    crypted = ""
    indexCle = 0
    for letter in message:
        if letter == " ":
            newMessage += " "
        else:
            newMessage += cle[indexCle]
            if indexCle != len(cle) - 1:
                indexCle += 1
            else:
                indexCle = 0
    print("Message chiffré avec la clé : ", newMessage)
    for i in range(len(newMessage)):
        if newMessage[i] == " ":
            crypted += " "
        else:
            ascii = (ord(newMessage[i]) + ord(message[i]) - 2 * ord("a")) % 26 + ord("a")
            crypted += chr(ascii)
    print(crypted)
    return

def main():
    chiffrer("je suis un message", "secret")
    quitter = input("Voulez-vous quitter ? (oui/non) : ")
    if quitter.lower() != 'oui':
        main()


main()
