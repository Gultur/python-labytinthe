# -*-coding:Utf-8 -*
"""
    Ce module contient la classe Labyrinthe.
"""
from collections import namedtuple
import pickle
import donnees
from carte import Carte


class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, carte_a_charger):
        """
            Un labyrinthe peut être construit à partir d'une nouvelle partie
            ou d'une sauvegarde existante
            parametre : tuple (nom / type[nouvelle partie/ sauvegarde])
        """

        self.carte = Carte(carte_a_charger.nom)

        if carte_a_charger.type == "Nouvelle partie":
            self.robot = self.carte.get_position_robot()
            self.obstacle = " "
        else:
            # pickle n'aime pas les namedtuple, les sauvegardes
            # ne contiennent donc pas des instances completes
            # je suis preneur de solutions pour gerer les namedtuple
            # via pickle (je pourrai passer par des tuples classiques
            # mais c'est tellement moins lisible)
            # on recréé une instance à partir des infos de sauvegarde
            sauvegarde = self.charger_partie(carte_a_charger.nom)
            Coordonnees = namedtuple('Coordonnees', ['abscisse', 'ordonnee'])
            self.robot = Coordonnees(sauvegarde[1][0], sauvegarde[1][1])
            self.obstacle = sauvegarde[2]
            self.carte.deplacer_robot(" ", self.robot)

    def __repr__(self):
        """
            redefinit la methode __repr__
            affiche les informations du labyrinthe
        """

        return "<Labyrinthe carte={0} robot={1} obstacle={2}>".format(
            self.carte.nom, self.robot, donnees.obstacles[self.obstacle].nom)

    def __getstate__(self):
        """
            methode pour gerer la récupération de donnees de Pickle
            non utilisée actuellement car conflict avec les namedtuple
        """
        robot_pickle = (self.robot.abscisse, self.robot.ordonnee)
        return (self.carte.nom, robot_pickle, self.obstacle)

    def __setstate__(self, lab):
        """
            methode pour gerer la création de donnees de Pickle
            non utilisée actuellement car conflict avec les namedtuple
        """
        nom_carte, tuple_robot, self.obstacle = lab
        self.carte = Carte(nom_carte)
        Coordonnees = namedtuple('Coordonnees', ['abscisse', 'ordonnee'])
        self.robot = Coordonnees(tuple_robot[0], tuple_robot[1])
        self.carte.deplacer_robot(" ", self.robot)
        print(self)

    def effectuer_deplacements(self, deplacements):
        """
            Verifie chaque case de deplacement et effectue le mouvement
            s'il est possible
            parametre: le déplacement (orientation, nombre de cases)
        """
        # on définit des coordonnees de mouvement selon l'axe cardinal
        Coordonnees = namedtuple("Coordonnees", ["abscisse", "ordonnee"])
        if deplacements.direction.upper() == "N":
            mouvement = Coordonnees(0, -1)
        elif deplacements.direction.upper() == "S":
            mouvement = Coordonnees(0, 1)
        elif deplacements.direction.upper() == "E":
            mouvement = Coordonnees(1, 0)
        elif deplacements.direction.upper() == "O":
            mouvement = Coordonnees(-1, 0)

        # on créé une boucle pour gerer les deplacements case après case
        for i in range(1, deplacements.cases + 1):
            obstacle_suivant = self.carte.get_obstacle(
                (self.robot.abscisse + mouvement.abscisse,
                 self.robot.ordonnee + mouvement.ordonnee))
            info_obstacle = self.carte.get_infos_obstacle(obstacle_suivant)
            print("Mouvement {0} : {1}".format(i, info_obstacle.message))
            if info_obstacle.blocage == "bloquant":
                # on stoppe en cas d'obstacle blocant
                print("Fin du mouvement")
                print(self.carte)
                return True
            elif info_obstacle.blocage == "non bloquant":
                nouvelle_position = Coordonnees(
                    self.robot.abscisse + mouvement.abscisse,
                    self.robot.ordonnee + mouvement.ordonnee)
                nouvel_obstacle = self.carte.get_obstacle(nouvelle_position)
                self.carte.deplacer_robot(self.obstacle, nouvelle_position)
                self.robot = nouvelle_position
                self.obstacle = nouvel_obstacle
                self.sauvegarder_partie()
            elif info_obstacle.blocage == "sortie":
                # on stoppe en cas d'obstacle de sortie
                # mais on met tout de même à jour le labyrinthe
                print("Fin du mouvement")
                nouvelle_position = Coordonnees(
                    self.robot.abscisse + mouvement.abscisse,
                    self.robot.ordonnee + mouvement.ordonnee)
                nouvel_obstacle = self.carte.get_obstacle(nouvelle_position)
                self.carte.deplacer_robot(self.obstacle, nouvelle_position)
                self.robot = nouvelle_position
                self.obstacle = nouvel_obstacle
                self.sauvegarder_partie()
                print(self.carte)
                return False
        print(self.carte)
        return True

    def sauvegarder_partie(self):
        """
            Enregistre la partie en cours
        """
        with open(donnees.fichier_sauvegardes, 'rb') as fichier:
            mon_depickler = pickle.Unpickler(fichier)
            try:
                # pour des raisons de conflits entre namedtuple et Pickle
                # passage par des tuples classiques pour la sauvegarde
                sauvegardes = mon_depickler.load()
                sauvegardes[self.carte.nom] = (
                    self.carte.nom,
                    (self.robot.abscisse, self.robot.ordonnee),
                    self.obstacle)
            except EOFError:
                sauvegardes = {}
                sauvegardes[self.carte.nom] = (
                    self.carte.nom,
                    (self.robot.abscisse, self.robot.ordonnee),
                    self.obstacle)
        with open(donnees.fichier_sauvegardes, 'wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(sauvegardes)

    def supprimer_partie(self):
        """
            Supprime une sauvegarde après avoir gagné le jeu
            On utilise le fichier données.py pour avoir le nom du fichier
        """
        with open(donnees.fichier_sauvegardes, 'rb') as fichier:
            mon_depickler = pickle.Unpickler(fichier)
            try:
                sauvegardes = mon_depickler.load()
                del sauvegardes[self.carte.nom]
            except EOFError:
                sauvegardes = {}
        with open(donnees.fichier_sauvegardes, 'wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(sauvegardes)

    @staticmethod
    def charger_partie(nom_carte):
        """
            charge les infos d'une partie commencée
            On utilise le fichier données.py pour avoir le nom du fichier
        """
        with open(donnees.fichier_sauvegardes, 'rb') as fichier:
            mon_depickler = pickle.Unpickler(fichier)
            try:
                sauvegarde = mon_depickler.load()[nom_carte]
                return sauvegarde
            except EOFError:
                print('erreur de fichier')
