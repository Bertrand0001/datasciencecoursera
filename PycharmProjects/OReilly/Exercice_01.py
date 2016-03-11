__author__ = 'bertr'

#Cet exercice montre comment stocker les noms et les notes des étudiants

#On utilise le concept de list
notes=["Raymond", 92, "Cynthia", 83, "Terrill", 64, "Jennifer", 75, "Clayton", 88, "David", 91, "Bryan", 100, "Danny", 99]
print(notes)
temp = notes[0]+" "+str(notes[1])
print(temp)
#Montre comment créer un "format string"
record="%s:%.2f" %(notes[0], notes[1])
print(record)

#Montre la note en fonction du nom
nom=input()
if nom ==notes[0]:
    print(notes[0], notes[1])
elif nom ==notes[2]:
    print(notes[2], notes[3])
elif nom ==notes[4]:
    print(notes[4], notes[1])
elif nom ==notes[6]:
    print(notes[6], notes[7])
elif nom ==notes[8]:
    print(notes[8], notes[9])
elif nom ==notes[10]:
    print(notes[10], notes[11])
elif nom ==notes[12]:
    print(notes[12], notes[13])
elif nom ==notes[14]:
    print(notes[14], notes[14])
else:
    print("Le nom que vous avez entré n'existe pas")

#On utilise le concept de dictionnaire
notes={"Raymond":92, "Cynthia":83, "Terrill":64, "Jennifer":75, "Clayton":88, "David":91, "Bryan":100, "Danny":99}
print(notes)
print("Voici la note de Bryan:", notes["Bryan"])
print("Voici la liste des étudiants: ",notes.keys())
print("Voici la liste des notes: ",notes.values())

#On constate que le dictionnaire est plus puissant que la liste car il permettra ultérieurement de réaliser
#des opérations directement sur les variables