import pygame
from character import *
from object import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600


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

        screen.blit(picture_minotaur_idle, (character_position_x, character_position_y))
        screen.blit(picture_object_Coffee_Cup, (object_position_x, object_position_y))

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


def collect_coffee_cup():
    counter_text = font.render("Counter: {}".format(counter), True, white)
    counter = 0
    screen.blit(Counter_Text, 10, 10)
    if (
        character_position_x == object_position_x
        and character_position_y == object_position_y
    ):
        counter += 1
        object_position_x = -100
        object_position_y = -100

        collect_coffee_cup()


if __name__ == "__main__":
    main()
