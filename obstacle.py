# -*-coding:Utf-8 -*
"""
    Ce module contient la classe Obstacle.
"""


class Obstacle:
    """ classe représentant un obstacle """

    def __init__(self, symbole, nom, type_de_blocage, message):
        self.symbole = symbole
        self.nom = nom
        self.type_de_blocage = type_de_blocage
        self.message = message

    def __repr__(self):
        return "<Obstacle {0} : Obstacle {1} de type {2} - {3}>".format(
            self.symbole, self.nom, self.type_de_blocage, self.message)

    def __str__(self):
        return self.symbole


class Chemin(Obstacle):
    """ classe représentant un chemin """

    def __init__(self):
        self.symbole = " "
        self.nom = "chemin"
        self.type_de_blocage = "non bloquant"
        self.message = "Vous poursuivez sur le chemin"


class Porte(Obstacle):
    """ classe représentant une porte """

    def __init__(self):
        self.symbole = "."
        self.nom = "porte"
        self.type_de_blocage = "non bloquant"
        self.message = "Vous ouvrez une porte et la franchissez"
        # A l'avenir, possibilité d'agir sur une porte?
        self.statut = "ouverte"

    def ouvrir(self):
        pass

    def fermer(self):
        pass


class Mur(Obstacle):
    """ classe représentant un mur """

    def __init__(self):
        self.symbole = "O"
        self.nom = "mur"
        self.type_de_blocage = "bloquant"
        self.message = "Devant vous se dresse un mur, impossible d'aller plus loin"


class Sortie(Obstacle):
    """ classe représentant un mur """

    def __init__(self):
        self.symbole = "U"
        self.nom = "sortie"
        self.type_de_blocage = "sortie"
        self.message = "Félicitations, vous venez de trouver la sortie"
