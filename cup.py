import pygame


class Cup:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
        self.is_collected = False
        self.picture_coffee_cup = pygame.image.load("./images/Objects/Coffee_Cup.png")
        self.picture_coffee_cup = pygame.transform.scale(
            self.picture_coffee_cup, (30, 30)
        )

    def draw(self):
        pygame.draw.rect(self.game.screen, "black", self.rect)
        self.game.screen.blit(self.picture_coffee_cup, (self.x, self.y))

    def update(self):
        self.draw()
        if self.rect.colliderect(self.game.character.rect):
            self.is_collected = True
