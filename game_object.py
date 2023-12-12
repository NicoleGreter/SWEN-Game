import pygame


# Initiierung der Klasse "Cup", welche im Game als Sammelobjekt verwendet wird.
# Mit dem Rectangle (aus pygame.Rect), wird die Spielfigur und das Objekt umrahmt und so die Kollision über die colliderect Funktion möglich
class Cup:
    def __init__(self, game, x, y, cup_width, cup_height):
        self.x = x
        self.y = y
        self.cup_width = cup_width
        self.cup_height = cup_height
        self.game = game
        self.rect = pygame.Rect(
            self.x, self.y, cup_width, cup_height
        )  # hier wird das Rechteck von pygame abgerufen und hinter das Objekt "Cup" mit der entsprechenden Breite und Höhe platziert
        self.is_collected = False
        self.picture_coffee_cup = pygame.image.load("./images/Objects/Coffee_Cup.png")
        self.picture_coffee_cup = pygame.transform.scale(
            self.picture_coffee_cup, (20, 20)
        )

    def draw(self):
        self.rect.x = self.x
        self.rect.y = self.y
        # pygame.draw.rect(self.game.screen, "yellow", self.rect)
        # die obige Zeile haben wir ausgeklammert, damit das Rechteck nicht effektiv gezeichnet wird und hinter dem Objekt ersichtlich wird. Für die Prüfung der Kollision war es aber sehr hilfreich zu zeichnen.
        self.game.screen.blit(self.picture_coffee_cup, (self.x, self.y))

    def update(self):
        self.draw()
        if self.rect.colliderect(self.game.character.rect):
            self.is_collected = True
            # mit dieser if-Bedingung wird sichergestellt, dass die Variable "is_collected" bei einer Kollision auf "True" gesetzt wird und den Ursprungsstatus von "False" überschreibt
            # Im Main wird diese Variable in der Update Funktion verwendet um "eingesammelte" Tassen (also "is_collected = True") aus der Liste "cups" zu entfernen.
