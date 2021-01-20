'''
CS5001
Fall 2019
HW7 - Othello
'''

import turtle
import time

TILES = ("black", "white", "empty")


class Valid_Move:

    # PURPOSE
    # Constructor for individual Cells.
    # SIGNATURE
    # __init__ :: Valid_Move, Integer, Integer, String => Valid_Move
    def __init__(self, cell_num, flipped, color, direction, cells_flip):
        self.cell_num = cell_num
        self.flip_num = flipped
        self.color = color
        self.direction = direction
        self.cells_to_flip = cells_flip

    # PURPOSE
    # Return a string representation of the valid move
    # SIGNATURE
    # __str__ :: Object => String
    def __repr__(self):

        return str("[{}, {}, {}, {}, {}]" .format(self.cell_num, self.flip_num,
                    self.color, self.direction, self.cells_to_flip))

    # PURPOSE
    # defines greater than comparison of moves based on distance from the
    # edge of the board
    # SIGNATURE
    # __gt__ :: Object => String
    def __gt__(self, other):

        if self.cell_num > other.cell_num:
            return True
        if self.cell_num < other.cell_num:
            return False
