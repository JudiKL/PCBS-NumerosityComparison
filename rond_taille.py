# PCBS : expérimentation visant à voir l'influence de la taille et du nombre de points sur une tâche de comparaison rapide.

import pygame 
import sys
# Pour commencer avec pygame
import random
# Pour avoir des tailles aléatoires

pygame.init()

screen = pygame.display.set_mode((800,600)) # Définition de l'écran. La minimale selon les standards actuels est prise par défaut.

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
yellow = (255,255,0)


screen.fill(black)


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

pygame.display.update() # Actualiser les figures sur l'écran.

# sauvegarder au format png le stimulus
pygame.image.save(screen, "stimulus_rond.png")

# Attendre que la fenêtre soit refermée. Inutile ici mais cela permet de tester le stimulus rapidement.
done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True




