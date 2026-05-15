import collections
import string
import locale

import filtrage

import vigenere

import distance_trigrammes

import analyse_frequence

def splitting(text_cipher, ncol):
    # On nettoie le texte pour ne garder que les lettres (optionnel selon ton besoin)
    text_cipher = filtrage.filtrer_uniquement_lettres(text_cipher)
    
    MAXCHAR = 500 # MAX_TOTAL_CHAR = ncol * MAXCHAR
    length = len(text_cipher)
    print(f"Length = {length}")
    
    # Initialisation d'un tableau de 'ncol' listes vides
    tab = [[] for _ in range(ncol)]
    #tab = [[] for col in range(ncol)]
    
    # Distribution des caractères dans les colonnes
    for k in range(length):
        i = k % ncol  # k modulo ncol
        tab[i].append(text_cipher[k])
        
    # On retourne les colonnes sous forme de chaînes de caractères
    return ["".join(col) for col in tab]


# Exemple d'utilisation :
# Ton texte ici :
texte_de_test = """Le code est secret ! Vive Cesar !
J'ai fait des exercices après mon cours de crypto à la fac, mais dans ces exercices, bien sûr, je connaissais l'algorithme derrière.
Je ne demande pas "comment casser un message chiffré en RSA 4096 ?", mais "quels sont les vrais processus utilisés pour forcer un code quand tu n'y connais rien ?". Peut-être un truc genre chiffre de César, utilisé par des gens pas pros chez eux, ou peut-être un jeu/quiz dans un magazine.
Qu'est-ce que font les pros ? Ils essaient juste toutes les techniques possibles ? Par quoi tu commencerais ? Quels logiciels sont utilisés professionnellement ? Y a-t-il des alternatives pour essayer à la maison ?
En d'autres termes, qu'est-ce que tu ferais concrètement si tu voulais te lancer un défi genre "essaie de casser ce code !!!" ? """

cle="PYTHON"

texte_de_test = filtrage.filtrer_uniquement_lettres(texte_de_test)

texte_cipher = vigenere.vigenere_cipher(texte_de_test, cle)

print(f"Choix 1 : distance_trigrammes")
print(f"Choix 2 : SPLIT et analyses de frequences")
print(f"Choix 3, autres ou Quit pour quitter.")
print()

choix = int(input("Choix ? "))

match(choix):
    
    case 1 :
        distance_trigrammes.distance_trigrammes(texte_cipher)
        
    case 2 :
        print()
        print("Longueur supposée de la clef de chiffrement ?")
        ncol = int(input())
        colonnes = splitting(texte_cipher, ncol)
        print("*"*100)
        print("*"*100)
        for i in range(ncol):
            print(f"\n Colonne n° = {i+1}")
            analyse_frequence.analyser_frequence(colonnes[i])
            print("*" *100)
            
    case _:
        print("Option invalide, veuillez choisir 1 ou 2.")
