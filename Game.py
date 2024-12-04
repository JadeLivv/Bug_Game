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

pygame.init()

#Setting up the screen for the game
Screen_W = 800
Screen_H = 600
screen = pygame.display.set_mode((Screen_W, Screen_H))

# Player will be able to quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background Setting here
    screen.fill ((65, 153, 204))

    #Test pygame.draw
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    #Right to Left (flip screen)
    pygame.display.flip()

#Quit time :D
pygame.quit()