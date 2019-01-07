## PCBS Non Numerical Dimensions and Numerosity Comparison Task

## 1.Preparation of the stimulus with PyGame
Some trials : 
# PCBS : expérimentation visant à voir l'influence de la taille et du nombre de points sur une tâche de comparaison rapide.

# Il y aura deux ensembles de points présentés simultanément. Ils seront présentés au sein de 2 rectangles artificiels. Cela me permet de mieux ajuster ll'espacement lors des simulations.
pygame.draw.rect(screen, black, (0,0,300,600), 0)
pygame.draw.rect(screen, black, (500,0,300,600), 0)

# Dessiner deux ensembles de points aléatoires
# Premier ensemble de points aléatoires
compteur_gauche = random.randint(1, 10)
nombre_cercles_gauches = 0
radius_gauche = 2*compteur_gauche # Test pour faire un rapport taille-nombre de points congruent
while nombre_cercles_gauches < compteur_gauche:
	position_cercle_x_gauche = random.randint(5, 300)
	position_cercle_y_gauche = random.randint(5, 555)
	pygame.draw.circle(screen, yellow, (position_cercle_x_gauche,position_cercle_y_gauche), radius_gauche, 0)
	nombre_cercles_gauches += 1
# Deuxième ensemble de points aléatoires
compteur_droit = random.randint(1,10)
nombre_cercles_droits = 0
radius_droit = 2*compteur_droit
while nombre_cercles_droits < compteur_droit:
	position_cercle_x_droit = random.randint(600, 755)
	position_cercle_y_droit = random.randint(5, 555)
	pygame.draw.circle(screen, yellow, (position_cercle_x_droit,position_cercle_y_droit), radius_droit, 0)
	nombre_cercles_droits += 1





## 2. Running The expyriment


