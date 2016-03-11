__author__ = 'bertr'

HeureHebdo=41
HeuresOuvrées=HeureHebdo*47
SalaireAnnuel=200000
SalaireHoraire=SalaireAnnuel/HeuresOuvrées
print(HeuresOuvrées)
print(SalaireHoraire)
interessant=(HeuresOuvrées<40) and (SalaireAnnuel>=200000)
print(interessant)
print(not(interessant))
