# PCBS Numerical Comparison Task vs. Non Numerical Dimensions

# <u>Plan</u>

* Introduction
* Preparation du stimulus avec PyGame
* Running The expyriment
* Conclusion


# <u>Introduction</u>

## <u>Points inférents</u> : 
   Parmi l'ensemble des prédispositions relatives à notre système naïf de connaissances (ou *core knowledge*) se trouve notre capacité à estimer pécisément et rapidement le nombre d'items présents dans un ensemble. Cette forme précoce de cognition numérique émergeant dès l'enfance est autrement nommée "numérosité" (Dehaene, 1997). Un des facteurs modulateurs de la numérosité est "l'effet de taille numérique", dont l'analyse répliquée montre que l'imprécision de notre estimation augmente au-delà de plus de 5 items contenus dans l'ensemble. Des psychologues comme Piaget ont aussi  mis en lumière l'influence de paramètres de dimensions non-numériques sur notre "sens des nombres". La taille, la densité ou l'espacement des objets peuvent  également nuancer la précision de l'estimation chez les enfants (Piaget, 1952). L'interrelation entre l'influence des dimensions non numériques, la numérosité, et la maturation des compétences mathématiques plus tard est toujours discutée. Toutefois, il est intéressant de noter que leur impact diffère individuellement et n'est pas homogène. Parmi les études s'étant intéressées aux variations interindividuelles vis-à_vis de l'influence de ces paramètres non-numériques chez les enfants, Viarouge et. al mettent en évidence dans une tâche de *matching* en choix forcé entre deux ensembles de points la préférence spontanée pour la taille, la densité, ou bien le nombre d'items présents dans un ensemble qui corrèle par la suite avec la performance des sujets dans une tâche de comparaison numérique (Viarouge et al., 2017). D'autres études de la numérosité chez une population de jeunes adultes autistes démontre une baisse de la précision lorsque l'ensemble d'objets (des points) à dénombrer sont présentés sous une forme évocative (i.e des formes d'animaux), que les auteurs expliquent par la propension qu'auraient les sujets autistes à vouloir déceler des patterns globaux (Meaux et al., 2014). 

## <u>Projet</u> : 
   Reprenant les tâches expérimentales de Viarouge et al., le projet vise à programmer
la tâche expérimentale suivante :
Il s'agit d'une tâche de comparaison numérique entre deux ensembles de points qui se déroule sur écran. 
Sur la droite et gauche de l'écran sont présentées deux cartes présentant un ensemble de points
La tâche du sujet est de choisir laquelle de ces deux cartes contient le plus de points présent sur la carte centrale en pressant *flèche gauche* pour choisir celle de gauche et *flèche droite* pour celle de droite.

<u>Deux magnitudes étudiées</u> : 
* la taille 
* la densité de points

