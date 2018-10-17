"""
    ce module contient des données globables du jeu de labyrinthe
    permet de faire des modifications en un seul endroit
    - fichier de sauvegarde
    - repertoire des cartes
    - details des obstacles
"""
from collections import namedtuple

# nom du repertoire des cartes
repertoire_des_cartes = "cartes"

# details des obstacles
Obstacle = namedtuple("obstacle", ["nom", "blocage", "message"])
obstacles = {
    "O": Obstacle("mur", "bloquant", "Devant vous se dresse un mur, impossible d'aller plus loin"),
    ".": Obstacle("porte", "non bloquant", "Vous ouvrez une porte et la franchissez"),
    "U": Obstacle("sortie", "sortie", "Vous venez de trouver la sortie"),
    "X": Obstacle("robot", "non bloquant", "Cette personne, c\'est vous"),
    " ": Obstacle("chemin", "non bloquant", "Vous poursuivez sur le chemin")
}

# nom du fichier de sauvegarde
fichier_sauvegardes = "sauvegardes.lsav"
