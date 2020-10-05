# importing libraries
import pygame
import circ
import var
import const

# function that returning col from mouse position
def get_col(mouse_pos):
    return int(mouse_pos[0] // const.SQUARE_SIDE)

# function how which places are free in column
def get_row(col):
    rows = []
    for circ in var.circs:
        if circ.get_pos()[1] == col:
            rows.append(circ.get_pos()[0])
    return 5 if len(rows) == 0 else min(rows) - 1

# function for placing circle
def place(col):
    color = const.RED if var.player1 else const.BLUE
    if get_row(col) != -1:
        var.player1 = not var.player1
        var.circs.append(circ.Circ(get_row(col), col, color))
    if win(color):             
        var.circs = []
        var.player1 = True

#
def find(row, col, color):
    for circ in var.circs:
        if circ.get_pos() == (row, col) and circ.get_color() == color: return True
    return False

# function for checking win
def win(color):
    for row in range(6):
        for col in range(7):
            if find(row, col, color) == find(row + 1, col, color) == find(row + 2, col, color) == find(row + 3, col, color) == True or \
                find(row, col, color) == find(row, col + 1, color) == find(row, col + 2, color) == find(row, col + 3, color) == True or \
                find(row, col, color) == find(row + 1, col + 1, color) == find(row + 2, col + 2, color) == find(row + 3, col + 3, color) == True or \
                find(row, col, color) == find(row - 1, col + 1, color) == find(row - 2, col + 2, color) == find(row - 3, col + 3, color) == True: return True
    return False
