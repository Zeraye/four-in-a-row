# importing libraries
import pygame
import draw
import const
import func
import var

# initializing all pygame functions
pygame.init()
# window creating
WINDOW = pygame.display.set_mode((const.SIDE, round(const.SIDE * (6 / 7))))
# setting title caption to window
pygame.display.set_caption('4 IN A ROW')

# main function
def main(screen):
    # creating clock
    clock = pygame.time.Clock()
    # main loop
    while True:
        clock.tick(const.FPS)
        for event in pygame.event.get():
            # closing game
            if event.type == pygame.QUIT:
                pygame.quit()
            # mouse click detection
            if event.type == pygame.MOUSEBUTTONDOWN:
                func.place(func.get_col(pygame.mouse.get_pos()))
        # drawing board and objects
        draw.draw(screen)

# running game
if __name__ == '__main__':
    main(WINDOW)
