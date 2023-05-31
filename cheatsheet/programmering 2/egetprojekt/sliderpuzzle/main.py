# Importerar moduler
import pygame
import random
import time

# Importerar bilder och andra variablar
from sprites import *
from settings import *

# Spel klassen
class Game: 
    def __init__(self) -> None:
        # Startar pygame
        pygame.init()
        # Bestämmer storleken på skärmen
        self.screen = pygame.display.set_mode((height, width))
        # Bestämmer skärmens titelnamn
        pygame.display.set_caption(title)
        # Ger objektet en instansvariabel med klocka
        self.clock = pygame.time.Clock()

    def create_game(self):
        grid = [[x + y * game_size for x in range(1, game_size + 1)] for y in range(game_size)]
        grid[-1][-1] = 0
        return grid

    def draw_tiles(self):
        self.tiles = []
        for row, x in enumerate(self.tiles_grid):
            self.tiles.append([])
            for col, tile in enumerate(x):
                # Om den inte är tom (0) så betyder det att vi behöver rita en tile
                if tile != 0:
                    self.tiles[row].append(Tile(self, col, row, str(tile)))
                # Om det är en en nolla, alltså tom
                else: 
                    self.tiles[row].append(Tile(self, col, row, 'empty'))


    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.tiles_grid = self.create_game()
        self.tiles_grid_completed = self.create_game()


    def run(self):
        # Spelet körs
        self.playing = True
        # Medan self.playing är True
        while self.playing == True:
            # Låt klockan ticka efter den satta fps
            self.clock.tick(fps)
            # Startar event gettern
            self.events()
            # 
            self.update()
            #
            self.draw()

    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        # En linje ritas för varje rad som visas 
        for row in range(-1, game_size * tilesize, tilesize):
            # Ritar linjen på spelets skärm med färgen vit och längden med startposition row + 58 för 
            # att centrera allting och 20 för att de inte ska nudda toppen
            pygame.draw.line(self.screen, white, (row + center, margin_top), (row + center, game_size * tilesize + margin_top))

        for col in range(-1, game_size * tilesize, tilesize):
            pygame.draw.line(self.screen, white, (center, col + margin_top), (game_size * tilesize + center, col + margin_top))
        

    def draw(self):
        # Sätter/fyller i bakgrundsfärgen
        self.screen.fill(darkgray)
        # Ritar alla sprites i gruppen på skärmen
        self.all_sprites.draw(self.screen)
        # Ritar in spelbrickan
        self.draw_grid()
        # Ritar numren
        self.draw_tiles
        # Uppdaterar skärmen
        pygame.display.flip()

    def events(self):
        # Kollar varje event som sker med hjälp av pygames event getter
        for event in pygame.event.get():
            # Om användaren stänger skrämen så kallas detta och programmet avslutas
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

# Main spel loop
game = Game()
while True:
    # Skapar ett nytt spel
    game.new()
    # Kör spelet
    game.run()

# Detta är slutet av koden 