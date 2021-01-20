'''
CS5001
Fall 2019
HW7 - Othello
'''

import turtle
import time
from cells import Cells


SQUARE = 75
MIDPOINT = (SQUARE + 1) // 2
RADIUS = 25
TILES = ("black", "white", "empty")
NUM_SIDES = 4
RIGHT_ANGLE = 90


class Board:

    # PURPOSE
    # Constructor for the Board class. size should be an efden integer.
    # SIGNATURE
    # __init__ :: Board, Integer => Board

    def __init__(self, size):
        self.size = size
        self.high_bound = SQUARE * size / 2
        self.low_bound = 0 - self.high_bound
        self.cells = Cells(self.size)
        self.turn = TILES[0]

    # PURPOSE
    # Draws the board.
    # SIGNATURE
    # draw_board :: Board => None

    def draw_board(self):
        global NUM_SIDES
        global RIGHT_ANGLE
        turtle.setup(self.size * SQUARE, self.size * SQUARE)
        turtle.screensize(self.size * SQUARE, self.size * SQUARE)
        turtle.bgcolor("blue")
        turtle.setworldcoordinates(
            0, 0, (SQUARE * self.size), (SQUARE * self.size)
        )

        # Create the turtle to draw the board
        self.othello = turtle.Turtle()  # This defines the drawing tool
        self.othello.penup()
        self.othello.speed(0)
        self.othello.hideturtle()

        # Line color is black, fill color is turquoise
        self.othello.color("black", "turquoise")

        # Move the turtle to the upper left corner
        corner = 0
        self.othello.setposition(0, 0)

        # Draw the green background
        self.othello.begin_fill()
        for i in range(NUM_SIDES):
            self.othello.pendown()
            self.othello.forward(SQUARE * self.size)
            self.othello.left(RIGHT_ANGLE)
        self.othello.end_fill()
        self.othello.penup()

        # Draw the horizontal lines
        for i in range(self.size + 1):
            self.othello.setposition(corner, SQUARE * i + corner)
            self.draw_lines(self.othello, self.size)

        # Draw the vertical lines
        self.othello.left(RIGHT_ANGLE)
        for i in range(self.size + 1):
            self.othello.setposition(SQUARE * i + corner, corner)
            self.draw_lines(self.othello, self.size)

        # Draw the 4 start pieces
        self.start_pieces()

        # Get the reference to the screen
        screen = turtle.Screen()
        # Listen for click events
        screen.onclick(self.board_click)  # calls self.board_click when a click
        # happens, right now it only prints but this is where you'll want to
        # make actions happen.

        # Stops the window from closing
        turtle.done()

    # PURPOSE
    # prints victory message
    # SIGNATURE
    # victory_message :: Object => None

    def victory_message(self):
        global NUM_SIDES
        global RIGHT_ANGLE
        turtle.screensize(self.size * SQUARE, self.size * SQUARE)
        turtle.bgcolor("blue")
        turtle.setworldcoordinates(
            0, 0, (SQUARE * self.size), (SQUARE * self.size)
        )

        # Create the turtle to draw the board
        self.othello = turtle.Turtle()  # This defines the drawing tool
        self.othello.penup()
        self.othello.speed(0)
        self.othello.hideturtle()

        # Line color is black, fill color is turquoise
        self.othello.color("black", "turquoise")

        # Move the turtle to the upper left corner
        CORNER = 0
        self.othello.setposition(CORNER, CORNER)

        # Draw the turquoise background
        self.othello.begin_fill()
        for i in range(NUM_SIDES):
            self.othello.pendown()
            self.othello.forward(SQUARE * self.size)
            self.othello.left(RIGHT_ANGLE)
        self.othello.end_fill()
        self.othello.penup()
        self.othello.setposition(
            SQUARE * (self.size // 2), SQUARE * (self.size // 2)
        )
        self.othello.pendown()

        # get scores and find winner
        scores = self.cells.count_tiles()
        winner = ""
        if scores[0] > scores[1]:
            winner = str(TILES[0]) + " wins"
        elif scores[0] == scores[1]:
            winner = "Both tie"
        else:
            winner = str(TILES[1] + " wins")

        # write winner screen
        self.othello.write(
            "The game is over!\n{}, black: {} white: {}."
            .format(winner, scores[0], scores[1]), move=False, align="center",
            font=("Arial", 12, "normal")
        )
        name = input("Please enter your name challenger.\n")
        self.update_scores(name, scores[0])
        turtle.bye()

    # PURPOSE
    # Creates and/or appends the scores file
    # SIGNATURE
    # draw_lines :: Board, String, Int, Int => None

    def update_scores(self, player_name, player_score):
        filepath = "scores.txt"
        scores_lst = []
        new_line = str("{} {}\n" .format(player_name, player_score))
        # new_line_beginning = str("{} {}" .format(player_name, player_score))
        try:
            with open(filepath, "r") as file:
                for line in file:
                    scores_lst.append(line)
                if len(scores_lst) > 0:
                    top_score = scores_lst[0]
                    top_score = top_score.rstrip()
                    top_score = top_score.rsplit(" ", 1)
                    score_only = int(top_score[1])
                    if player_score > score_only:
                        scores_lst.insert(0, new_line)
                    else:
                        scores_lst.append(new_line)
        except FileNotFoundError:
            scores_lst.append(new_line)
        file = open(filepath, "w")
        file.writelines(scores_lst)
        file.close()

    # PURPOSE
    # Helper function to draw the lines on the board
    # SIGNATURE
    # draw_lines :: Board, Turtle, Integer => None

    def draw_lines(self, turt, n):

        turt.pendown()
        turt.forward(SQUARE * n)
        turt.penup()

    # PURPOSE
    # Helper function returning the center coordinates of a square on the board.
    # SIGNATURE
    # get_center :: Board, Integer, Integer => (Integer, Integer)

    def get_center(self, col, row):

        x = col * SQUARE + MIDPOINT + RADIUS
        y = row * SQUARE + MIDPOINT
        return (x, y)

    # PURPOSE
    # Draw a tile of a given color in a given square on the board
    # SIGNATURE
    # draw_piece :: Board, Integer, Integer => None

    def draw_piece(self, col, row):

        # Draws the tile
        global TILES
        start = self.get_center(col, row)
        self.othello.penup()
        self.othello.setposition(start[0], start[1])
        self.othello.pendown()
        self.othello.begin_fill()
        self.othello.color(TILES[0], self.turn)
        self.othello.circle(RADIUS)
        self.othello.end_fill()

    # PURPOSE
    # Determine whose turn it is or if the game is over
    # SIGNATURE
    # change_turn :: Board => None

    def change_turn(self):

        game_state = self.cells.game_state(self.turn)
        if game_state == "game_over":
            self.victory_message()
        else:
            self.turn = game_state
            print(str("It is now {}'s turn" .format(game_state)))
            if self.turn == TILES[1]:
                cell_key_set = self.cells.computer_move()
                for key in cell_key_set:
                    if (key % self.size) == 0:
                        col = self.size - 1
                        row = key // self.size - 1
                    else:
                        col = (key % self.size) - 1
                        row = key // self.size
                    self.draw_piece(col, row)
                self.cells.tiles_placed += 1
                self.change_turn()
            else:
                pass

    # PURPOSE
    # Helper function that draws the 4 starting pieces.
    # SIGNATURE
    # start_pieces :: Board => None

    def start_pieces(self):

        row_upper = self.size // 2
        row_lower = self.size // 2 - 1
        col_left = self.size // 2 - 1
        col_right = self.size // 2

        self.cells.place_start_tile(row_upper, col_left, self.turn)
        self.draw_piece(col_left, row_upper)
        turn_num = abs(TILES.index(self.turn) - 1)
        self.turn = TILES[turn_num]

        self.cells.place_start_tile(row_upper, col_right, self.turn)
        self.draw_piece(col_right, row_upper)
        turn_num = abs(TILES.index(self.turn) - 1)
        self.turn = TILES[turn_num]

        self.cells.place_start_tile(row_lower, col_right, self.turn)
        self.draw_piece(col_right, row_lower)
        turn_num = abs(TILES.index(self.turn) - 1)
        self.turn = TILES[turn_num]

        self.cells.place_start_tile(row_lower, col_left, self.turn)
        self.draw_piece(col_left, row_lower)
        turn_num = abs(TILES.index(self.turn) - 1)
        self.turn = TILES[turn_num]

    # PURPOSE
    # Handles mouse clicks on the board. Returns the column and row of the
    # board that is clicked on.
    # SIGNATURE
    # board_click :: Board, Int, Int => None

    def board_click(self, x, y):

        # print(x, y)
        col = int(x // SQUARE)
        row = int(y // SQUARE)
        if self.turn == TILES[0]:
            cell_key_set = self.cells.place_tile(row, col, self.turn)
            if len(cell_key_set) > 0:
                for key in cell_key_set:
                    if (key % self.size) == 0:
                        col = self.size - 1
                        row = key // self.size - 1
                    else:
                        col = (key % self.size) - 1
                        row = key // self.size
                    self.draw_piece(col, row)
                self.cells.tiles_placed += 1
                self.change_turn()
        else:
            pass
