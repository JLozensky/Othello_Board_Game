'''
CS5001
Fall 2019
HW7 - Othello
'''


from cell import Cell
from valid_move import Valid_Move

TILES = ("black", "white", "empty")
RIGHT = 1
LEFT = -1
DIRS = {
    "up": 0,
    "up_right": 1,
    "right": 2,
    "down_right": 3,
    "down": 4,
    "down_left": 5,
    "left": 6,
    "up_left": 7,
    0: "up",
    1: "up_right",
    2: "right",
    3: "down_right",
    4: "down",
    5: "down_left",
    6: "left",
    7: "up_left",
}

NEIGHBOR_NUM_INDEX = 0
NEIGHBOR_DIR = 1


class Cells:

    def __init__(self, size):

        self.size = size
        self.tiles_placed = 0
        self.max_tiles = size ** 2
        self.UP = self.size
        self.DOWN = -self.size

        # The other corners are the max and min of the cells
        self.TOP_LEFT_CORNER = ((self.size ** 2) - (self.size) + 1)
        self.BOTTOM_RIGHT_CORNER = self.size
        self.create_dict()

    # PURPOSE
    # Creates a nested list of Cell objects.
    # SIGNATURE
    # create_dict :: Cells => Nested List

    def create_dict(self):

        self.dict = {}
        for i in range(self.size ** 2):
            self.dict[i + 1] = Cell()
        for cell in self.dict:
            self.find_neighbors(cell)

    # PURPOSE
    # Used for placing the 1st 4 starting tiles
    # SIGNATURE
    # place_start_tile :: Cells, Integer, Integer, String => Bool
    def place_start_tile(self, row, col, color):

        key = self.get_key(row, col)
        cell = self.dict[key]
        cell.add_tile(color)
        self.tiles_placed += 1

    # PURPOSE
    # checks to see if a move is valid and if so updates the cell_object and
    # returns a set of the cells needing to be drawn on the board
    # SIGNATURE
    # place_tile :: Cells, Integer, Integer, String => Set<Integer>

    def place_tile(self, row, col, color):

        key = self.get_key(row, col)
        opp_color = self.find_opp_color(color)
        valid_move_lst = self.valid_moves(opp_color)
        key_set = set({})
        for move in valid_move_lst:
            if move.cell_num == key:
                temp_set = set(move.cells_to_flip)
                key_set.update(temp_set)
        for i in key_set:
            cell = self.dict[i]
            cell.add_tile(color)
        return key_set

    # PURPOSE
    # sums the number of each color of tile
    # SIGNATURE
    # count_tiles :: Cells => List<Int>

    def count_tiles(self):

        black = 0
        white = 0
        for cell in self.dict.values():
            if cell.tile == TILES[0]:
                black += 1
            elif cell.tile == TILES[1]:
                white += 1
        return [black, white]

    # PURPOSE
    # Translates a row and column reference into the key for the given Cell
    # SIGNATURE
    # get_key :: Cells, Integer, Integer  => Integer

    def get_key(self, row, col):

        key = (row * self.size) + (col + 1)
        return key

    # PURPOSE
    # Adds up, down, left, and right neighboring cells to each Cell object
    # SIGNATURE
    # find_neighbors :: Int  => None

    def find_neighbors(self, cell_key):

        neighbors = []
        current_cell = self.dict[cell_key]

        # check if the cell is not in the top row and append up neighbor
        if cell_key < self.TOP_LEFT_CORNER:
            up_num = cell_key + self.UP
            up_neighbor = [up_num, "up"]
            neighbors.append(up_neighbor)

        # check if the cell is not in the bottom row and append down neighbor
        if cell_key > self.BOTTOM_RIGHT_CORNER:
            down_num = cell_key + self.DOWN
            down_neighbor = [down_num, "down"]
            neighbors.append(down_neighbor)

        # check if the cell is not on the right edge and append right neighbor
        if cell_key % self.size != 0:
            right_num = cell_key + RIGHT
            right_neighbor = [right_num, "right"]
            neighbors.append(right_neighbor)

        # check if the cell is not on the left edge and append left neighbor
        if cell_key % self.size != 1:
            left_num = cell_key + LEFT
            left_neighbor = [left_num, "left"]
            neighbors.append(left_neighbor)

        # add helper function to identify the appropriate diagonal neighbors
        neighbors.extend(self.diag_neighbors(neighbors, cell_key))

        # adds the neighbors list to the Cell attribute
        current_cell.neighbors = neighbors

    # PURPOSE
    # Adds diagonal neighboring cells to the neighbors list for a Cell object
    # SIGNATURE
    # diag_neighbors() ::Cells, List, Integer => None

    def diag_neighbors(self, neighbor_lst, cell_num):

        NEIGHBOR_DIR = 1
        diagonal_neighbors = []
        for i in neighbor_lst:

            # if there is a right neighbor
            if "right" in i[NEIGHBOR_DIR]:

                # if the first neighbor's direction is up
                if neighbor_lst[0][NEIGHBOR_DIR] == "up":
                    up_right_num = cell_num + RIGHT + self.UP
                    up_right_neighbor = [up_right_num, "up_right"]
                    diagonal_neighbors.append(up_right_neighbor)

                # if there is a down neighbor
                for x in range(2):
                    if neighbor_lst[x][NEIGHBOR_DIR] == "down":
                        dwn_right_num = cell_num + RIGHT + self.DOWN
                        dwn_right_neighbor = [dwn_right_num, "down_right"]
                        diagonal_neighbors.append(dwn_right_neighbor)

            # if there is a left neighbor
            if "left" in i[NEIGHBOR_DIR]:

                # if the first neighbor's direction is up
                if neighbor_lst[0][NEIGHBOR_DIR] == "up":
                    up_lft_num = cell_num + LEFT + self.UP
                    up_lft_neighbor = [up_lft_num, "up_left"]
                    diagonal_neighbors.append(up_lft_neighbor)

                # if there is a down neighbor
                for x in range(2):
                    if neighbor_lst[x][NEIGHBOR_DIR] == "down":
                        dwn_lft_num = cell_num + LEFT + self.DOWN
                        dwn_lft_neighbor = [dwn_lft_num, "down_left"]
                        diagonal_neighbors.append(dwn_lft_neighbor)
        return diagonal_neighbors

    # PURPOSE
    # Determine whose turn it is or if the game is over and returns the result
    # SIGNATURE
    # game_state() :: Cells, String => String

    def game_state(self, current_turn):

        if self.tiles_placed == self.max_tiles:
            pass
        elif current_turn == TILES[0]:
            white_valid = self.validate_turn(TILES[1])
            if white_valid is True:
                return TILES[1]
            black_valid = self.validate_turn(TILES[0])
            if black_valid is True:
                return TILES[0]
        else:
            black_valid = self.validate_turn(TILES[0])
            if black_valid is True:
                return TILES[0]
            white_valid = self.validate_turn(TILES[1])
            if white_valid is True:
                return TILES[1]
        return "game_over"

    # PURPOSE
    # Determine whether a valid move is available for the given color
    # SIGNATURE
    # validate_turn() :: Cells, String => Bool

    def validate_turn(self, color):

        opp_color = self.find_opp_color(color)
        moves_lst = self.valid_moves(opp_color)
        if len(moves_lst) > 0:
            return True
        return False

    # PURPOSE
    # Build and return a list of valid_move objects for the given color
    # SIGNATURE
    # valid_moves() :: Cells, String => Set<Valid_Moves>

    def valid_moves(self, color):

        # iterate through dictionary to find cells of the given tile color
        valid_moves = []
        for x in self.dict:
            cell_object = self.dict[x]
            cell_color = cell_object.tile
            if color == cell_color:

                # find empty cells across from cells
                potentials = self.get_potentials(x, color)

                # find valid moves, turn them into objects, add to the list
                for i in potentials:
                    potential_move = i[0]
                    dir_num = i[1]
                    move = self.validate_move(color, potential_move, dir_num)
                    valid_moves.extend(move)
        return valid_moves

    # PURPOSE
    # Validate potential valid move and return as a Valid_Move object
    # SIGNATURE
    # validate_move() :: Cells, String, Integer, String => List<Valid_Moves>

    def validate_move(self, color, potential_move, dir_num):

        current_cell = potential_move
        current_color = self.find_opp_color(color)
        found_end = False
        current_cell_object = self.dict[current_cell]
        counter = 0
        cells_to_flip = []
        valid = False
        while found_end is False:
            counter += 1
            cells_to_flip.append(current_cell)
            prior_cell_object = current_cell_object
            current_cell = self.relative_cell_num(current_cell, dir_num)
            neighbor_lst = []
            for i in prior_cell_object.neighbors:
                neighbor_lst.append(i[NEIGHBOR_NUM_INDEX])
            if current_cell in neighbor_lst:
                current_cell_object = self.dict[current_cell]
                if current_cell_object.tile == current_color:
                    valid = True
                    found_end = True
            else:
                found_end = True
        if valid is True:
            return [Valid_Move(
                potential_move, counter, current_color, dir_num, cells_to_flip
            )]
        else:
            return []

    # PURPOSE
    # Returns the opposite color as a string
    # SIGNATURE
    # find_opp_color() :: Cells, String => String

    def find_opp_color(self, color):

        try:
            current_color = TILES.index(color)
            if current_color > 1:
                return TILES[2]
            opp_color = abs(current_color - 1)
            return TILES[opp_color]
        except Exception:
            return TILES[2]

    # PURPOSE
    # return empty cells from around the given cell that are across from a cell
    # of the opposite color
    # SIGNATURE
    # get_potentials() :: Cells, Integer, String => List<Valid_Moves>

    def get_potentials(self, cell_num, color):

        # since there are 8 total directions opposite neighbors are 4 away from
        # each other (starting with up as 0 and numbering clockwise)
        DIR_MIDDLE = 4

        NEIGHBOR_NUM_INDEX = 0
        NEIGHBOR_DIR = 1

        cell_object = self.dict[cell_num]
        valid_potentials_lst = []

        # put the cell numbers of all neighbors into a list
        neighbor_dir_num_lst = []
        for neighbor in cell_object.neighbors:
            neighbor_dir_num_lst.append(DIRS[neighbor[NEIGHBOR_DIR]])

        # check for empty cells
        for neighbor in cell_object.neighbors:
            potential_move = self.dict[neighbor[NEIGHBOR_NUM_INDEX]]
            if potential_move.tile == TILES[2]:

                # opposite neighbor's direction relative to the original cell
                opposite_neighbor_dir_num = int()
                direction_num = DIRS[neighbor[NEIGHBOR_DIR]]
                if direction_num < DIR_MIDDLE:
                    opposite_neighbor_dir_num = direction_num + DIR_MIDDLE
                else:
                    opposite_neighbor_dir_num = direction_num - DIR_MIDDLE

                # if the opposite neighbor is not empty and it is a neighbor of
                # the original cell, append the potentially valid move
                if neighbor_dir_num_lst.count(opposite_neighbor_dir_num) > 0:
                    opposite_neighbor = self.relative_cell_num(
                        cell_num, opposite_neighbor_dir_num
                    )
                    opposite_neighbor_cell = self.dict[opposite_neighbor]
                    if opposite_neighbor_cell.tile != TILES[2]:
                        valid_potentials_lst.append(
                            [neighbor[NEIGHBOR_NUM_INDEX],
                            opposite_neighbor_dir_num])
        return valid_potentials_lst

    # PURPOSE
    # Finds the key of a cell identified via direction from another cell
    # SIGNATURE
    # relative_cell_num() :: Cells, Integer, Integer => Integer

    def relative_cell_num(self, orig_cell_num, dir_num):

        relative_cell_num = int()
        text_dir = DIRS[dir_num]
        if text_dir == "up":  # 0
            relative_cell_num = orig_cell_num + self.UP
        elif text_dir == "up_right":  # 1
            relative_cell_num = orig_cell_num + self.UP + RIGHT
        elif text_dir == "right":  # 2
            relative_cell_num = orig_cell_num + RIGHT
        elif text_dir == "down_right":  # 3
            relative_cell_num = orig_cell_num + self.DOWN + RIGHT
        elif text_dir == "down":  # 4
            relative_cell_num = orig_cell_num + self.DOWN
        elif text_dir == "down_left":  # 5
            relative_cell_num = orig_cell_num + self.DOWN + LEFT
        elif text_dir == "left":  # 6
            relative_cell_num = orig_cell_num + LEFT
        else:  # 7
            relative_cell_num = orig_cell_num + self.UP + LEFT
        return relative_cell_num

    # PURPOSE
    # Controls the computer's turn
    # SIGNATURE
    # computer_move() :: Cells => Set<Integer>

    def computer_move(self):

        valid_move_lst = self.valid_moves(TILES[0])
        if len(valid_move_lst) == 0:
            return set({})

        # sort the list by cell number
        valid_move_lst.sort(key=lambda x: x.cell_num)
        current_move_set = set({})
        selected_move_set = set({})
        current_move = 0
        current_total = 0
        selected_total = -10000
        current_move_value = 0
        selected_move_value = 0
        selected_key_set = set({})

        # Combine the cells to be flipped by the same move then compare to find
        # the one with the highest comparison score
        for move in valid_move_lst:
            if move.cell_num == current_move or current_move == 0:
                current_move_set.add(move)
                current_move = move.cell_num
            else:
                current_move_value = self.calculate_comp_num(current_move)
                for move in current_move_set:
                    current_total += self.calculate_comp_num(move.cell_num)
                if current_total > selected_total or\
                    (current_total == selected_total and
                        current_move_value > selected_move_value):
                    selected_total = current_total
                    selected_move_set = current_move_set
                    selected_move_value = current_move_value
                current_move_set.clear
                current_move_set.add(move)
                current_move = move.cell_num
                current_total = 0
                current_move_value = 0
        for move in selected_move_set:
            place_set = set(move.cells_to_flip)
            selected_key_set.update(place_set)
        for key in selected_key_set:
            cell = self.dict[key]
            cell.add_tile(TILES[1])
        return selected_key_set

    # PURPOSE
    # Create a single number to compare valid moves based on the cell number
    # SIGNATURE
    # calculate_comp_num():: Cells, Integer => Integer

    def calculate_comp_num(self, key):

        total = 0
        MIDDLE = self.size // 2
        UPPER_RIGHT_CORNER = self.size ** 2
        URC_NEIGHBOR_ONE = UPPER_RIGHT_CORNER + LEFT
        URC_NEIGHBOR_TWO = UPPER_RIGHT_CORNER + self.DOWN
        URC_NEIGHBOR_THREE = UPPER_RIGHT_CORNER + LEFT + self.DOWN

        UPPER_LEFT_CORNER = UPPER_RIGHT_CORNER - (self.size - 1)
        ULC_NEIGHBOR_ONE = UPPER_LEFT_CORNER + RIGHT
        ULC_NEIGHBOR_TWO = UPPER_LEFT_CORNER + self.DOWN
        ULC_NEIGHBOR_THREE = UPPER_LEFT_CORNER + RIGHT + self.DOWN

        LOWER_RIGHT_CORNER = self.size
        LRC_NEIGHBOR_ONE = LOWER_RIGHT_CORNER + LEFT
        LRC_NEIGHBOR_TWO = LOWER_RIGHT_CORNER + self.UP
        LRC_NEIGHBOR_THREE = LOWER_RIGHT_CORNER + LEFT + self.UP

        LOWER_LEFT_CORNER = 1
        LLC_NEIGHBOR_ONE = LOWER_LEFT_CORNER + RIGHT
        LLC_NEIGHBOR_TWO = LOWER_LEFT_CORNER + self.UP
        LLC_NEIGHBOR_THREE = LOWER_LEFT_CORNER + RIGHT + self.UP

        CORNER_SET = [
            UPPER_LEFT_CORNER, UPPER_RIGHT_CORNER,
            LOWER_LEFT_CORNER, LOWER_RIGHT_CORNER
        ]

        CORNER_NEIGHBOR_SET = [
            URC_NEIGHBOR_ONE, URC_NEIGHBOR_TWO, URC_NEIGHBOR_THREE,
            ULC_NEIGHBOR_ONE, ULC_NEIGHBOR_TWO, ULC_NEIGHBOR_THREE,
            LRC_NEIGHBOR_ONE, LRC_NEIGHBOR_TWO, LRC_NEIGHBOR_THREE,
            LLC_NEIGHBOR_ONE, LLC_NEIGHBOR_TWO, LLC_NEIGHBOR_THREE
        ]

        if (key % self.size) == 0:
            col = self.size - 1
            row = key // self.size - 1
        else:
            col = (key % self.size) - 1
            row = key // self.size

        # take the absolute value of both col and row minus the midpoint of
        # the board size then add them together. This will more heavily
        # weight cells on the outside of the board while also allowing for
        # large numbers of tiles to succeed even if they are in the center
        # of the board.
        total += abs(col - MIDDLE) + abs(row - MIDDLE)

        # if a col or row is an even number from the edge it gets an extra
        # half point per cell since that makes it easier to obtain the edge
        # space or is an edge
        if col > MIDDLE and col % 2 == 1:
            total += .5
        elif col % 2 == 0:
            total += .5
        if row > MIDDLE and row % 2 == 1:
            total += .5
        elif row % 2 == 0:
            total += .5

        # a corner gets + 100 more since they are impossible to flip
        if key in CORNER_SET:
            total += 100

        # if a new cell would be placed next to a corner by the computer,
        # disincentivize this action
        if key != 0:
            cell_object = self.dict[key]
            if cell_object.tile == TILES[2]:
                if key in CORNER_NEIGHBOR_SET:
                    total -= 20
        return total

    # PURPOSE
    # represents the dictionary as a string showing all keys and values
    # SIGNATURE
    # __repr__ :: Cells => String

    def __repr__(self):

        msg = "Dictionary : \n"
        for i in self.dict:
            msg += str("{}: {}\n" .format(i, self.dict[i]))
        return msg
