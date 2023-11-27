import pygame
from character import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


def main():
    pygame.init()

    # returns time when it starts to run
    last_update = pygame.time.get_ticks()
    animation_cooldown_ms = 75
    frame = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Definitely not Donkey Kong")

    running = True

    character_position_x = 50
    character_position_y = 500

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # returns the current_time and updates the animation
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown_ms:
            frame += 1
            last_update = current_time

        screen.fill(BLACK)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            screen.blit(
                walking_right_images[frame % len(walking_right_images)],
                (character_position_x, character_position_y),
            )
            character_position_x += CHARACTER_SPEED
            if character_position_x > SCREEN_WIDTH - CHARACTER_WIDTH:
                character_position_x = SCREEN_WIDTH - CHARACTER_WIDTH
        elif keys[pygame.K_LEFT]:
            screen.blit(
                walking_left_images[frame % len(walking_left_images)],
                (character_position_x, character_position_y),
            )
            character_position_x -= CHARACTER_SPEED
            if character_position_x < 0:
                character_position_x = 0
        elif keys[pygame.K_UP]:
            screen.blit(
                jump_start_images[frame % len(jump_start_images)],
                (character_position_x, character_position_y),
            )
            character_position_y -= CHARACTER_SPEED
            if character_position_x < 0:
                character_position_x = 0
        else:
            screen.blit(
                idle_images[frame % len(idle_images)],
                (character_position_x, character_position_y),
            )

        pygame.display.update()


if __name__ == "__main__":
    main()
