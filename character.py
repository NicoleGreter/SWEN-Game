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
        self.left = False
        self.right = True
        self.isjump = False
        self.jumpcount = 40
        self.game = game
        self.acceleration_x = acceleration_x
        self.speed_x = speed_x
        self.speed_y = speed_y
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
        # Jump Start Right
        self.jump_start_images_right = []
        for i in range(6):
            image_path = f"./images/Minotaur/PNG/PNG Sequences/Jump Start/0_Minotaur_Jump Start_{i:03d}.png"
            self.jump_start_images_right.append(
                pygame.transform.scale(
                    pygame.image.load(image_path).convert_alpha(),
                    (self.character_width, self.character_height),
                )
            )

        # Jump Start Left
        self.jump_start_images_left = []
        for i in range(6):
            image_path = f"./images/Minotaur/PNG/PNG Sequences/Jump Start/0_Minotaur_Jump Start_{i:03d}.png"
            self.jump_start_images_left.append(
                pygame.transform.flip(
                    pygame.transform.scale(
                        pygame.image.load(image_path).convert_alpha(),
                        (self.character_width, self.character_height),
                    ),
                    True,
                    False,
                )
            )

    def update(self, frame):
        # self.rect = pygame.Rect(
        #     self.x, self.y, self.character_width, self.character_height
        # )
        self.draw()
        self.movement(200, frame)
        self.checkcollisionsx(self.game.tiles_rects)

        keys = pygame.key.get_pressed()

        if self.left and keys[pygame.K_LEFT] and not (self.isjump):
            self.surface.blit(
                self.walking_left_images[frame % len(self.walking_left_images)],
                (self.x, self.y),
            )

        # self.horizental_movement(self.acceleration_x, frame)
        # self.vertical_movement(self.speed_y, frame)

        # def horizental_movement(self, acceleration_x, frame):
        #     keys = pygame.key.get_pressed()

        #     if keys[pygame.K_RIGHT]:
        #         if not keys[pygame.K_UP]:
        #             self.surface.blit(
        #                 self.walking_right_images[frame % len(self.walking_right_images)],
        #                 (self.x, self.y),
        #             )

        #         self.speed_x = acceleration_x
        #         self.x += self.speed_x * self.game.delta_time
        #         if self.x > self.game.screen_width - self.character_width:
        #             self.x = self.game.screen_width - self.character_width
        #     if keys[pygame.K_LEFT]:
        #         if not keys[pygame.K_UP]:
        #             self.surface.blit(
        #                 self.walking_left_images[frame % len(self.walking_left_images)],
        #                 (self.x, self.y),
        #             )
        #         self.speed_x = acceleration_x * -1
        #         self.x += self.speed_x * self.game.delta_time
        #         if self.x < 0:
        #             self.x = 0
        #     else:
        #         if not keys[pygame.K_UP]:
        #             self.surface.blit(
        #                 self.idle_images[frame % len(self.idle_images)],
        #                 (self.x, self.y),
        #             )

        # def vertical_movement(self, speed_y, frame):
        #     keys = pygame.key.get_pressed()

        #     if keys[pygame.K_UP]:
        if self.right and keys[pygame.K_RIGHT] and not (self.isjump):
            self.surface.blit(
                self.walking_right_images[frame % len(self.walking_right_images)],
                (self.x, self.y),
            )

        if self.isjump and self.right:
            self.surface.blit(
                self.jump_start_images_right[frame % len(self.jump_start_images_right)],
                (self.x, self.y),
            )

        if self.isjump and self.left:
            self.surface.blit(
                self.jump_start_images_left[frame % len(self.jump_start_images_left)],
                (self.x, self.y),
            )

    def movement(self, speed, frame):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and not (keys[pygame.K_LEFT]):
            self.right = True
            self.left = False
            self.x += speed * self.game.delta_time
            if self.x > self.game.screen_width - 75 + 24:
                self.x = self.game.screen_width - 75 + 24

        if keys[pygame.K_LEFT] and not (keys[pygame.K_RIGHT]):
            self.right = False
            self.left = True
            self.x -= speed * self.game.delta_time
            if self.x < -24:
                self.x = -24

        if not (self.isjump):
            if keys[pygame.K_SPACE]:
                self.isjump = True
        if self.isjump:
            if self.y > 560:
                self.y = 560
            if self.jumpcount >= -40:
                neg = 1
                self.jumpcount -= 1
                if self.jumpcount < 0:
                    neg = -1
                self.y -= ((self.jumpcount**2) * 0.5 * neg) * self.game.delta_time
                self.jumpcount -= 1
            else:
                self.isjump = False
                self.jumpcount = 40
        # self.y -= speed * self.game.delta_time

        if self.right and not (True in keys) and not (self.isjump):
            self.surface.blit(
                self.idle_images_right[frame % len(self.idle_images_right)],
                (self.x, self.y),
            )

        if self.left and not (True in keys) and not (self.isjump):
            self.surface.blit(
                self.idle_images_left[frame % len(self.idle_images_left)],
                (self.x, self.y),
            )

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
