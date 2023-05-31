# Prevents __pycache__ folders from being created
import sys
sys.dont_write_bytecode = True

# Importerar moduler
import pygame
import random as r

# Importerar spelvariabler 
from settings import *

# Definerar spelklass
class Game: 
    def __init__(self):
        # Startar pygame
        pygame.init()
        # Bestämmer storleken på skärmen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Bestämmer skärmens titel
        pygame.display.set_caption(TITLE)
        self.finished = False
        self.first = True
        # x och y för text koordinat
        self.x = 10
        self.y = 10

    # Skapar spelets kompletta form
    def create_game(self):
        grid = []
        number = 1
        for x in range(3):
            l = []
            for y in range(3):
                l.append(number)
                number += 1
            grid.append(l)
        grid[-1][-1] = 0
        return grid

    # Ritar spelplanen
    def draw_grid(self):
        # Kollar om pusslet är löst
        self.finished = self.is_finished()
        # Om den är det så körs inte ritandet av spelplanen
        if self.finished == True:
            return

        # Ritar bakgrunden
        self.screen.fill(DARKGREY)
        pygame.display.flip()

        # Ritar rutnätet
        for row in range(-1, GAME_SIZE * TILE_SIZE - 1, TILE_SIZE):
            pygame.draw.line(self.screen, RED, (row, 0), (row, GAME_SIZE * TILE_SIZE))
        for col in range(-1, GAME_SIZE * TILE_SIZE - 1, TILE_SIZE):
            pygame.draw.line(self.screen, RED, (0, col), (GAME_SIZE * TILE_SIZE, col))
        
        # Definerar font och storlek
        font = pygame.font.Font('freesansbold.ttf', 50)
        for i in range(1, 10):
            # Får fram vilket nummer som är i ruta 1, ruta 2 osv
            target = pos[i]
            number = self.tiles_grid[target[0]][target[1]]
            text = font.render(str(number), True, WHITE)
            # Om det inte är en nolla, skriv ut siffran
            if number != 0:
                self.screen.blit(text, (self.x, self.y))

            self.x += 200
            if i == 3:
                self.y = self.y + 200
                self.x = 10
            if i == 6:
                self.y += 200
                self.x = 10
        self.x = 10
        self.y = 10
        self.first = False

    def draw(self):
        # Om finished inte är sant
        if self.finished != True:
            pygame.display.flip()
        else: return
        if self.first == True:
            # Ritar spelplanen
            self.draw_grid()

    # Skapar spelet
    def new(self):
        # Väljer en slumpmässad redan olöst plan 
        self.tiles_grid = shuffled[r.randint(1, 15)]
        # Skapar en kopia av den kompletta plane
        self.tiles_grid_completed = self.create_game()
        self.clicked = 0

    # Startar spelet
    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.draw()

    def move(self):        
        # Vilken ruta i 3x3 som trycks (ger tillbaka koordinaterna för att även finna den i nested list spelplanen)
        target = pos[self.clicked]  

        #Skriver vad som är där i just nu (också den som ska flyttas)
        current = self.tiles_grid[target[0]][target[1]]
        
        # Vilka som är grannar
        neighbours = ref[self.clicked]
        length = len(neighbours)

        for neighbour in neighbours:
             # Tittar ifall det är en nolla på någon av grannarna/kollar om den går att flytta dit
            nb = self.tiles_grid[neighbour[0]][neighbour[1]]
        
            # Är det det, så byt ut current mot nollan och vice versa
            if nb == 0:
                self.tiles_grid[neighbour[0]][neighbour[1]] = current
                self.tiles_grid[target[0]][target[1]] = 0

                # Avslutar for loop då inget har bytts ut
                continue 

            # Är det inte det, gör inget
            else: 
                pass

    # Kollar om pusslet är löst
    def is_finished(self):
        # Kollar om spelplanen är likadan som den kompletta spelplanen
        if self.tiles_grid == self.tiles_grid_completed:
            # Font och storlek
            font = pygame.font.Font('freesansbold.ttf', 100)

            # Text to be displayed if puzzle is finished
            text = font.render('You win!', True, WHITE)
            ctr = text.get_rect()
            ctr.center = (WIDTH // 2, HEIGHT // 2)

            # Sätter fram bakgrunden på nytt, så att spelplanen försvinner och skriv ut du vann!
            self.screen.fill(DARKGREY)
            self.screen.blit(text, ctr)
            pygame.display.flip()
            return True

    # Fångar upp vad som händer
    def events(self):
        for event in pygame.event.get():
            # Kollar efter om användaren stänger spelet för att stänga det på rätt sätt
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Vänster kollumnen
                if mouse_x < 200:
                    if mouse_y < 200: 
                        self.clicked = 1
                    if 200 < mouse_y < 400:
                        self.clicked = 4
                    if 400 < mouse_y < 600:
                        self.clicked = 7
                # Mitt kollumnen
                if 200 < mouse_x < 400:
                    if mouse_y < 200: 
                        self.clicked = 2
                    if 200 < mouse_y < 400:
                        self.clicked = 5
                    if 400 < mouse_y < 600:
                        self.clicked = 8
                # Höger kollumnen
                if 400 < mouse_x < 600:
                    if mouse_y < 200: 
                        self.clicked = 3
                    if 200 < mouse_y < 400:
                        self.clicked = 6
                    if 400 < mouse_y < 600:
                        self.clicked = 9
                self.move()
                self.draw_grid()

# Main game loop
game = Game()
while True:
    game.new()
    game.run()

# Det här är slutet av koden  