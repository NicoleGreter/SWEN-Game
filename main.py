import pygame

BLACK = (0, 0, 0)


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Definitely not Donkey Kong")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        pygame.display.update()


if __name__ == "__main__":
    main()
