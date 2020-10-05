# importing libraries
import pygame
import const
import var
import circ

# cricles drawing function
def draw_circs(screen):
    for circ in var.circs:
        circ.draw(screen)

def draw_lines(screen):
    for i in range(6):
        pygame.draw.line(screen, const.WHITE, ((i + 1) * const.SQUARE_SIDE, 0), ((i + 1) * const.SQUARE_SIDE, const.SIDE))
        pygame.draw.line(screen, const.WHITE, (0, (i + 1) * const.SQUARE_SIDE), (const.SIDE, (i + 1) * const.SQUARE_SIDE))

# main drawing function
def draw(screen):
    screen.fill(const.BLACK)
    draw_circs(screen)
    draw_lines(screen)
    pygame.display.flip()
