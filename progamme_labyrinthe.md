
#Lancement du programme
## on affiche la liste des cartes disponibles:
		- chargement des cartes du repertoires (voir liste_cartes() / functions)
		- chargement des cartes en sauvegarde (voir liste_sauvegarde() / functions)
##l'utilisateur fait un choix de la carte:
	=> si nouvelle partie
		- labyrinthe = on charge le fichier cartes et on le met dans une liste
		- position = position robot initiale
		- obstacle actuel = " "
		- dictionnaire d'obstacles = obstacles présents dans la cartes (issus d'un fichiers données)
	=> si ancienne partie
		- position = position enregistrée
		- obstacle actuel = obstacle enregistré ( ou get_obstacle en utilisant le fichier carte)
		- labyrinthe = on transforme la carte serialisée en liste
##l'utilisateur fait un choix de deplacement:
	=> verification de la validité de l'entrée
	=> on quitte si demandé (et on enregistre)
	=> on fait une boucle avec le nombre de deplacement (recursif)
		- on teste si l'on ne sort pas de la carte
		- on teste si l'obstacle rencontré n'est pas bloquant
			=> on regarde dans un dictionnaire d'obstacle le message à afficher (ex {"." : " vous êtes devant une porte})
			=> s'il est bloquant on bloque le déplacement et on retourne la position actuelle
			=> s'il s'agit de la sortie on félicité et on quitte, et on supprime la sauvegarde

		

représentation de la carte sous forme de dictionnaire
un tuple de coordonnées comme clé (voir nametupled?)
carte_labyrinthe = {(coordonnee_x, coordonnee_y : "obstacle"), ...}
on le serialise pour la sauvegarde


test deplacement: on regarde l'obstacle contenu à la nouvelle position
deplacement : modification de la valeur correpondant à la nouvelle position et sauvegarde de l'obstacle initial


choix de la carte
creation du labyrinthe (choix)
choix.nom = nom carte
choix.type = sauvegarde ou non
=> self.carte = new Carte (nom_carte)
if choix.type == nouvelle partie
self.robot = self.carte.position_initiale
self.obstacle = " "
else
recherche de la sauvegarde
self.robot = position dans la sauvegarde
self.obstacle = obstacle enregistré dans la sauvegarde


instructions 
	instruction non valide, continue
	instruction valide:
		quitter, break
		for each deplacement:
			if deplacement valide:
				message()
				deplacer()
			if non valide:
				message
				break
		if mabythinthe termine: message, break



pickle_data = pickle.dump(laby, open('save.test', 'wb'))
print(pickle.load(open('save.test', 'rb')))


