'''
CS5001
Fall 2019
HW7 - Othello
'''
import sys
import time
import turtle
from board import Board

sys.setrecursionlimit(1500)

TILES = ("black", "white", "empty")


def main():
    OTHELLO_SIZE = 8
    size = OTHELLO_SIZE
    board = Board(size)
    board.draw_board()


main()
