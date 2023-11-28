import pygame

# Définition de la classe qui va gérer le projectile du joueur
class Projectile(pygame.sprite.Sprite):
    # Définition du constructeur de la class
    def __init__(self, player):
        super().__init__()
        self.velocity = 2
        self.player = player
        self.image = pygame.image.load('./assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0
        
    def rotate(self):
        # Tourner le projectile quand il est en déplacement
        self.angle += 3
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        
    def remove(self):
        self.player.all_projectiles.remove(self)
        
    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        
        # Condition pour vérifier si le projectile n'est plus présent sur l'écran
        if self.rect.x > 1080:
            # Supprimer le projectile
            self.remove()