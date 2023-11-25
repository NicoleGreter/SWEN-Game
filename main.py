import pygame
from character import Character
from cup import Cup

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 900
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Definitely not Donkey Kong")
        self.clock = pygame.time.Clock()
        self.character = Character(self, 200, 450, 150, 150)
        self.cups = [Cup(self, 400, 500), Cup(self, 600, 500), Cup(self, 500, 500)]
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
            self.character.update()

            for cup in self.cups:
                cup.update()
                if cup.is_collected:
                    self.cups.remove(cup)
                    self.counter += 1
            self.display_counter()
            pygame.display.update()

        pygame.quit()

    def display_counter(self):
        text = self.font.render(f"gesammelte Objekte: {self.counter}", True, WHITE)
        self.screen.blit(text, (self.screen_width - 300, 20))


game = Game()
