# PCBS : expérimentation visant à voir l'influence de la taille et du nombre de points sur une tâche de comparaison rapide.
"""Module rond taile congruent qui a pour but d'afficher des ensembles de points dont le rayon est proportionnel au nombre de points"""

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
		right_size = random.randint(2,5) # Test pour faire un rapport nombre de points/taille congruent
		left_size = 2*right_size
	else :
		left_size = random.randint(2,5)
		right_size = 2*left_size
	return left_size
	return right_size

def distance_points(couple1,couple2):
	"""Fonction controllant la distance entre nos points pour notre ensemble de points aléatoires"""

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
		new_couple = liste_couple[compteur] #Prend en compte le couple de coordonées suivant
		range_dist = distance_points(couple, new_couple) > dist_max
		compteur += 1
	return range_dist

def display_dots_size_cong(file_name_stim_cong):
	""" Génère deux ensemble de points aléatoires dont la taille est proportionnelle au nombre de points"""
	pygame.init()

	screen = pygame.display.set_mode((1600,900)) # Définition de la résolution pour mon écran.

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

	pygame.image.save(screen, file_name_stim_cong) # sauvegarde l'image généré avec le nom choisi, pour la suite c'est le format png qui nous intéresse


	

