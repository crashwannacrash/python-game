import pygame
from classes.projectile import Projectile

# Créer une classe qui représente le joueur
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("./assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        
    def launch_projectile(self):
        # Création d'une nouvelle instance de la class Projectile
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)
        
    def move_right(self):
        self.rect.x += self.velocity
        
    def move_left(self):
        self.rect.x -= self.velocity