import pygame

# Colors hex
WHITE = '#FFFFFF'
BLACK = '#000000'

# Window settings
WIDTH = 600
HEIGHT = 600

# Initiatera pygame
pygame.init()

# Sätter skärmens storlek
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Font setting
font = pygame.font.Font('freesansbold.ttf', 50)

# Settings
TILE_SIZE = 200
posX = 0
posY = 0
textX = 200
textY = 200

# Nummer att skriva i
number = 1

text = font.render(str(number), True, BLACK)

textRect = text.get_rect()
textRect.center = (posX//2, posY//2)

pygame.draw.rect(screen, WHITE, (0, 0, 200, 200))
screen.blit(text, textRect)

def draw_tiles(x, y, text, number, textX, textY):
    for i in range(3):
        pygame.draw.rect(screen, WHITE, (x, y, TILE_SIZE, TILE_SIZE))
        x += 200
    x = 0
    y += 200
    for i in range(3):
        pygame.draw.rect(screen, WHITE, (x, y, TILE_SIZE, TILE_SIZE))
        x += 200
        number += 1
    x = 0
    y += 200
    for i in range(3):
        pygame.draw.rect(screen, WHITE, (x, y, TILE_SIZE, TILE_SIZE))
        x += 200
        number += 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    draw_tiles(posX, posY, text, number, textX, textY)
    

    pygame.display.flip()