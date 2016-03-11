#__author__ = 'bertr'

#Ecriture dans un fichier test.txt n'existant pas encore
fichier = open("test.txt","w")
for indice in range(30):
    fichier.write("C'est un essai d'écriture dans un fichier" + str(indice+1) + "!\n")
    print("Ligne", str(indice+1))
fichier.close()

#Lecture du contenu du fichier test.txt
fichier = open("test.txt","r")
for ligne in fichier :
    print(ligne)
fichier.close()