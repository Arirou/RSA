import ast

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:  # Si l'exposant est impair
            result = (result * base) % mod
        exp = exp // 2  # Division entière de l'exposant par 2
        base = (base * base) % mod
    return result

def rsa_decrypt_char(cipher_value, d, n):
    decrypted_code = mod_exp(cipher_value, d, n)  # Applique RSA
    return chr(decrypted_code)  # Convertit le code ASCII en caractère

def get_possible_decryptions(cipher_value, d, n):
    # On suppose qu'une seule valeur déchiffrée est valide.
    # Cette fonction pourrait être adaptée pour rechercher plusieurs solutions possibles si nécessaire.
    decrypted_char = rsa_decrypt_char(cipher_value, d, n)
    return [decrypted_char]  # Une seule solution par défaut

def generate_all_possible_messages(encrypted_message, d, n, current_message, all_messages):
    if len(encrypted_message) == 0:
        all_messages.append(current_message)
        return

    # Prendre le premier élément de la liste des valeurs chiffrées
    current_cipher_value = encrypted_message[0]

    # Obtenir les décryptions possibles
    possible_decryptions = get_possible_decryptions(current_cipher_value, d, n)

    # Essayer toutes les décryptions possibles
    for decryption in possible_decryptions:
        generate_all_possible_messages(encrypted_message[1:], d, n, current_message + decryption, all_messages)

def rsa_decrypt_all_messages(encrypted_message, d, n):
    all_messages = []
    generate_all_possible_messages(encrypted_message, d, n, "", all_messages)
    return all_messages

# Exemple d'utilisation :
if __name__ == "__main__":
    # Clé privée (d, n)
    d = 2753  # Exposant privé
    n = 3233  # Module RSA (produit de deux nombres premiers)

    while True:
        # Demander à l'utilisateur d'entrer le message crypté
        encrypted_message_input = input("Entrez le message crypté (valeurs séparées par des espaces ou une liste entière) : ")

        try:
            # Convertir l'entrée en une liste d'entiers, en traitant les crochets et les virgules
            encrypted_message = ast.literal_eval(encrypted_message_input)
            if not isinstance(encrypted_message, list):
                raise ValueError
            encrypted_message = [int(x) for x in encrypted_message]
        except (ValueError, SyntaxError):
            print("Format invalide, veuillez entrer la liste sous forme correcte.")
            continue

        # Trouver toutes les phrases possibles
        possible_messages = rsa_decrypt_all_messages(encrypted_message, d, n)

        # Afficher toutes les possibilités
        for message in possible_messages:
            print("Message possible :", message)

        # Demander si l'utilisateur souhaite décrypter un autre message
        another = input("Voulez-vous décrypter un autre message ? (oui/non) : ")
        if another.lower() != "oui":
            print("Au revoir !")
            break
