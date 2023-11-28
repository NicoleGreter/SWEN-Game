import pygame


class Character:
    def __init__(
        self,
        game,
        x,
        y,
        character_width,
        character_height,
        acceleration_x,
        speed_x,
        speed_y,
    ):
        self.x = x
        self.y = y
        self.character_width = character_width
        self.character_height = character_height
        self.game = game
        self.acceleration_x = acceleration_x
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.surface = game.screen
        # Skalierung damit rectangle hinter charackter width = 75/900 * 375 = 31.25 und hight 75/900 * 505 = 42.1
        self.rect = pygame.Rect(self.x + 20, self.y + 21, 31.25, 42.1)
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
        self.horizental_movement(self.acceleration_x, frame)
        self.vertical_movement(self.speed_y, frame)
        self.checkcollisionsx(self.game.tiles_rects)

    def horizental_movement(self, acceleration_x, frame):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if not keys[pygame.K_UP]:
                self.surface.blit(
                    self.walking_right_images[frame % len(self.walking_right_images)],
                    (self.x, self.y),
                )

            self.speed_x = acceleration_x
            self.x += self.speed_x * self.game.delta_time
            if self.x > self.game.screen_width - self.character_width:
                self.x = self.game.screen_width - self.character_width
        if keys[pygame.K_LEFT]:
            if not keys[pygame.K_UP]:
                self.surface.blit(
                    self.walking_left_images[frame % len(self.walking_left_images)],
                    (self.x, self.y),
                )
            self.speed_x = acceleration_x * -1
            self.x += self.speed_x * self.game.delta_time
            if self.x < 0:
                self.x = 0
        else:
            if not keys[pygame.K_UP]:
                self.surface.blit(
                    self.idle_images[frame % len(self.idle_images)],
                    (self.x, self.y),
                )

    def vertical_movement(self, speed_y, frame):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.surface.blit(
                self.jump_start_images[frame % len(self.jump_start_images)],
                (self.x, self.y),
            )
            self.y -= speed_y * self.game.delta_time
            if self.x < 0:
                self.x = 0

    def get_hits(self, tiles_rects):
        hits = []
        for tile_rect in tiles_rects:
            if self.rect.colliderect(tile_rect):
                hits.append(tile_rect)
        return hits

    def checkcollisionsx(self, tiles):
        collisions = self.get_hits(tiles)
        for tile_rect in collisions:
            if self.speed_x > 0:  # Hit tile moving right
                self.x = tile_rect.left - 52
                self.rect.x = self.x
                self.speed_x = 0
            elif self.speed_x < 0:  # Hit tile moving left
                self.x = tile_rect.right - 21
                self.rect.x = self.x
                self.speed_x = 0

    def draw(self):
        self.rect.x = self.x + 20
        self.rect.y = self.y + 21
        # self.rect = pygame.draw.rect(
        #     self.surface, (0, 0, 0), (self.x + 20, self.y + 21, 31.25, 42.1)
        # )
