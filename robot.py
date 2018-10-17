# -*-coding:Utf-8 -*
"""
    Ce module contient la classe Robot.
"""


class Robot:
    """ classe Robot """

    def __init__(self, coordonnees):
        self.symbole = "X"
        # self.nom = "nom"
        # coordonnees est un tuple (abscisse, ordonnee)
        self.abscisse = coordonnees[0]
        self.ordonnee = coordonnees[1]
        self.obstacle = " "

    def __repr__(self):
        return "<Robot {0} : abscisse = {1} - ordonnee = {2} sur {3} ".format(
            self.symbole, self.abscisse, self.ordonnee, self.obstacle
        )

    def __str__(self):
        return self.symbole

    def deplacer(self, nouvelle_coordonnees, obstacle):
        self.abscisse = nouvelle_coordonnees[0]
        self.ordonnee = nouvelle_coordonnees[1]
        self.obstacle = obstacle

    @property
    def coordonnees(self):
        return(self.abscisse, self.ordonnee)
