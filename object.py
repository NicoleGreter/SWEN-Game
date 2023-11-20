import pygame

OBJECT_WIDTH = 30
OBJECT_HEIGHT = 30
object_position_x = 400
object_position_y = 500


class Object:
    def __init__(
        self, OBJECT_WIDTH, OBJECT_HEIGHT, object_position_x, object_position_y
    ):
        self.OBJECT_WIDTH = OBJECT_WIDTH
        self.OBJECT_HEIGHT = OBJECT_HEIGHT
        self.object_position_x = object_position_x
        self.object_position_y = object_position_y


"""Objekt Klassen verwalten"""

Coffee_Cup = Object(30, 30, 400, 500)

picture_object_Coffee_Cup = pygame.image.load("./images/Objects/Coffee_Cup.png")
picture_object_Coffee_Cup = pygame.transform.scale(
    picture_object_Coffee_Cup, (OBJECT_WIDTH, OBJECT_HEIGHT)
)
