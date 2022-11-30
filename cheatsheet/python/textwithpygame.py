import pygame

pygame.init()

# Define colors using hex codes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen size
HEIGHT = 400
WIDHT = 400

screen = pygame.display.set_mode((WIDHT, HEIGHT))

font = pygame.font.Font('freesansbold.ttf', 32)

text = font.render('This is text!', True, WHITE)

textRect = text.get_rect()
textRect.center = (WIDHT //2 , HEIGHT // 2)

while True:
    screen.fill(BLACK)
    screen.blit(text, textRect)

    for event in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
 
            # deactivates the pygame library
            pygame.quit()
 
            # quit the program.
            quit()

    pygame.display.update()