<u>Deux conditions par magnitude</u> :  
* congruent : la taille des points est proportionnelle au nombre de points/la densité (concentration de points par unité d'aire) est proportionnelle au nombre de points

* incongruent : la taille des points est inversement proportionnelle au nombre de points/la densité (concentration de points par unité d'aire) est inversement proportionnelle au nombre de points

Pour que la réponse du sujet soit la plus spontanée, chaque essai dure 1200 ms, après quoi l'ensemble des trois cartes est renouvellé.
Une croix de fixation est affichée durant 500 ms avant chaque essai pour que le sujet reste attentif.

Ok, let's dive in it !

# 1.<u>Preparation du stimulus avec PyGame</u>

   J'ai choisi d'entreprendre ce projet de façon séquentielle, en créeant d'abord un module dédiée à la création de mes stimuli et à leur enregistrement. Chaque magnitude et stimuli fait l'objet d'un module qui lui est spécifiquement dédié. 
  
## <u>1. Générer deux ensembles de points, rapport nombre/taille congruent :</u>

### <u>Définir sur quelle carte la taille sera la plus importante :</u>

```
def most_size_side(compteur_gauche, compteur_droit): 
	"""Fonction qui détermine où seront situés les plus gros cercles, avec un rapport de 1/2"""

	global left_size
	global right_size 
	left_size = int()
	right_size = int()
	if compteur_gauche > compteur_droit :
		right_size = random.randint(2,5) # Test pour faire un rapport nombre de points/taille congruent
		left_size = 2*right_size
	else :
		left_size = random.randint(2,5)
		right_size = 2*left_size
	return left_size
	return right_size
```
La fonction ci-dessus assure ce rôle.  S'il y a plus de points à gauche, il seront plus gros à gauche et inversement. Elle regarde le nombre de points, elle définit une taille de rayon spécifique pour le côté où il y en a le moins puis multiplie par deux ce rayon du côté où il y en a le plus. Le ratio de taille entre les deux cartes est donc de 1/2.

### <u>Calculer la distance entre nos points :</u>

```
def distance_points(couple1,couple2):
	"""Fonction controllant la distance entre nos points pour notre ensemble de points aléatoires"""

	return math.sqrt((couple1[0]-couple2[0])**2+(couple1[1]-couple2[1])**2) #Th pythagore
```
Celle-ci permet de calculer la distance entre deux points. Elle emploie la formule pour calculer le carré de l'hypothénuse d'un triangle dont deux points seraient de part et d'autre de l'angle droit du triangle rectangle pour retrouver la distance entre ces points en se servant de leurs couples de coordonées. Cette fonction avec la suivante est celle qui m'a prise le plus de temps à implémenter. Elle me permettra de gérer la distance entre les points ensuite, elle était donc essentielle. 

### <u>Contrôler le stimuli : empêcher la superposition des points :</u>

```
def check_superposition(couple,liste_couple,radius):
	"""Vérifie si le point couple n'entre dans le rayon minimum d'aucun point de la liste_couple"""
	overlap = False
	compteur = 0
	while not overlap and compteur<len(liste_couple):
		new_couple = liste_couple[compteur] #Prend en compte le couple suivant
		overlap = distance_points(couple, new_couple) < radius
		compteur += 1
	return overlap
```
On définit un booléen et on appelle la fonction qui calcule la distance entre les points et on regarde si la distance est inférieure au rayon, auquel cas la superposition des points risque de poser problème pour discriminer deux points différents et overlap = True. La liste couple prend comme éléments l'ensemble des coordonées de nos points. On contrôle la distance à partir de l'ensemble des coordonées de points contenus dans notre liste.

### <u>Contrôler la distance entre les points :</u>

```
def check_range_dist(couple,liste_couple,dist_max):
	"""Vérifie si le point couple est dans le champ d'éloignement défini"""
	range_dist = False
	compteur = 0
	while not range_dist and compteur<len(liste_couple):
		new_couple = liste_couple[compteur] #Prend en compte le couple de coordonées suivant
		range_dist = distance_points(couple, new_couple) > dist_max
		compteur += 1
	return range_dist
```
Je me suis servi de la fonction précédèmment pour faire en sorte que la distance entre les points soit contrôlée et reste dans une aire prédéfinie.

### <u>Générer l'ensemble de points :</u>

```
def display_dots_size_cong(file_name_stim_cong):
	""" Génère deux ensemble de points aléatoires dont la taille est proportionnelle au nombre de points"""
	pygame.init()

	screen = pygame.display.set_mode((1600,900)) # Résolution pour mon écran
	red = (255,0,0)
	green = (0,255,0)
	blue = (0,0,255)
	darkBlue = (0,0,128)
	white = (255,255,255)
	black = (0,0,0)
	pink = (255,200,200)
	yellow = (255,255,0)
	grey = (210,210,210)
	darkGrey = (99,99,99)


	screen.fill(black)


	# Il y aura deux ensembles de points présentés simultanément. Ils seront présentés au sein de 2 rectangles artificiels. Cela me permet de mieux ajuster ll'espacement lors des simulations.
	pygame.draw.rect(screen, grey, (250,400,450,300), 0)
	pygame.draw.rect(screen, grey, (900,400,450,300), 0)


	# Dessiner deux ensembles de points aléatoires
	# Initialisation des variables
	compteur_gauche = random.randint(8, 18)
	compteur_droit = random.randint(8,18)
	nombre_cercles_gauches = int()
	nombre_cercles_droits = int()

	most_size_side(compteur_gauche, compteur_droit) # Rapport taille/nombres de points
	radius_gauche = left_size
	radius_droit = right_size

	coordonees_cercles_gauches = []
	coordonees_cercles_droits = []
	overlap = False
	range_dist = False


	# Premier ensemble de points aléatoires
	while nombre_cercles_gauches < compteur_gauche:
		position_cercle_x_gauche = random.randint(260, 690)
		position_cercle_y_gauche = random.randint(410, 690)
		while check_superposition((position_cercle_x_gauche,position_cercle_y_gauche), coordonees_cercles_gauches, radius_gauche) and check_range_dist((position_cercle_x_gauche,position_cercle_y_gauche), coordonees_cercles_gauches, 25): # Boucle qui empêche la superposition de points
			position_cercle_x_gauche = random.randint(260, 690)
			position_cercle_y_gauche = random.randint(410, 690)
		print((position_cercle_x_gauche,position_cercle_y_gauche)) # Vérification dans la console
		pygame.draw.circle(screen, darkGrey, (position_cercle_x_gauche,position_cercle_y_gauche), radius_gauche, 0)
		nombre_cercles_gauches += 1
		coordonees_cercles_gauches.append((position_cercle_x_gauche,position_cercle_y_gauche))
	print("le nombre de cercles de à gauche est de", nombre_cercles_gauches) # Contrôle pour suivre la création de nos stimuli

			

	# Deuxième ensemble de points aléatoires
	while nombre_cercles_droits < compteur_droit:
		position_cercle_x_droit = random.randint(910, 1340)
		position_cercle_y_droit = random.randint(410, 690)
		while check_superposition((position_cercle_x_droit,position_cercle_y_droit), coordonees_cercles_droits, radius_droit) and check_range_dist((position_cercle_x_droit,position_cercle_y_droit), coordonees_cercles_droits, 50): # Boucle qui empêche la superposition de points
			position_cercle_x_droit = random.randint(910,1340)
			position_cercle_y_droit = random.randint(410, 690)
		pygame.draw.circle(screen, darkGrey, (position_cercle_x_droit,position_cercle_y_droit), radius_droit, 0)
		nombre_cercles_droits += 1
		coordonees_cercles_droits.append((position_cercle_x_gauche,position_cercle_y_gauche))
	print("le nombre de cercles de à droite est de", nombre_cercles_droits) # Contrôle pour suivre la création de nos timuli

	pygame.image.save(screen, file_name_stim_cong)

```
La fonction est documentée. La taille de l'écran est ici adaptée à ma résolution d'écran. Les compteurs de cercles permettent d'attribuer un nombre de points à afficher à droite et à gauche, entre 8 et 18 suivant Viarouge, et al. Des coordonées de points sont attribuées au départ au sein de deux aires rectangulaires qui définissent l'aire de nos cartes. La distance entre les points est ensuite contrôlée par nos fonctions prédéfinies et modifiées pour remplir les conditions de distance : supérieur au rayon, inférieur à la distance délimitée. Ceci est reproduit séparément à droite et à gauche. Les coordonées de nos points sont attribuées aléatoirement à la condition qu'elles soient contenues dans la limite de l'aire de nos cartes.
Les ensembles générés sont ensuite sauvegardés sous le nom fichier dont le nom est défini en paramètre de la fonction.

Note : l'espacement entre les points est deux fois plus petit dans là où il y en a le plus, c'est une forme de compensation par rapport à l'espace occupé par les points.

## <u>2. Générer deux ensembles de points, rapport nombre/taille incongruent :</u>

Les mêmes fonctions seront appelées, on inversera simplement les conditions de notre fonction most_size_side() de sorte que les points soient plus petits lorsqu'il y en a plus :

```
def most_size_side(compteur_gauche, compteur_droit): 
	"""Fonction qui détermine où seront situés les plus gros cercles, avec un rapport de 1/2"""

	global left_size
	global right_size 
	left_size = int()
	right_size = int()
	if compteur_gauche > compteur_droit :
		right_size = random.randint(2,5) # Test pour faire un rapport nombre de points/taille congruent
		left_size = 2*right_size
	else :
		left_size = random.randint(2,5)
		right_size = 2*left_size
	return left_size
	return right_size
```

## <u>3. Générer deux ensembles de points, rapport espacement/taille congruent et incongruent :</u>

   Le projet de départ était de contrôler la densité des points. Je n'y suis cependant pas parvenu. Plusieurs solutions auxquelles j'ai pu réfléchir : (1) définir une grille au sein de mes cartes, afin de prédéfinir les positions occupables par mes points  et faire en sorte qu'ils se retrouvent tous dans une sous-aire de cette grille. (2) Partir d'une définition de la densité : rapport du nombre de positions occupées/le nombre de positions occuppables sur une grille d'emplacements prédéfinis. Malgré des essais, ces solutions me sont parues compliquées à implémenter, notamment à cause des manipulations sur listes qu'elles requierent, je me suis donc concentré sur l'espacement (*sparsity*) des points.
Pour la sparsity cong, j'ai essayé de réduire la distance maximale entre les points en diminuant la distance maximale de leur éloignements. 
Pour le rapport espacement/taille incongruent, j'ai fait l'inverse. Le but est que les points soient d'autant plus éloignés qu'il y a de points. 
Pour sparsity_cong, le but est de jouer sur l'intuition que les points seront d'autant plus ressérés entre eux qu'il y en a.
Le ratio choisi est de 1:2, dans des études sur la dimension de la densité, le rapport est de 1:3, mais ne la manipulant pas directement, je préfère choisir un ratio qui permettrait de rendre plus saillant visuellement l'espacement.

# <u>2. Running The expyriment</u>

### <u>1. Préparation des stimuli</u>

   La seconde partie du programme est la tâche expérimentale. J'ai d'abord importé l'ensemble de mes modules me permettant de générer et enregistrer mes stimuli. 

```
"""A series of trials where sets of dots are displayed, the goal is to guess on which side there are more.
"""

import pygame 
import rond_taille_congruent 
import rond_taille_noncongruent 
import rond_sparsity_congruent
import rond_sparsity_noncongruent
import random
# L'ensemble de ces modules nous servent à générer nos stimuli aléatoirement et les enregistrer sous format png
import numpy as np # Pas utile ici mais au cas où
import expyriment
from  expyriment.stimuli import FixCross, BlankScreen, Video, Picture
from expyriment import control
control.set_develop_mode(False) # Renvoie erreurs format python
```
Il faut ensuite enregistrer les ensembles générés sous format png. La fonction display_dots que j'ai créé pour chaque magnitude et module le permet. Ici, les fichiers images (png) sont enregistrés successivement jusqu'à ce qu'on génére 16 ensembles pour chaque condition, soit 48 en tout.  Le nom du fichier pris en paramètre par la fonction display_dots est formaté de sorte qu'à chaque image enregistrée, la suivante n'écrase pas la précédente, ils sont successivements numérotés de 1 à 16 suivant la valeur de n, c'est-à-dire l'ordre dans lequel ils sont créés, c'est pourquoi n va de 1 à 16 et ne débute pas à 0. Les stimuli sont stockées dans une liste et la randomisation se fait via random.shuffle qui permet de mélanger les éléments de cette liste. Par contrainte de concision, je ne mettrai que les exemples concernant la première magnitude (taille), la même chose est effectué en appellant les modules et fonctions controllant l'espacement.

```
# Phase de génération des stimuli. Inconvénient : Prend un certain temps
# On génère les stimulus utilisés pour le block 1 : ici on regarde la taille en fonction du nombre de points
list_stim_block_1 = []

if __name__ == "__main__":
	n = 1
	while n<=16:
		rond_taille_congruent.display_dots_size_cong("stimulus_rond_size_up%d.png"%(n))
		list_stim_block_1.append("stimulus_rond_size_up%d.png"%(n))
		rond_taille_noncongruent.display_dots_size_incong("stimulus_rond_size_down%d.png"%(n))
		list_stim_block_1.append("stimulus_rond_size_down%d.png"%(n))
		n += 1 
# Initialisation : génération des fichiers d'ensembles de points aléatoires jusqu'à 16 pour chaque condition, 48 en tout, on les stocke dans une liste 
print(list_stim_block_1) # Vérifie si la liste contient bien mes images png

random.shuffle(list_stim_block_1)
```
### <u>2. Simulation de tâche expérimentale</u>
   
#### <u>Début de la présentation des stimuli</u>

```
expyriment.control.start()

message_beginning = expyriment.stimuli.TextLine(text="Your goal is to guess on which side of the screen there are more dots, if it's left, press left, if it's right, press right, type either of the arrow keys to begin")
message_beginning.present()
key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,expyriment.misc.constants.K_RIGHT])
```
Les consignes sont affichées pour informer le sujet. La dernière ligne permet le *binding* des touches *flèches gauche et droite*

```
for stim_block_1 in list_stim_block_1:
	# On crée l'interstimulus, écran noir. Je l'insère ici exceptionnellement pour éviter les problèmes de compression que rencontre le module
	inter_stimulus = expyriment.stimuli.BlankScreen()
	fixcross = expyriment.stimuli.FixCross()
	fixcross.preload()
	fixcross.present()
	exp.clock.wait(500)
	stim = expyriment.stimuli.Picture(stim_block_1)
	stim.present()
	exp.clock.wait(1200)
	inter_stimulus.present()
	key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,expyriment.misc.constants.K_RIGHT])
```

Le script est exécuté linéairement. Les stimuli contenus dans notre liste de stimuli sont successivement affichés durant 1200 ms, une croix de fixation les précède durant 500 ms. J'ai dû créer un écran noir, l'inter_stimulus, à afficher après les 1200 ms de présentation car le stimulus reste autrement affiché jusqu'à ce que le sujet réponde. Malheureusement, j'ai essayé de le créer en dehors de a boucle, au début de mon code, mais cela engendrait une erreur de compression que je ne comprenais pas.
La même chose est répétée avec les stimuli relatifs à la seconde magnitude non numérique, puis la tâche expérimentale prend fin.

# <u>Limitations</u>

   Par rapport à mes objectifs, je n'ai pu réussir à contrôler avec exactitude la densité des points. L'espacement ne se substitue pas bien à cette variable que je souhaitais contrôler. Par manque de temps, je n'ai pas réalisé de partie dédiée à l'analyse des réponses données par le sujet, et de sa performance.
   
   J'ai également eu des difficultés dans l'élaboration des stimuli et leur enreistrement. Empêcher la supersposition et contrôler la distance entre chaque point une fois qu'il est nouvellement créé par rapport aux précédents m'a pris beaucoup de temps d'implémentation. D'autres solutions étaient envisageables, mais elles faisaient recours à des scripts qui auraient été trop longs et compliqués à rédiger à mon niveau. J'ai également eu de la difficulté à trouver comment générer des stimuli qui s'enregistrent successivement sans s'écraser les uns à la suite des autres.
   
   Des limitations pratiques et théoriques sont présentes. Des  limites théoriques car la tâche a été développée en se calquant sur le paradigme de Viarouge et al., mais en parcourant la littrature relative aux tâches de comparaison numérique, je me suis rendu compte qu'il y a des variations dans les ratios, les temps de présentations et les méthodes d'enregistrement de réponses employées. Il y a également des limitations pratiques, car le temps de création des stimuli est long et les ensembles de points générés sont partiellement visibles durant ce temps. La tâche expérimentale créée est ainsi une ébauche pouvant servir de tâche pilote.
 
# <u>Conclusion</u>

   Les objectifs de départ ont été partiellement atteints, la réflexion sur la création d'ensemble de points générés aléatoirement variant en taille a cependant été un bon exercice d'apprentissage. La réfexion théorique sur la densité était également intéressante, malgré que je n'ai pu totalement l'atteindre, cela m'a permis de réfléchir à comment à manipuler l'ensemble des outils de python que je connais pour le moment afin de les utiliser de façon optimale. J'ai ainsi pu contrôler la superposition totale des points en me sevant de boucles *while* que je connaissais, tandis que d'autres alternatives que j'ai pu voir sur des forums employaient des classes spécifiques.
  
  Mon niveau en python est débutant, j'ai connu le langage et ses bases lors de la prérentrée au CogMaster. Avec ce projet, j'ai ainsi pu implémenter dans mon projet, sans utiliser de méthodes complexes. Le formatage et la création d'objets générés et enregistrés dynamiquement fait aussi partie de ce que j'ai pu apprendre. J'ai pu me familiariser avec le module PyGame et Expyriment, même si la création des stimuli est ce qui m'a pris le plus de temps.
  
  Les exercices donnés pour le cours PCBS permettent de progresser. Peut-être faudrait-il faire une classe inversée et demander plus en amont de choisir un projet afin d'axer le cours sur les demandes. Cependant ceci est à la fois dur car on ne sait ce qu'on est réellement capable de coder lorsqu'on débute.
   
# <u>Bibliographie</u> 

Dehaene S., 1997. The Number Sense: How the Mind Creates Mathematics. New-York: Oxford University Press.

Meaux E., et al., 2014. Neural Substrates of Numerosity Estimation in Autism. Human Brain Mapping (Issue 35) : pp 4362-4385

Piaget J., 1952. The child's conception of number. London: Routledge& Kegan Paul, Ltd.

Sacks O., 1985. The Man who Mistook his Wife for a hat and other Clinical Tales. London, UK: Ducksworth.

Smith SB., 1983. The Great Mental Calculators: The Psychology Methods, and Lives of Calculating Prodigies, Past and Present. Columbia Univ. Press, New York.

Viarouge A., et al., 2017. Spontaneous orientation towards irrelevant dimnsions of magnitude and numerical acuity. Learning and Instruction.
Vol 54. pp 156-163


