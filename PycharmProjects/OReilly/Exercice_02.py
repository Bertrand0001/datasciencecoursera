__author__ = 'bertr'

import sys
sys.stdout.write("Hello\n")

#On écrit dans un fichier en redirigeant l'output de print
sys.stdout= open("text.dat","a")
print("hello")
#exit()

#Une autre manière de rediriger l'output de print
textfile=open("text1.dat","a")
textfile.write("Bonjour, c'est moi")
textfile.close()
print("ceci est imprimé à l'écran est pas dans le fichier")
