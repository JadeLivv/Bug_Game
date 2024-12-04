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
        self.rect = self.surf.get_rect()

    # Keypresses Move Player
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
    
    # Keep Player In the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Screen_W:
            self.rect.right = Screen_W
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= Screen_H:
            self.rect.bottom = Screen_H
        
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
        
    # Key currently pressed
    pressed_keys = pygame.key.get_pressed()
    # Update Player by keypresses
    player.update(pressed_keys)

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
    screen.blit(player.surf, player.rect)

    # Right to Left (flip screen)
    pygame.display.flip()

# Quit time :D
pygame.quit()