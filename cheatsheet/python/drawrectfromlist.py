import pygame

pygame.init()

tiles = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
font = pygame.font.Font('freesansbold.ttf', 50)

screen = pygame.display.set_mode((600, 600))

pos = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
}

for i in range(1, 10):
    target = pos[i]
    number = tiles[target[0]][target[1]]
    print(number)


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)

    font = pygame.font.Font('freesansbold.ttf', 50)
    text = font.render('1', True, '#FFFFFF')
    screen.blit(text, (200//2,200//2))