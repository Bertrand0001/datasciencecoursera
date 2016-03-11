__author__ = 'bertr'
from random import randint
#################################################################
#                                                               #
# Ce programme est un programme similaire au jeu "Le juste prix #
#                                                               #
# ------------------------------------------------------------- #
# Prof. Dr. Bertrand Loison, cours d'introduction Python I      #
# 2015                                                          #
#################################################################

# Fixation des valeurs des variables environnementales
total_essai=1
essai=0

# Détermination du niveau de jeu
print("Bonjour, bienvenue au jeu du juste prix")
print("Introduisez le niveau de difficulté du jeu")
print("")
print("1 = Le nombre est compris entre 0 et 100")
print("2 = Le nombre est compris entre 0 et 200")
print("3 = Le nombre est compris entre 0 et 300")
print("")
niveauJeu=input()
niveauJeu = eval(niveauJeu)
# Détermination de la valeur aléatoire en fonction du niveau de jeu
if niveauJeu ==1:
    nombreAleatoire = randint(0, 100)
elif niveauJeu==2:
    nombreAleatoire = randint(0, 200)
else:
    nombreAleatoire = randint(0, 300)

if niveauJeu ==1:
    while essai != nombreAleatoire:
        print("Saisissez votre nombre")
        essai=input()
        essai = eval(essai)
        total_essai=total_essai+1
        if essai > nombreAleatoire:
            print("Votre chiffre est trop grand")
        elif essai < nombreAleatoire:
            print("Votre chiffre est trop petit")
        else:
            print("Bravo, vous avez trouvé le juste prix: ", essai)
            print("Il aura fallu", total_essai, "essai(s) pour parvenir au juste prix")
elif niveauJeu ==2:
    while essai != nombreAleatoire:
        print("Saisissez votre nombre")
        essai=input()
        essai = eval(essai)
        total_essai=total_essai+1
        if essai > nombreAleatoire:
            print("Votre chiffre est trop grand")
        elif essai < nombreAleatoire:
            print("Votre chiffre est trop petit")
        else:
            print("Bravo, vous avez trouvé le juste prix: ", essai)
            print("Il aura fallu", total_essai, "essai(s) pour parvenir au juste prix")
else:
    while essai != nombreAleatoire:
        print("Saisissez votre nombre")
        essai=input()
        essai = eval(essai)
        total_essai=total_essai+1
        if essai > nombreAleatoire:
            print("Votre chiffre est trop grand")
        elif essai < nombreAleatoire:
            print("Votre chiffre est trop petit")
        else:
            print("Bravo, vous avez trouvé le juste prix: ", essai)
            print("Il aura fallu", total_essai, "essai(s) pour parvenir au juste prix")
print("\nLe jeu est terminé")

