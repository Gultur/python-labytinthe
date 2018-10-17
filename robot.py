# -*-coding:Utf-8 -*
"""
    Ce module contient la classe Robot.
"""


class Robot:
    """ classe Robot """

    def __init__(self, coordonnees):
        self.symbole = "X"
        # self.nom = "nom"
        self.position = coordonnees

    def __repr__(self):
        return "<Robot {0} : abscisse = {2} - ordonnee = {3} ".format(
            self.symbole, self.position.abscisse, self.position.ordonnee
        )
