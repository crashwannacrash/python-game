import pygame
from classes.player import Player

# Créer une classe qui represente le jeu
class Game:
    
    def __init__(self):
        # Génerer le joueur
        self.player = Player()
        self.pressed = {}