__author__ = 'bertr'

# For
for i in range(50):
    print(i)

#while True :
 #   print("Je suis une boucle infinie !")

print("Entrez des données. (Entrée vide pour arrêter).")
boucler = True
while boucler :
    entree = input()
    if entree == "" :
        print("Nous avons terminé !")
        boucler = False
    else :
        print("Vous avez entré :",entree)

print("Entrez des données. (Entrée vide pour arrêter).")
while True :
    entree = input()
    if entree == "" :
        print("Nous avons terminé !")
        break
    else :
        print("Vous avez entré :",entree)

unNombre = 0
while unNombre < 50 :
     unNombre += 1
     if unNombre % 2 != 0:
          continue
     print("unNombre =",unNombre)

unNombre = 0
while unNombre < 50 :
    unNombre += 1
    print("J'apprends à compter :",unNombre)

#Travail sur les conditions SI ELIF et ELSE

print("Bonjour !")
nombre = input("Merci d'introduire un nombre: ")
if nombre > "20":
    print("Le nombre introduit est plus grand que 20")
elif nombre=="20":
    print("Le nombre introduit est 20")
else :
    print("Le nombre introduit est plus petit que 20")

#Travail sur les blocs de codes

print("Travail sur les blocs de code !")
nombre = input("Merci d'introduire un nombre: ")
if nombre > "0":
    print("1er bloc de code")
    if nombre > "3":
        print("nombre > 3")
    print ("Fin du 2eme bloc de code")
else:
    print("Nombre inferieur a 0")

#Travail sur les booleens

print("Travail sur les fonctions booléennes")

