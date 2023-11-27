import pygame


class Character:
    def __init__(self, game, x, y, character_width, character_height):
        self.x = x
        self.y = y
        self.character_width = character_width
        self.character_height = character_height
        self.game = game
        self.surface = game.screen
        self.rect = pygame.Rect(
            self.x, self.y, self.character_width, self.character_height
        )
        # Idle blinking_right
        self.idle_images = []
        for i in range(18):
            image_path = f"./images/Minotaur/PNG/PNG Sequences/Idle Blinking/0_Minotaur_Idle Blinking_{i:03d}.png"
            self.idle_images.append(
                pygame.transform.scale(
                    pygame.image.load(image_path).convert_alpha(),
                    (self.character_width, self.character_height),
                )
            )
        # Walking right
        self.walking_right_images = []
        for i in range(24):
            image_path = f"./images/Minotaur/PNG/PNG Sequences/Walking/0_Minotaur_Walking_{i:03d}.png"
            self.walking_right_images.append(
                pygame.transform.scale(
                    pygame.image.load(image_path).convert_alpha(),
                    (self.character_width, self.character_height),
                )
            )
        # Walking left
        self.walking_left_images = []
        for i in range(24):
            image_path = f"./images/Minotaur/PNG/PNG Sequences/Walking/0_Minotaur_Walking_{i:03d}.png"
            self.walking_left_images.append(
                pygame.transform.flip(
                    pygame.transform.scale(
                        pygame.image.load(image_path).convert_alpha(),
                        (self.character_width, self.character_height),
                    ),
                    True,
                    False,
                )
            )
        # Jump Start
        jump_start_images = []
        for i in range(6):
            image_path = f"./images/Minotaur/PNG/PNG Sequences/Jump Start/0_Minotaur_Jump Start_{i:03d}.png"
            jump_start_images.append(
                pygame.transform.scale(
                    pygame.image.load(image_path).convert_alpha(),
                    (self.character_width, self.character_height),
                )
            )

    def update(self, frame):
        # self.rect = pygame.Rect(
        #     self.x, self.y, self.character_width, self.character_height
        # )
        self.draw()
        self.movement(20, frame)

    def movement(self, speed, frame):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.surface.blit(
                self.walking_right_images[frame % len(self.walking_right_images)],
                (self.x, self.y),
            )
            self.x += speed * self.game.delta_time
            if self.x > self.game.screen_width - self.character_width:
                self.x = self.game.screen_width - self.character_width
        elif keys[pygame.K_LEFT]:
            self.surface.blit(
                self.walking_left_images[frame % len(self.walking_left_images)],
                (self.x, self.y),
            )
            self.x -= speed * self.game.delta_time
            if self.x < 0:
                self.x = 0
        elif keys[pygame.K_UP]:
            self.surface.blit(
                self.jump_start_images[frame % len(self.jump_start_images)],
                (self.x, self.y),
            )
            self.y -= speed * self.game.delta_time
            if self.x < 0:
                self.x = 0
        else:
            self.surface.blit(
                self.idle_images[frame % len(self.idle_images)],
                (self.x, self.y),
            )

    def draw(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect = pygame.draw.rect(self.surface, (0, 0, 0), (self.x, self.y, 75, 75))
