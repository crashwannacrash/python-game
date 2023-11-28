import pygame
from classes.game import Game
pygame.init()

# Génerer la fenetre du jeu
pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080, 720))

# Importer l'arrière plan du jeu
background = pygame.image.load("./assets/bg.jpg")

# Chargement du jeu
game = Game()

running = True

# Boucle tant que cette condition est vraie
while running:
    
    # Appliquer l'arrière plan du jeu
    screen.blit(background, (0, -200))
    
    # Appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)
    
    # Récupérer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()
    
    # Appliquer l'image du projectile
    game.player.all_projectiles.draw(screen)
    
    # Verifier si le joueur veut aller à droite ou à gauche
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    
    # Mettre à jour l'écran
    pygame.display.flip()
    
    # Si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # Que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
        # Détecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
            # Détecter si la touche espace est enclanchée pour lancer un projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
            
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False