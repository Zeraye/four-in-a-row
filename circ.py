# importing libraries
import pygame
import var
import const

# circle class
class Circ:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    # getting circle position
    def get_pos(self):
        return self.row, self.col

    # getting circle color
    def get_color(self):
        return self.color

    # circle drawing function
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.col * const.SQUARE_SIDE, self.row * const.SQUARE_SIDE, const.SQUARE_SIDE, const.SQUARE_SIDE))

    # deleting circle
    def delete(self):
        var.circs.remove(self)
        del self
