import pygame


class Character:
    def __init__(self, game, x, y, character_width, character_height):
        self.x = x
        self.y = y
        self.character_width = character_width
        self.character_height = character_height
        self.game = game
        self.surface = game.screen
        self.rect = pygame.Rect(
            self.x, self.y, self.character_width, self.character_height
        )

    def update(self):
        self.rect = pygame.Rect(
            self.x, self.y, self.character_width, self.character_height
        )
        self.movement(20)
        self.draw()

    def draw(self):
        pygame.draw.rect(self.surface, "yellow", (self.x, self.y, 75, 75))
        picture_minotaur_idle = pygame.image.load(
            "./images/Minotaur/PNG/PNG Sequences/Idle/0_Minotaur_Idle_000.png"
        )
        picture_minotaur_idle = pygame.transform.scale(
            picture_minotaur_idle, (self.character_width, self.character_height)
        )
        self.surface.blit(picture_minotaur_idle, (self.x, self.y))

    def movement(self, speed):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            picture_minotaur_walking_right = pygame.image.load(
                "./images/Minotaur/PNG/PNG Sequences/Walking/0_Minotaur_Walking_000.png"
            )
            picture_minotaur_walking_right = pygame.transform.scale(
                picture_minotaur_walking_right,
                (self.character_width, self.character_height),
            )
            self.x += speed * self.game.delta_time
            if self.x > self.game.screen_width - self.character_width:
                self.x = self.game.screen_width - self.character_width

        elif keys[pygame.K_LEFT]:
            picture_minotaur_walking_left = pygame.transform.flip(
                picture_minotaur_walking_right, True, False
            )
            self.x -= speed * self.game.delta_time
            if self.x < 0:
                self.x = 0

            self.surface.blit(picture_minotaur_walking_left, (self.x, self.y))
