# -*-coding:Utf-8 -*
"""
    Ce module contient la classe Robot.
"""


class Robot:
    """ classe Robot """

    def __init__(self, nom, coordonnees):
        self.nom = nom
        self.coordonnees = coordonnees

    def __repr__(self):
        return "<Robot {0} : abscisse = {1} - ordonnee = {2} ".format(
            self.nom, self.coordonnees.abscisse, self.coordonnees.ordonnee
        )
