# PCBS Numerical Comparison Task vs. Non Numerical Dimensions

# <u>Introduction</u>

## <u>Points inférents</u> : 
Parmi l'ensemble des prédispositions relatives à notre système naïf de connaissances (ou *core knowledge*) se trouve notre capacité à estimer pécisément et rapidement le nombre d'items présents dans un ensemble. Cette forme précoce de cognition numérique émergeant dès l'enfance est autrement nommée "numérosité" (Dehaene, 1997). Un des facteurs modulateurs de la numérosité est "l'effet de taille numérique", dont l'analyse répliquée montre que l'imprécision de notre estimation augmente au-delà de plus de 5 items contenus dans l'ensemble. Des psychologues comme Piaget ont aussi  mis en lumière l'influence de paramètres de dimensions non-numériques sur notree "sens des nombres". La taille, la densité ou l'espacement des objets peuvent  également nuancer la précision de l'estimation chez les enfants (Piaget, 1952). L'interrelation entre l'influence des dimensions non numériques, la numérosité, et la maturation des compétences mathématiques plus tard est toujours discutée. Toutefois, il est intéressant de noter que leur impact diffère individuellement et n'est pas homogène. Parmi les études s'étant intéressées aux variations interindividuelles vis-à_vis de l'influence de ces paramètres non-numériques chez les enfants, Viarouge et. al mettent en évidence dans une tâche de *matching* en choix forcé entre deux ensembles de points la préférence spontanée pour la taille, la densité, ou bien le nombre d'items présents dans un ensemble qui corrèle par la suite avec la performance des sujets dans une tâche de comparaison numérique (Viarouge et al., 2017). D'autres études de la numérosité chez une population de jeunes adultes autistes démontre une baisse de la précision lorsque l'ensemble d'objets (des points) à dénombrer sont présentés sous une forme évocative (i.e des formes d'animaux), que les auteurs expliquent par la propension qu'auraient les sujets autistes à vouloir déceler des patterns globaux (Meaux et al., 2014). 

## <u>Projet</u> : 
Reprenant les tâches expérimentales de Viarouge et al. (voir bibliographie), le projet vise à programmer
la tâche expérimentale suivante :
Il s'agit d'une tâche de comparaison numérique entre deux ensemble de points qui se déroule sur écran. 
Sur la droite et gauche de l'écran sont présentées deux cartes présentant un ensemble de points
La tâche du sujet est simplement de choisir laquelle de ces deux cartes contient le plus de points présent sur la carte centrale en pressant *flèche gauche* pour choisir celle de gauche et *flèche droite* pour celle de droite.
<u>Deux magnitudes étudiées</u> : 
* la taille 
* la densité de points
<u>Deux conditions par magnitude</u> :  
* congruent : la taille des points est proportionnelle au nombre de points/la densité (concentration de points par unité d'aire) est proportionnelle au nombre de points
* incongruent : la taille des points est inversement proportionnelle au nombre de points/la densité (concentration de points par unité d'aire) est inversement proportionnelle au nombre de points
Pour que la réponse du sujet soit la plus spontanée, chaque essai dure 1200 ms, après quoi l'ensemble des trois cartes est renouvellé.
Une croix de fixation est affichée durant 500 ms avant chaque essai pour que le sujet reste attentif.

Ok, let's dive in it !

## 1.Preparation of the stimulus with PyGame
Some trials : 
PCBS : expérimentation visant à voir l'influence de la taille et du nombre de points sur une tâche de comparaison rapide.

Il y aura deux ensembles de points présentés simultanément. Ils seront présentés au sein de 2 rectangles artificiels. Cela me permet de mieux ajuster l'espacement lors des simulations.
'''pygame.draw.rect(screen, black, (0,0,300,600), 0)
pygame.draw.rect(screen, black, (500,0,300,600), 0)'''

Dessiner deux ensembles de points aléatoires
'''Premier ensemble de points aléatoires
compteur_gauche = random.randint(1, 10)
nombre_cercles_gauches = 0
radius_gauche = 2*compteur_gauche # Test pour faire un rapport taille-nombre de points congruent
while nombre_cercles_gauches < compteur_gauche:
	position_cercle_x_gauche = random.randint(5, 300)
	position_cercle_y_gauche = random.randint(5, 555)
	pygame.draw.circle(screen, yellow, (position_cercle_x_gauche,position_cercle_y_gauche), radius_gauche, 0)
	nombre_cercles_gauches += 1'''
Deuxième ensemble de points aléatoires
'''compteur_droit = random.randint(1,10)
nombre_cercles_droits = 0
radius_droit = 2*compteur_droit
while nombre_cercles_droits < compteur_droit:
	position_cercle_x_droit = random.randint(600, 755)
	position_cercle_y_droit = random.randint(5, 555)
	pygame.draw.circle(screen, yellow, (position_cercle_x_droit,position_cercle_y_droit), radius_droit, 0)
	nombre_cercles_droits += 1'''





## 2. Running The expyriment

# Title 1
## Title 2

**Gras**
*italique*
***gras italique***
<u>souligne</u>

* liste 
* liste

1. Ex 1
2. Ex 2
	*
	
> citation

`citer code`

```
bloc de code
```
