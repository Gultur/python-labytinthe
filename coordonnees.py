# -*-coding:Utf-8 -*
"""
    Ce module contient la classe Coordonnees.
"""


class Coordonnees:
    """ classe Coordonnees """

    def __init__(self, abscisse, ordonnee):
        self.abscisse = abscisse
        self.ordonnee = ordonnee

    def __repr__(self):
        return "<Coordonnees : abscisse = {0}, ordonnee = {1}>".format(
            self.abscisse, self.ordonnee
        )
