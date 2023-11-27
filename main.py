import pygame
from leveldesign import *
from character import Character
from cup import Cup
from pytmx.util_pygame import load_pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 960
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Definitely not Donkey Kong")
        tmx_data = load_pygame("./images/Hintergrund_nur_Platform.tmx")
        tiles = Tile.get_tiles(self, tmx_data)
        # returns time when it starts to run
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown_ms = 75
        self.frame = 0
        self.clock = pygame.time.Clock()
        self.character = Character(self, 40, 560, 75, 75, 50, 50)
        self.cups = [
            Cup(self, 200, 540, 20, 20),
            Cup(self, 280, 605, 20, 20),
            Cup(self, 320, 238, 20, 20),
            Cup(self, 450, 92, 20, 20),
            Cup(self, 510, 494, 20, 20),
            Cup(self, 600, 605, 20, 20),
            Cup(self, 690, 318, 20, 20),
            Cup(self, 870, 396, 20, 20),
            Cup(self, 890, 605, 20, 20),
        ]
        self.counter = 0
        self.font = pygame.font.Font(None, 36)
        self.run()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            self.delta_time = self.clock.tick(60) / 1000

            self.screen.fill(BLACK)
            self.screen.blit(BackGround.image, BackGround.rect)
            sprite_group.draw(self.screen)
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.animation_cooldown_ms:
                self.frame += 1
                self.last_update = current_time

            for (
                self.tile_rect
            ) in self.tiles_rects:  # tiles_rects enthält die Rechtecke der Tiles
                if self.character.rect.colliderect(self.tile_rect):
                    if (
                        self.character.rect.right
                        > self.tile_rect.left
                        > self.character.rect.left
                    ):
                        self.character.x = (
                            self.tile_rect.left - self.character.character_width
                        )
                    elif (
                        self.character.rect.left
                        < self.tile_rect.right
                        < self.character.rect.right
                    ):
                        self.character.x = self.tile_rect.right
                    if (
                        self.character.rect.bottom
                        > self.tile_rect.top
                        > self.character.rect.top
                    ):
                        self.character.y = (
                            self.tile_rect.top - self.character.character_height
                        )
                    elif (
                        self.character.rect.top
                        < self.tile_rect.bottom
                        < self.character.rect.bottom
                    ):
                        self.character.y = self.tile_rect.bottom

            self.character.update(self.frame)

            for cup in self.cups:
                cup.update()
                if cup.is_collected:
                    self.cups.remove(cup)
                    self.counter += 1
            self.display_counter()
            pygame.display.update()

        pygame.quit()

    def display_counter(self):
        text = self.font.render(f"gesammelte Objekte: {self.counter}", True, "blue")
        self.screen.blit(text, (self.screen_width - 300, 20))


game = Game()
