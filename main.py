import pygame
from character import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Definitely not Donkey Kong")

    running = True

    character_position_x = 50
    character_position_y = 500

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            screen.blit(
                picture_minotaur_walking_right,
                (character_position_x, character_position_y),
                (300, 0, 75, 75),
            )
            character_position_x += CHARACTER_SPEED
            if character_position_x > SCREEN_WIDTH - CHARACTER_WIDTH:
                character_position_x = SCREEN_WIDTH - CHARACTER_WIDTH
        elif keys[pygame.K_LEFT]:
            screen.blit(
                picture_minotaur_walking_left,
                (character_position_x, character_position_y),
            )
            character_position_x -= CHARACTER_SPEED
            if character_position_x < 0:
                character_position_x = 0
        else:
            screen.blit(
                picture_minotaur_idle, (character_position_x, character_position_y)
            )
        pygame.display.update()


if __name__ == "__main__":
    main()
