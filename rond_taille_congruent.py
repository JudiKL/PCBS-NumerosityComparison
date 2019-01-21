# PCBS : expérimentation visant à voir l'influence de la taille et du nombre de points sur une tâche de comparaison rapide.

import pygame 
import sys
# Pour commencer avec pygame
import random
# Pour avoir des tailles aléatoires
import math

def distance_points(couple1,couple2):
	"""Fonction controllant la superposition des points pour notre ensemble de points aléatoires"""

	return math.sqrt((couple1[0]-couple2[0])**2+(couple1[1]-couple2[1])**2) #Th pythagore


def check_superposition(couple,liste_couple,radius):
	"""Vérifie si le point couple n'entre dans le rayon minimum d'aucun point de la liste_couple"""
	overlap = False
	compteur = 0
	while not overlap and compteur<len(liste_couple):
		new_couple = liste_couple[compteur] #Prend en compte le couple suivant
		overlap = distance_points(couple, new_couple) < radius
		compteur += 1
	return overlap



pygame.init()

screen = pygame.display.set_mode((1600,900)) # Définition de l'écran. La minimale selon les standards actuels est prise par défaut.

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
# Premier ensemble de points aléatoires
compteur_gauche = random.randint(8, 18)
nombre_cercles_gauches = int()
radius_gauche = random.randint(2,5) # Test pour faire un rapport taille-nombre de points congruent
coordonees_cercles_gauches = []
overlap = False




while nombre_cercles_gauches < compteur_gauche:
	position_cercle_x_gauche = random.randint(255, 655)
	position_cercle_y_gauche = random.randint(405, 655)
	while check_superposition((position_cercle_x_gauche,position_cercle_y_gauche), coordonees_cercles_gauches, 30): # Boucle qui permet de
		position_cercle_x_gauche = random.randint(255, 655)
		position_cercle_y_gauche = random.randint(405, 655)
	print((position_cercle_x_gauche,position_cercle_y_gauche))
	pygame.draw.circle(screen, darkGrey, (position_cercle_x_gauche,position_cercle_y_gauche), radius_gauche, 0)
	nombre_cercles_gauches += 1
	coordonees_cercles_gauches.append((position_cercle_x_gauche,position_cercle_y_gauche))

		


print(coordonees_cercles_gauches)

# Deuxième ensemble de points aléatoires
compteur_droit = random.randint(8,18)
nombre_cercles_droits = 0
radius_droit = 2*radius_gauche
coordonees_cercles_droits = []
while nombre_cercles_droits < compteur_droit:
	position_cercle_x_droit = random.randint(905, 1345)
	position_cercle_y_droit = random.randint(405, 655)
	pygame.draw.circle(screen, darkGrey, (position_cercle_x_droit,position_cercle_y_droit), radius_droit, 0)
	nombre_cercles_droits += 1
	coordonees_cercles_droits.append((position_cercle_x_gauche,position_cercle_y_gauche))


pygame.display.update() # Actualiser les figures sur l'écran.

# sauvegarder au format png le stimulus
pygame.image.save(screen, "stimulus_rond.png")

# Attendre que la fenêtre soit refermée. Inutile ici mais cela permet de tester le stimulus rapidement.
done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True




