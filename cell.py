'''
CS5001
Fall 2019
HW7 - Othello
'''


import turtle
import time


SIDE_LENGTH = 75
RADIUS = 60
TILES = ("black", "white", "empty")


class Cell:

    # PURPOSE
    # Constructor for individual Cells.
    # SIGNATURE
    # __init__ :: Object => Cell

    def __init__(self):
        global TILES
        self.tile = TILES[2]
        self.neighbors = []

    # PURPOSE
    # changes the tile attribute to the given string
    # SIGNATURE
    # add_tile :: Object, String => None

    def add_tile(self, tile_color):
        self.tile = tile_color

    # PURPOSE
    # Return a string representation of the cell i.e. empty, False
    # SIGNATURE
    # __str__ :: Object => String
    def __repr__(self):
        return str(
            "['{}', {}]" .format(self.tile, self.neighbors)
        )
