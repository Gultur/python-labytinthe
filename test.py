from collections import namedtuple
from obstacle import Obstacle, Mur

carte = {}
ordonnee = 0
Coordonnees = namedtuple('Coordonnees', ['abscisse', 'ordonnee'])


for i in range(6):

    case = Coordonnees(i, i)
    carte[case] = Mur()

for case in carte.values():
    print(case)
