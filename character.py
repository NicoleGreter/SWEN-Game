import pygame

CHARACTER_SPEED = 0.1
CHARACTER_WIDTH = 75
CHARACTER_HEIGHT = 75

# Idle blinking_right
idle_images = []
for i in range(18):
    image_path = f"./images/Minotaur/PNG/PNG Sequences/Idle Blinking/0_Minotaur_Idle Blinking_{i:03d}.png"
    idle_images.append(
        pygame.transform.scale(
            pygame.image.load(image_path), (CHARACTER_WIDTH, CHARACTER_HEIGHT)
        )
    )

# Walking right
walking_right_images = []
for i in range(24):
    image_path = (
        f"./images/Minotaur/PNG/PNG Sequences/Walking/0_Minotaur_Walking_{i:03d}.png"
    )
    walking_right_images.append(
        pygame.transform.scale(
            pygame.image.load(image_path), (CHARACTER_WIDTH, CHARACTER_HEIGHT)
        )
    )

# Walking left
walking_left_images = []
for i in range(24):
    image_path = (
        f"./images/Minotaur/PNG/PNG Sequences/Walking/0_Minotaur_Walking_{i:03d}.png"
    )
    walking_left_images.append(
        pygame.transform.flip(
            pygame.transform.scale(
                pygame.image.load(image_path), (CHARACTER_WIDTH, CHARACTER_HEIGHT)
            ),
            True,
            False,
        )
    )
