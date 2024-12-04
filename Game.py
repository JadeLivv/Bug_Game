import pygame

# pygame.locals imports for key coordinates
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Setting up the screen for the game
Screen_W = 800
Screen_H = 600
screen = pygame.display.set_mode((Screen_W, Screen_H))

# Call on the surf to be the player (Using pygame.sprite.Sprite)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((0, 0, 0))
        self.ect = self.surf.get_rect()
        
pygame.init()   

# Instantiate Player
player = Player()

# Player will be able to quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        
        elif event.type == QUIT:
            running = False
        

    # Background Setting here
    screen.fill ((65, 153, 204))

    # Surface created with width & length
    #   surf = pygame.Surface((50, 50))
    # Color it
    #   surf.fill ((0, 0, 0))
    #   rect = surf.get_rect()

    # Test pygame.draw
    #   pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Move the surf to the center
    #surf_center = (
    #    (Screen_W-surf.get_width())/2,
    #    (Screen_H-surf.get_height())/2
    #)
    screen.blit(player.surf, (Screen_W/2, Screen_H/2))

    # Right to Left (flip screen)
    pygame.display.flip()

# Quit time :D
pygame.quit()