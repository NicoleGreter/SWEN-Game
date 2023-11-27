import pygame


class Cup:
    def __init__(self, game, x, y, cup_width, cup_height):
        self.x = x
        self.y = y
        self.cup_width = cup_width
        self.cup_height = cup_height
        self.game = game
        self.rect = pygame.Rect(self.x, self.y, cup_width, cup_height)
        self.is_collected = False
        self.picture_coffee_cup = pygame.image.load("./images/Objects/Coffee_Cup.png")
        self.picture_coffee_cup = pygame.transform.scale(
            self.picture_coffee_cup, (20, 20)
        )

    def draw(self):
        self.rect.x = self.x
        self.rect.y = self.y
        # pygame.draw.rect(self.game.screen, "yellow", self.rect)
        self.game.screen.blit(self.picture_coffee_cup, (self.x, self.y))

    def update(self):
        self.draw()
        if self.rect.colliderect(self.game.character.rect):
            self.is_collected = True
