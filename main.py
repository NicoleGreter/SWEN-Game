import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

CHARACTER_SPEED = 0.5
CHARACTER_WIDTH = 20
CHARACTER_HEIGHT = 20


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

        pygame.draw.rect(
            screen,
            WHITE,
            (
                character_position_x,
                character_position_y,
                CHARACTER_WIDTH,
                CHARACTER_HEIGHT,
            ),
        )

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            character_position_x += CHARACTER_SPEED
            if character_position_x > SCREEN_WIDTH - CHARACTER_WIDTH:
                character_position_x = SCREEN_WIDTH - CHARACTER_WIDTH
        if keys[pygame.K_LEFT]:
            character_position_x -= CHARACTER_SPEED
            if character_position_x < 0:
                character_position_x = 0

        pygame.display.update()


if __name__ == "__main__":
    main()
