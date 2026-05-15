def vigenere_cipher(text, key, decrypt=False):
    """
    Chiffre ou déchiffre un texte en utilisant le carré de Vigenère.
    """
    result = ""
    key = key.upper()
    key_index = 0
    
    # On définit le mode (1 pour chiffrement, -1 pour déchiffrement)
    mode = -1 if decrypt else 1
    
    for char in text:
        if char.isalpha():
            # Gestion de la casse (Majuscule ou Minuscule)
            start = ord('A') if char.isupper() else ord('a')
            
            # Récupération de la valeur de décalage via la clé (0-25)
            shift = ord(key[key_index % len(key)]) - ord('A')
            
            # Formule de Vigenère : (Position_Lettre + (Mode * Décalage)) % 26
            # On utilise (char_val - start) pour travailler sur une base 0-25
            char_val = ord(char) - start
            new_val = (char_val + (mode * shift)) % 26
            
            result += chr(new_val + start)
            
            # On n'avance dans la clé que si on a traité une lettre
            key_index += 1
        else:
            # On garde les espaces et la ponctuation intacts
            result += char
            
    return result


# --- Exemple d'utilisation ---
# message_original = """Le code est secret ! Vive Cesar !

# J'ai fait des exercices après mon cours de crypto à la fac, mais dans ces exercices, bien sûr, je connaissais l'algorithme derrière.

# Je ne demande pas "comment casser un message chiffré en RSA 4096 ?", mais "quels sont les vrais processus utilisés pour forcer un code quand tu n'y connais rien ?". Peut-être un truc genre chiffre de César, utilisé par des gens pas pros chez eux, ou peut-être un jeu/quiz dans un magazine.

# Qu'est-ce que font les pros ? Ils essaient juste toutes les techniques possibles ? Par quoi tu commencerais ? Quels logiciels sont utilisés professionnellement ? Y a-t-il des alternatives pour essayer à la maison ?

# En d'autres termes, qu'est-ce que tu ferais concrètement si tu voulais te lancer un défi genre "essaie de casser ce code !!!" ? 


# """
# cle = "PYTHON"

# # Chiffrement
# message_chiffre = vigenere_cipher(message_original, cle)
# print(f"Original : {message_original}")
# print(f"Chiffré  : {message_chiffre}")

# # Déchiffrement
# message_dechiffre = vigenere_cipher(message_chiffre, cle, decrypt=True)
# print(f"Déchiffré : {message_dechiffre}")




