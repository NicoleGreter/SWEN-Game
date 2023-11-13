import pygame

CHARACTER_SPEED = 0.1
CHARACTER_WIDTH = 75
CHARACTER_HEIGHT = 75

picture_minotaur_idle = pygame.image.load(
    "./images/Minotaur/PNG/PNG Sequences/Idle/0_Minotaur_Idle_000.png"
)
picture_minotaur_idle = pygame.transform.scale(
    picture_minotaur_idle, (CHARACTER_WIDTH, CHARACTER_HEIGHT)
)

picture_minotaur_walking_right = pygame.image.load(
    "./images/Minotaur/PNG/PNG Sequences/Walking/0_Minotaur_Walking_000.png"
)
picture_minotaur_walking_right = pygame.transform.scale(
    picture_minotaur_walking_right, (CHARACTER_WIDTH, CHARACTER_HEIGHT)
)
picture_minotaur_walking_left = pygame.transform.flip(
    picture_minotaur_walking_right, True, False
)
