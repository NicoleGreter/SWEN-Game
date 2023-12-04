import pygame

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
    def __init__(self, pos, surf, groups, tmx_data):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.tmx_data = tmx_data

    def get_tiles(self, tmx_data):
        self.tiles_rects = []
        for layer in tmx_data.layers:
            for x, y, surf in layer.tiles():
                pos = (x * 16, y * 16)
                Tile(pos=pos, surf=surf, groups=sprite_group, tmx_data=tmx_data)
                tile_rect = pygame.Rect(pos, (16, 16))
                self.tiles_rects.append(tile_rect)
