import pygame
from leveldesign import *
from character import Character
from game_object import Cup
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
        self.tiles = Tile.get_tiles(self, tmx_data)
        # returns time when it starts to run
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown_ms = 75
        self.gravity = 50
        self.frame = 0
        self.clock = pygame.time.Clock()
        self.character = Character(self, 40, 560, 75, 75, 200, 0)
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
        self.font_endgame = pygame.font.Font(None, 48)
        self.run()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE:
                        self.character.isjump = True

            self.delta_time = self.clock.tick(60) / 1000

            self.screen.fill(BLACK)
            self.screen.blit(BackGround.image, BackGround.rect)
            sprite_group.draw(self.screen)
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.animation_cooldown_ms:
                self.frame += 1
                self.last_update = current_time

            self.character.update(self.frame)

            for cup in self.cups:
                cup.update()
                if cup.is_collected:
                    self.cups.remove(cup)
                    self.counter += 1
            self.display_counter()

            if self.counter >= 1:
                text = self.font_endgame.render(f"COFFEE OVERLOAD", True, "saddlebrown")
                self.screen.blit(text, (300, 400))

            pygame.display.update()

        pygame.quit()

    def display_counter(self):
        text = self.font.render(f"gesammelte Objekte: {self.counter}", True, "blue")
        self.screen.blit(text, (self.screen_width - 300, 20))


game = Game()
