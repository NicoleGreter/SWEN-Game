import pygame


class Character:
    def __init__(self, game, x, y, character_width, character_height):
        self.x = x
        self.y = y
        self.character_width = character_width
        self.character_height = character_height
        self.game = game
        self.surface = game.screen
        # Skalierung damit rectangle hinter charackter width = 75/900 * 375 = 31.25 und hight 75/900 * 505 = 42.1
        self.rect = pygame.Rect(self.x + 20, self.y + 21, 31.25, 42.1)
        # Idle blinking_right
        self.idle_images_right = []
        for i in range(18):
            image_path = f"./images/Minotaur/PNG/PNG Sequences/Idle Blinking/0_Minotaur_Idle Blinking_{i:03d}.png"
            self.idle_images_right.append(
                pygame.transform.scale(
                    pygame.image.load(image_path).convert_alpha(),
                    (self.character_width, self.character_height),
                )
            )
        # Idle blinking_left
        self.idle_images_left = []
        for i in range(18):
            image_path = f"./images/Minotaur/PNG/PNG Sequences/Idle Blinking/0_Minotaur_Idle Blinking_{i:03d}.png"
            self.idle_images_left.append(
                pygame.transform.flip(
                    pygame.transform.scale(
                        pygame.image.load(image_path).convert_alpha(),
                        (self.character_width, self.character_height),
                    ),
                    True,
                    False,
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
        self.jump_start_images = []
        for i in range(6):
            image_path = f"./images/Minotaur/PNG/PNG Sequences/Jump Start/0_Minotaur_Jump Start_{i:03d}.png"
            self.jump_start_images.append(
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
        self.movement(200, frame)

    def movement(self, speed, frame):
        isjump = False
        jumpcount = 10
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and not (keys[pygame.K_LEFT]):
            self.surface.blit(
                self.walking_right_images[frame % len(self.walking_right_images)],
                (self.x, self.y),
            )
            self.x += speed * self.game.delta_time
            if self.x > self.game.screen_width - 75 + 24:
                self.x = self.game.screen_width - 75 + 24
        if keys[pygame.K_LEFT] and not (keys[pygame.K_RIGHT]):
            self.surface.blit(
                self.walking_left_images[frame % len(self.walking_left_images)],
                (self.x, self.y),
            )
            self.x -= speed * self.game.delta_time
            if self.x < -24:
                self.x = -24
        if not (isjump):
            if keys[pygame.K_SPACE]:
                isjump = True
        else:
            if jumpcount >= -10:
                neg = 1
                self.surface.blit(
                    self.jump_start_images[frame % len(self.jump_start_images)],
                    (self.x, self.y),
                )
                if jumpcount < 0:
                    neg = -1
                y -= ((jumpcount**2) * 0.5 * neg) * self.game.delta_time
                jumpcount -= 1
            else:
                isjump = False
                jumpcount = 10
            # self.y -= speed * self.game.delta_time
            # if self.x < 0:
            #     self.x = 0
        if not (True in keys):
            self.surface.blit(
                self.idle_images_right[frame % len(self.idle_images_right)],
                (self.x, self.y),
            )

    def draw(self):
        self.rect.x = self.x + 20
        self.rect.y = self.y + 21
        # self.rect = pygame.draw.rect(
        #     self.surface, (0, 0, 0), (self.x + 20, self.y + 21, 31.25, 42.1)
        # )
