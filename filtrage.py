import string
import unicodedata

def filtrer(message, opt="FRENCH"): # default FRENCH option or ENGLISH, ... for later
    #  0. Mise en minuscule
    message = message.lower()
    
     # 1. Normalisation NFD : sépare la lettre de son accent (ex: 'é' devient 'e' + '´')
    forme_decompo = unicodedata.normalize('NFD', message)
    
    # 2. On ne garde que les caractères qui ne sont pas des marques d'accent (Mn = Non-Spacing Mark)
    texte_sans_accents = "".join(c for c in forme_decompo if unicodedata.category(c) != 'Mn')
    
    # 3. On remet tout en minuscules (ascii_lowercase)
    return texte_sans_accents.lower()


def filtrer_uniquement_lettres(texte): # enlève la ponctuation et les accents
    # Nettoyage des accents d'abord
    texte = filtrer(texte)
    # On ne garde que ce qui est dans string.ascii_lowercase
    return "".join(c for c in texte if c in string.ascii_lowercase)


# Exemple d'utilisation :
# str = "azertyuiopqsdfghjklmwxcvbn,;:!^$ù*<>;aàâ;éêè;iïî;oôö;uùû;yÿ;œ"
# print(f"str     = {str}")
# print(f"filtrer = {filtrer(str)}")
# print(f"lettres = {filtrer_uniquement_lettres(str)}")

