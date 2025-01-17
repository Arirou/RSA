def brute_force_all_rsa_with_dictionary(ciphertext, e, n, dictionary_file):
    """Effectue une attaque brute force sur RSA et retourne toutes les phrases valides en français."""
    # Charger le dictionnaire depuis le fichier
    with open(dictionary_file, "r", encoding="utf-8") as file:
        dictionary = set(word.strip().lower() for word in file)

    possible_sentences = []

    # Essayer toutes les combinaisons possibles de décryptage
    def decrypt_message(ciphertext, partial_message=""):
        if not ciphertext:
            # Découper la phrase pour valider les mots individuellement
            words = partial_message.lower().split(" ")
            if all(word in dictionary for word in words):
                possible_sentences.append(partial_message)
            return

        cipher_char = ciphertext[0]
        # Tester toutes les valeurs possibles pour m (message clair)
        for m in range(n):  # m est compris entre 0 et n-1
            if pow(m, e, n) == cipher_char:
                decrypted_char = chr(m)
                decrypt_message(ciphertext[1:], partial_message + decrypted_char)

    # Lancer le décryptage
    decrypt_message(ciphertext)

    return possible_sentences


# Exemple d'utilisation
if __name__ == "__main__":
    # Clé publique (e, n)
    e = 17  # Exposant public
    n = 3233

    # Message chiffré (exemple)
    encrypted_message = [745, 1632, 1992, 1369, 1313, 2412, 2271, 3179, 1313, 2412, 1313, 1992, 2271, 1632, 2235, 2923, 1313, 1992, 2160, 2235, 1992, 612, 1632, 3179, 2235]

    # Fichier contenant les mots français
    dictionary_file = "ods5.txt"

    # Attaque brute force
    valid_sentences = brute_force_all_rsa_with_dictionary(encrypted_message, e, n, dictionary_file)

    # Affichage des résultats
    if valid_sentences:
        print("Phrases décryptées par brute force :")
        for sentence in valid_sentences:
            print("-", sentence)
    else:
        print("Aucune phrase française trouvée.")
