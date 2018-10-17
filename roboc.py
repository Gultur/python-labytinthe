# -*-coding:Utf-8 -*

"""
    fichier d'execution du jeu

"""
import os
import functions
from labyrinthe import Labyrinthe


def main():
    """
        methode d'execution du jeu
    """

    # on affiche la liste des cartes disponibles
    liste_des_cartes = functions.liste_cartes() + functions.liste_sauvegardes()
    functions.afficher_liste(liste_des_cartes)

    # selection d'une carte, un retour "None" indique une mauvaise saisie
    while True:
        choix = functions.choix_carte(
            input('''Indiquez le numéro de la carte choisie.
    Attention, si vous choisissez une nouvelle partie, la sauvegarde associée
    à la carte concernée sera remplacée. \n'''), liste_des_cartes)
        if choix is not None:
            break

    # la carte est choisie, on peut générer un Labyrinthe
    laby = Labyrinthe(choix)
    # on affiche le tracé du labyrinthe
    print(laby.carte)

    # on lance la boucle du jeu
    while True:
        deplacements = input("""Dans quelle direction voulez vous aller?
    "E" pour aller vers l'est, "N" pour aller vers le nord
    "S" pour aller vers le sud, "O" pour aller vers l'ouest
    Suivi d'un nombre (optionnel) pour le nombre de cases à parcourir
    "Q" pour sauvegarder et quitter
    """)
        # on vérifie que les données entrées par l'utilisateur sont valides
        instructions = functions.instructions_valide(deplacements)
        if instructions is not None:

            if instructions == "quitter":
                laby.sauvegarder_partie()
                break
            if instructions == "lettre non valide":
                print("La lettre entrée n'est pas valide \n")
                continue
            if instructions == "non valide":
                print("Les données entrées ne sont pas valides \n")
                continue
            else:
                # on vérifie si la partie est toujours active
                partie_en_cours = laby.effectuer_deplacements(instructions)
                if not partie_en_cours:
                    # en cas de sortie trouvée, on supprime la sauvegarde
                    laby.supprimer_partie()
                    print("Partie terminée, sauvegarde supprimée")
                    break

    # On met en pause le système (Windows)
    os.system("pause")


if __name__ == "__main__":
    main()
