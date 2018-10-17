from coordonnees import Coordonnees
from robot import Robot
import donnees


def charger_fichier_carte(nom_carte):
    """
    trabsforme une carte issue d'un fichier de base en dictionnaire
    parametre : tuple (nom/type) de la carte à charger
    retourne : dictionnaire de la carte
    => clé : coordonnees(abscisses, ordonnees)
    => valeur : obstacle
    """
    carte = {}
    ordonnee = 0
    # Coordonnees = namedtuple('Coordonnees', ['abscisse', 'ordonnee'])
    nom_fichier_carte = "{0}/{1}.txt".format(
    donnees.repertoire_des_cartes, nom_carte)

    with open(nom_fichier_carte, 'r') as fichier:
        for line in fichier.readlines():
            for abscisse, obstacle in enumerate(line):
                if obstacle == "\n":
                    ordonnee += 1
                elif obstacle == "X":
                    case = Coordonnees(abscisse, ordonnee)
                    carte[case] = Robot(case)
                else:
                    case = Coordonnees(abscisse, ordonnee)
                    carte[case] = obstacle
    return carte



carte_chargee = charger_fichier_carte("facile")

ligne = 0
affichage = "Test"
for coordonnees, obstacle in carte_chargee.items():
    if coordonnees.ordonnee > ligne:
        affichage += ("\n{0}".format(obstacle))
        ligne += 1
    else:
        affichage += str(obstacle)
print(affichage + "\n")

print(str("bonjour"))
