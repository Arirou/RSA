def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:  # Si l'exposant est impair
            result = (result * base) % mod
        exp = exp // 2  # Division entière de l'exposant par 2
        base = (base * base) % mod
    return result

def rsa_encrypt_char(character, e, n):
    char_code = ord(character)  # Convertit le caractère en code ASCII
    encrypted = mod_exp(char_code, e, n)  # Applique RSA
    return encrypted

def rsa_decrypt_char(cipher_value, d, n):
    decrypted_code = mod_exp(cipher_value, d, n)  # Applique RSA
    return chr(decrypted_code)  # Convertit le code ASCII en caractère

def rsa_encrypt_message(message, e, n):
    encrypted_message = []
    for char in message:
        encrypted_char = rsa_encrypt_char(char, e, n)
        encrypted_message.append(encrypted_char)
    return encrypted_message

def rsa_decrypt_message(cipher_values, d, n):
    decrypted_message = ""
    for cipher_value in cipher_values:
        decrypted_char = rsa_decrypt_char(cipher_value, d, n)
        decrypted_message += decrypted_char
    return decrypted_message

# Exemple d'utilisation :
if __name__ == "__main__":
    # Clé publique (e, n)
    e = 17  # Exposant public
    n = 3233  # Module RSA (produit de deux nombres premiers)

    # Clé privée (d, n)
    d = 2753  # Exposant privé

    while True:
        # Demander à l'utilisateur de saisir le message à crypter
        message = input("Entrez la phrase à crypter : ")

        # Chiffrement
        encrypted_message = rsa_encrypt_message(message, e, n)
        print("Message chiffré :", encrypted_message)

        # Déchiffrement
        decrypted_message = rsa_decrypt_message(encrypted_message, d, n)
        print("Message déchiffré :", decrypted_message)

        # Demander si l'utilisateur souhaite crypter et déchiffrer un autre message
        another = input("Voulez-vous crypter et déchiffrer un autre message ? (oui/non) : ")
        if another.lower() != "oui":
            print("Au revoir !")
            break
