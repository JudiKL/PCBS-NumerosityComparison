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

random.shuffle(list_stim_block_1) # On mélange les stimulus de la liste pour les présenter dans un ordre aléatoire et mélanger les conditions (voir module).




# On génère les stimulus utilisés pour le block 2. Ici, on s'intéresse à l'éloignement en fonction du nombre de points.
list_stim_block_2 = []

if __name__ == "__main__":
	n = 1
	while n<=16:
		rond_sparsity_congruent.display_dots_sparsity_cong("stimulus_rond_spars_cong%d.png"%(n))
		list_stim_block_2.append("stimulus_rond_spars_cong%d.png"%(n))
		rond_sparsity_noncongruent.display_dots_sparsity_incong("stimulus_rond_spars_noncong%d.png"%(n))
		list_stim_block_2.append("stimulus_rond_spars_noncong%d.png"%(n))
		n += 1

random.shuffle(list_stim_block_2) # On mélange les stimulus de la liste pour les présenter dans un ordre aléatoire.




# Initialisation du module expyriment pour y faire appel maintenant que nos stimuli sont prêts
exp = expyriment.design.Experiment(name="Numerical comparison vs. non numerical dimensions")
#expyriment.control.set_develop_mode()
expyriment.control.initialize(exp)


# Début de la présentation des stimuli
expyriment.control.start()

message_beginning = expyriment.stimuli.TextLine(text="Your goal is to guess on which side of the screen there are more dots, if it's left, press left, if it's right, press right, type either of the arrow keys to begin")
message_beginning.present()
key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,expyriment.misc.constants.K_RIGHT])

# Designing the first block
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


# Pause
message_two = expyriment.stimuli.TextLine(text="Rest time. Press one arrow key when ready to go")
message_two.present()
key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,expyriment.misc.constants.K_RIGHT])


# Designing the second block
for stim_block_2 in list_stim_block_2:
	key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,expyriment.misc.constants.K_RIGHT])
	fixcross = expyriment.stimuli.FixCross()
	fixcross.preload()
	fixcross.present()
	exp.clock.wait(500)
	stim = expyriment.stimuli.Picture(stim_block_2)
	stim.present()
	exp.clock.wait(1200)
	inter_stimulus.present()
	key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,expyriment.misc.constants.K_RIGHT])

expyriment.control.end()