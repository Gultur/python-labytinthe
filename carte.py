# -*-coding:Utf-8 -*
"""
    Ce module contient la classe Carte.
"""

from collections import namedtuple
import donnees


class Carte:

    """
        La classe Carte permet de générer un dictionnaire représentant le tracé
        du Labyrinthe
        Le fichier texte de la carte est chargé via cette classe
    """

    def __init__(self, nom):
        """
            construit une Carte en allant chercher le fichier txt
            parametre : le nom de la carte

        """
        self.nom = nom
        self.plan = self.charger_fichier_carte(nom)

    def __repr__(self):
        """
            Affiche les infos de la Carte, nom et dictionnaire
        """
        return "<Carte {0}, de taille {1}> \n {2}".format(
            self.nom, self.get_taille(), self.plan)

    def __str__(self):
        """
            affiche la carte à l'écran
            utilise l'attribut plan pour l'affichage
        """
        ligne = 0
        affichage = "Carte {0} \n".format(self.nom)
        for coordonnees, obstacle in self.plan.items():
            if coordonnees.ordonnee > ligne:
                affichage += ("\n{0}".format(obstacle))
                ligne += 1
            else:
                affichage += obstacle
        return affichage + "\n"

    def get_taille(self):
        """
            Determine la taille de la carte
            Utilise l'attribut plan
            Retourne : namedtuple(colonnes,lignes) de ses dimensions
        """
        Taille = namedtuple('Taille', ['colonnes', 'lignes'])
        taille = Taille(
            max((coordonnees.abscisse) + 1 for coordonnees in self.plan),
            max((coordonnees.ordonnee) + 1 for coordonnees in self.plan)
            )
        return taille

    def get_position_robot(self):
        """
            recupère la position du robot sur la carte initiale
            retourne : tuple de position
        """
        # on recupère le symbole utilisé pour le robot

        symbole_robot = self.get_symbole("robot")
        for position, obstacle in self.plan.items():
            if obstacle == symbole_robot:
                return position
        return None

    def get_obstacle(self, position):
        """
            renvoie l'obstacle situé à une position donnée
            parametres: position
            retourne: l'obstacle à analyser
        """
        if position not in self.plan:
            return "La position est en dehors de la carte"
        return self.plan[position]

    def deplacer_robot(self, obstacle_initial, nouvelle_position):
        """
            deplace le robot sur la cartes
            parametres : obstacle sur lequel est le robot
                         nouvelle position du robot
            retourne : dictionnaire du plan mis à jour
        """
        self.plan[self.get_position_robot()] = obstacle_initial
        self.plan[nouvelle_position] = self.get_symbole("robot")
        return self.plan

    @staticmethod
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
        Coordonnees = namedtuple('Coordonnees', ['abscisse', 'ordonnee'])
        nom_fichier_carte = "{0}/{1}.txt".format(
            donnees.repertoire_des_cartes, nom_carte)

        with open(nom_fichier_carte, 'r') as fichier:
            for line in fichier.readlines():
                for abscisse, obstacle in enumerate(line):
                    if obstacle != "\n":
                        case = Coordonnees(abscisse, ordonnee)
                        carte[case] = obstacle
                    else:
                        ordonnee += 1
        return carte

    @staticmethod
    def get_symbole(nom):
        """
            permet de récuperer le symbole d'un obstacles
            parametre : nom du symbole
            retourne : symbole

            sera utile en cas de changement de symbole des obstacles
        """
        for key, value in donnees.obstacles.items():
            if value.nom == nom:
                return key
        return "No key"

    @staticmethod
    def get_infos_obstacle(symbole):
        """
            permet d'afficher les informations d'un obstacle
            c'est à dire son effet et le message accompagnant sa découverte
            parametre : le symbole représenant l'obstacles
            retourne : namedtuple d'informations
        """
        return donnees.obstacles[symbole]
