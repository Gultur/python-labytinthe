"""
    Ce module contient des fonctions necessaires au lancement du jeu.
"""
# on pourrait à l'avenir passer par une classe Jeu contenant ces méthodes

import os
import pickle
from collections import namedtuple
import donnees


def liste_cartes():
    """
        retourne la liste des cartes de bases disponibles
        on passe par un namedtuple carte_type(nom, type)
        on utilise le fichier données.py pour acceder au bon repertoire
    """
    Carte_type = namedtuple("Carte_type", ['nom', 'type'])
    return [Carte_type(carte[:-4], "Nouvelle partie") for position, carte in
            enumerate(os.listdir(donnees.repertoire_des_cartes))]


def liste_sauvegardes():
    """
        recupère le nom des cartes dans le fichier de sauvegarde
        retourne les sauvegardes sous forme de liste
        on utilise le fichier données.py pour acceder au bon repertoire
    """
    Carte_type = namedtuple("Carte_type", ['nom', 'type'])
    with open('sauvegardes.lsav', 'rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        try:
            sauvegardes = []
            for nom in mon_depickler.load():
                sauvegardes.append(Carte_type(nom, "Partie sauvegardée"))
            return sauvegardes
        except EOFError:
            return []


def afficher_liste(liste_des_cartes):
    """
        affiche la liste des cartes fournies en paramètre
    """
    for(index, carte_type) in enumerate(liste_des_cartes):
        print("{0} - {1} - {2}".format(
            index + 1, carte_type.nom, carte_type.type))


def choix_carte(numero_carte, liste_des_cartes):
    """
        Retourne la carte choisie par l'utilisateur
        parametre : nom de la carte choisie
                    liste de namedtuple (nom, type)
        retourne : fichier à exploiter
    """
    # il faut juste verifier qu'un nombre valide est entré
    try:
        numero = int(numero_carte)
        if (numero - 1) >= 0 and (numero - 1) < len(liste_des_cartes):
            return liste_des_cartes[numero - 1]
        print("Veuillez entrer un nombre entre 1 et {0}".format(
            len(liste_des_cartes)))
        return None
    except ValueError:
        print("Vous n'avez pas entré un entier")
        return None


def instructions_valide(deplacement):
    """
        teste la validité du choix entré par l'utilisateur
        parametre : string du choix
        retourne : string
    """
    try:
        Deplacements = namedtuple("Deplacements", ["direction", "cases"])
        # le premièr caractère doit être une lettre
        if len(deplacement) >= 1 and deplacement[0].isalpha():
            lettre = deplacement[0].upper()
            # il y a 5 lettres possibles
            if lettre not in ["Q", "E", "O", "N", "S"]:
                return "lettre non valide"
            if lettre == 'Q':
                print('Fermeture du jeu, à bientôt')
                return "quitter"
            if len(deplacement) == 1:
                return Deplacements(deplacement[0], 1)
            else:
                # il faut aussi vérifier la validité du nombre entré
                # on ne met pas de nombre maximum, le mouvement sera arrété
                # dès un obstacle rencontré
                if int(deplacement[1:]) and deplacement[1] not in ['+', '-']:
                    return Deplacements(deplacement[0], int(deplacement[1:]))
        return "non valide"
    except (TypeError, ValueError):
        return "non valide"
