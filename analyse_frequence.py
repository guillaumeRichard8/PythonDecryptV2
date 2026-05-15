import collections
import string
import filtrage


def analyser_frequence(message, opt = 0): 
    # avec graph opt = 0 et sans graph opt = 1
    # option avec ou sans ponctuation à ajouter
    
    # 1. Mise en minuscule et filtrage (on ne garde que les lettres de a-z)
    message = message.lower()
    lettres_valides = filtrage.filtrer_uniquement_lettres(message)
    
    total_lettres = len(lettres_valides)
    
    if total_lettres == 0:
        return "Aucune lettre trouvée dans le message."

    # 2. Comptage des occurrences
    compteur = collections.Counter(lettres_valides)
    print(f"compteur : {compteur} \n")
    
    # 3. Tri des lettres par ordre alphabétique
    resultats_tries = sorted(compteur.items())
    print(f"resultats_tries : {resultats_tries} \n")

    print(f"--- Résultats de l'analyse ({total_lettres} lettres au total) ---")
    print(f"{'Lettre':<10} | {'Nombre':<10} | {'Fréquence (%)':<10}")
    print("-" * 40)

    for lettre, nombre in resultats_tries:
        pourcentage = (nombre / total_lettres) * 100
        print(f"{lettre.upper():<10} | {nombre:<10} | {pourcentage:>12.2f}%")

    # Graph option :
    if opt == 0 :
        print(f"--- Résultats de l'analyse ({total_lettres} lettres au total) --- : Opt Graph")
        print(f"{'Lettre':<10} | {'Nombre':<10}")
        print("-" * 40)
        for c in string.ascii_lowercase :
            res = " "  # On réinitialise res pour cette lettre
            for lettre, nombre in resultats_tries:
                if c == lettre :
                    res = "*" * nombre
                    break 
                    # On a trouvé la lettre, on peut sortir de la boucle interne
            print(f"{c:<10} | {res}")
           
    return 0


# Exemple d'utilisation
# texte_de_test = """L'intelligence artificielle est une technologie en pleine évolution. 
# Elle transforme notre façon de travailler et de communiquer. Ce texte est interessant à plus d'un égard.
# """
# analyser_frequence(texte_de_test)

