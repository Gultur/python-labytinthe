# -*-coding:Utf-8 -*
"""
    Ce module contient la classe Coordonnees.
"""


class Coordonnees:
    """ classe Coordonnees """

    def __init__(self, abscisse, ordonnee):
        self.abscisse = abscisse
        self.ordonnee = ordonnee
        # A l'avenir, plusieurs étages?
        self.etage = 1

    def __repr__(self):
        return "<Coordonnees : abscisse = {0}, ordonnee = {1}>".format(
            self.abscisse, self.ordonnee
        )

    def __add__(self, other):
        return (self.abscisse + other.abscisse, self.ordonnee + other.ordonnee)

    def __sub__(self, other):
        return (self.abscisse - other.abscisse, self.ordonnee - other.ordonnee)
