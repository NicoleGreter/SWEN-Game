import pygame
from character import *
from leveldesign import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Definitely not Donkey Kong")

    running = True

    character_position_x = 40
    character_position_y = 560

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        screen.blit(BackGround.image, BackGround.rect)

        screen.blit(picture_minotaur_idle, (character_position_x, character_position_y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            screen.blit(
                picture_minotaur_walking_right,
                (character_position_x, character_position_y),
            )
            character_position_x += CHARACTER_SPEED
            if character_position_x > SCREEN_WIDTH - CHARACTER_WIDTH:
                character_position_x = SCREEN_WIDTH - CHARACTER_WIDTH
        if keys[pygame.K_LEFT]:
            screen.blit(
                picture_minotaur_walking_left,
                (character_position_x, character_position_y),
            )
            character_position_x -= CHARACTER_SPEED
            if character_position_x < 0:
                character_position_x = 0

        pygame.display.update()


if __name__ == "__main__":
    main()
