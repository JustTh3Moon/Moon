import pygame
from settings import *

pygame.font.init()

class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text):
        self.groups =  game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((tilesize, tilesize))
        self.x, self.y = x, y
        self.text = text
        self.rect = self.image.get_rect()
        if self.text != 'empty':
            self.font = pygame.font.SysFont('Consolas', 50)
            font_surface = self.font.render(self.text, True, red)
            self.image.fill(white)
            self.font_size = self.font.size(self.text)
            draw_x = (tilesize / 2) - self.font_size[0] / 2
            draw_y = (tilesize / 2) - self.font_size[1] / 2
            self.image.blit(font_surface, (draw_x, draw_y))
        else:
            self.image.fill(red)

    def update(self):
        self.rect.x = self.x * tilesize
        self.rect.y = self.y * tilesize

    def click(self, mouse_x, mouse_y):
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.bottom