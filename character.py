import pygame


class Character:
    def __init__(
        self,
        game,
        x,
        y,
        character_width,
        character_height,
        acceleration,
        speed_x,
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
        self.acceleration = acceleration
        self.speed_x = speed_x
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
        self.horizental_movement(self.acceleration)
        self.checkcollisions_x(self.game.tiles_rects)
        self.vertical_movement()
        self.checkcollisions_y(self.game.tiles_rects)

        if (
            self.y > 560
        ):  # Character kann nicht weiter als unterste Ebene fallen, diese wurde nicht als Tile eingefügt
            self.y = 560

        keys = pygame.key.get_pressed()

        if (
            not self.isjump
        ):  # Character fällt mit einer Geschwindigkeit von 150, wenn er nicht aufgrund einer Collision auf etwas stehen bleibt
            self.y += 150 * self.game.delta_time

        if self.left and keys[pygame.K_LEFT] and not (self.isjump):
            self.surface.blit(
                self.walking_left_images[frame % len(self.walking_left_images)],
                (self.x, self.y),
            )

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

    def horizental_movement(self, acceleration):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.right = True
            self.left = False
            self.speed_x = acceleration
            self.x += self.speed_x * self.game.delta_time
            if self.x > self.game.screen_width - 75 + 24:
                self.x = self.game.screen_width - 75 + 24
        if keys[pygame.K_LEFT]:
            self.right = False
            self.left = True
            self.speed_x = -acceleration
            self.x += self.speed_x * self.game.delta_time
            if self.x < -24:
                self.x = -24

    def vertical_movement(self):
        if self.isjump:
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

    def get_hits(self, tiles_rects):
        hits = []
        for tile_rect in tiles_rects:
            if self.rect.colliderect(tile_rect):
                hits.append(tile_rect)
        return hits

    def checkcollisions_x(self, tiles):
        collisions = self.get_hits(tiles)
        for tile_rect in collisions:
            if self.speed_x > 0:
                self.speed_x = 0
            elif self.speed_x < 0:
                self.speed_x = 0

    def checkcollisions_y(self, tiles):
        keys = pygame.key.get_pressed()
        collisions = self.get_hits(tiles)
        for tile_rect in collisions:
            if self.jumpcount != 0 and not keys[pygame.K_SPACE]:
                self.isjump = False
                self.is_jumping = False
                self.y = tile_rect.top - 62
                self.jumpcount = 40

    def draw(self):
        self.rect.x = self.x + 20
        self.rect.y = self.y + 21
        # self.rect = pygame.draw.rect(
        #     self.surface, (0, 0, 0), (self.x + 20, self.y + 21, 31.25, 42.1)
        # )
