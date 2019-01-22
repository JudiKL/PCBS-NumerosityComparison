# PCBS : expérimentation visant à voir l'influence de la taille et du nombre de points sur une tâche de comparaison rapide.
"""Module espacement congruent qui a pour but d'afficher des ensembles de points dont l'espacement est proportionnel au nombre de points"""

import pygame 
import sys
# Pour commencer avec pygame
import random
# Pour avoir des tailles aléatoires
import math

def most_size_side(compteur_gauche, compteur_droit):
	"""Fonction qui détermine où seront situés les plus gros cercles, avec un rapport de 1/2"""

	global left_size
	global right_size
	left_size = int()
	right_size = int()
	if compteur_gauche > compteur_droit :
		right_size = random.randint(2,5) # Test pour faire un rapport taille-nombre de points congruent
		left_size = 2*right_size
	else :
		left_size = random.randint(2,5)
		right_size = 2*left_size
	return left_size
	return right_size

def most_sparisty_side(compteur_gauche,compteur_droit):
	"""Fonction qui détermine où les points seront théoriquement les plus éloignés entre eux"""

	global left_sparsity
	global right_sparsity
	left_size = int()
	right_size = int()
	if compteur_gauche > compteur_droit :
		left_sparsity = random.randint(8,16)
		right_sparsity = 2* left_sparsity
	else :
		right_sparsity = random.randint(8,16)
		left_sparsity = 2*right_sparsity
	return left_sparsity
	return right_sparsity

def distance_points(couple1,couple2):
	"""Fonction controllant la superposition des points pour notre ensemble de points aléatoires"""

	return math.sqrt((couple1[0]-couple2[0])**2+(couple1[1]-couple2[1])**2) #Th pythagore : formule donnant la distance entre deux points adjacents


def check_superposition(couple,liste_couple,radius):
	"""Vérifie si le point couple n'entre dans le rayon minimum d'aucun point de la liste_couple"""
	overlap = False
	compteur = 0
	while not overlap and compteur<len(liste_couple):
		new_couple = liste_couple[compteur] #Prend en compte le couple suivant
		overlap = distance_points(couple, new_couple) < radius
		compteur += 1
	return overlap


def check_range_dist(couple,liste_couple,dist_max):
	"""Vérifie si le point couple est dans le champ d'éloignement défini"""
	range_dist = False
	compteur = 0
	while not range_dist and compteur<len(liste_couple):
		new_couple = liste_couple[compteur] #Prend en compte le couple suivant
		range_dist = distance_points(couple, new_couple) > dist_max
		compteur += 1
	return overlap

def display_dot_sparsity_cong():
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
	# Initialisation des variables
	compteur_gauche = random.randint(8, 18)
	compteur_droit = random.randint(8,18)
	nombre_cercles_gauches = int()
	nombre_cercles_droits = int()


	radius_gauche = 8
	radius_droit = 8

	most_sparisty_side(compteur_gauche,compteur_droit)
	range_dist_max_left = left_sparsity
	range_dist_max_right = right_sparsity

	coordonees_cercles_gauches = []
	coordonees_cercles_droits = []
	overlap = False
	range_dist = False


	# Premier ensemble de points aléatoires
	while nombre_cercles_gauches < compteur_gauche:
		position_cercle_x_gauche = random.randint(260, 690)
		position_cercle_y_gauche = random.randint(410, 690)
		while check_superposition((position_cercle_x_gauche,position_cercle_y_gauche), coordonees_cercles_gauches, radius_gauche): # Boucle qui empêche la superposition de points
			position_cercle_x_gauche = random.randint(260, 690)
			position_cercle_y_gauche = random.randint(410, 690)
			while check_range_dist((position_cercle_x_gauche,position_cercle_y_gauche), coordonees_cercles_gauches, range_dist_max_left): 
				position_cercle_x_gauche = random.randint(260, 690)
				position_cercle_y_gauche = random.randint(410, 690)
		print((position_cercle_x_gauche,position_cercle_y_gauche)) # Vérification dans la console
		pygame.draw.circle(screen, darkGrey, (position_cercle_x_gauche,position_cercle_y_gauche), radius_gauche, 0)
		nombre_cercles_gauches += 1
		coordonees_cercles_gauches.append((position_cercle_x_gauche,position_cercle_y_gauche))
	print("le nombre de cercles de à gauche est de", nombre_cercles_gauches) # Contrôle

			

	# Deuxième ensemble de points aléatoires
	while nombre_cercles_droits < compteur_droit:
		position_cercle_x_droit = random.randint(910, 1340)
		position_cercle_y_droit = random.randint(410, 690)
		while check_superposition((position_cercle_x_droit,position_cercle_y_droit), coordonees_cercles_droits, radius_droit): # Boucle qui empêche la superposition de points
			position_cercle_x_droit = random.randint(910,1340)
			position_cercle_y_droit = random.randint(410, 690)
			while check_range_dist((position_cercle_x_droit,position_cercle_y_droit), coordonees_cercles_droits, range_dist_max_right): 
				position_cercle_x_droit = random.randint(910, 1340)
				position_cercle_y_droit = random.randint(410, 690)
		pygame.draw.circle(screen, darkGrey, (position_cercle_x_droit,position_cercle_y_droit), radius_droit, 0)
		nombre_cercles_droits += 1
		coordonees_cercles_droits.append((position_cercle_x_gauche,position_cercle_y_gauche))
	print("le nombre de cercles de à droite est de", nombre_cercles_droits)


	# sauvegarder au format png le stimulus
	pygame.image.save(screen, "stimulus_rond_sparsity_up.png")