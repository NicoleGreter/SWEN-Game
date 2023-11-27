import pygame
from pytmx.util_pygame import load_pygame

num_columns = 60
num_rows = 50
tile_size = 16
screen_width = num_columns * tile_size
screen_height = num_rows * tile_size

tilemap_image = pygame.image.load("./images/Leveldesign_ohne_Platform.png")


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = image_file
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


BackGround = Background(tilemap_image, [0, 0])


sprite_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
