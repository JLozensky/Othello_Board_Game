from cells import Cells
from valid_move import Valid_Move
from cell import Cell


def test_create_dict():
    # I couldn't figure out how to format this according to the style guide
    # (70 char limit per line) without messing up the test
    # This also tests find neighbors and diag_neighbors since their outputs
    # make up the neighbors list in each Cell object
    x = Cells(8)
    y = x.dict
    assert(str(y[1]) == "['empty', [[9, 'up'], [2, 'right'], [10, 'up_right']]]")
    assert(str(y[2]) == "['empty', [[10, 'up'], [3, 'right'], [1, 'left'], [11, 'up_right'], [9, 'up_left']]]")
    assert(str(y[3]) == "['empty', [[11, 'up'], [4, 'right'], [2, 'left'], [12, 'up_right'], [10, 'up_left']]]")
    assert(str(y[4]) == "['empty', [[12, 'up'], [5, 'right'], [3, 'left'], [13, 'up_right'], [11, 'up_left']]]")
    assert(str(y[5]) == "['empty', [[13, 'up'], [6, 'right'], [4, 'left'], [14, 'up_right'], [12, 'up_left']]]")
    assert(str(y[6]) == "['empty', [[14, 'up'], [7, 'right'], [5, 'left'], [15, 'up_right'], [13, 'up_left']]]")
    assert(str(y[7]) == "['empty', [[15, 'up'], [8, 'right'], [6, 'left'], [16, 'up_right'], [14, 'up_left']]]")
    assert(str(y[8]) == "['empty', [[16, 'up'], [7, 'left'], [15, 'up_left']]]")
    assert(str(y[9]) == "['empty', [[17, 'up'], [1, 'down'], [10, 'right'], [18, 'up_right'], [2, 'down_right']]]")
    assert(str(y[10]) == "['empty', [[18, 'up'], [2, 'down'], [11, 'right'], [9, 'left'], [19, 'up_right'], [3, 'down_right'], [17, 'up_left'], [1, 'down_left']]]")
    assert(str(y[11]) == "['empty', [[19, 'up'], [3, 'down'], [12, 'right'], [10, 'left'], [20, 'up_right'], [4, 'down_right'], [18, 'up_left'], [2, 'down_left']]]")
    assert(str(y[12]) == "['empty', [[20, 'up'], [4, 'down'], [13, 'right'], [11, 'left'], [21, 'up_right'], [5, 'down_right'], [19, 'up_left'], [3, 'down_left']]]")
    assert(str(y[13]) == "['empty', [[21, 'up'], [5, 'down'], [14, 'right'], [12, 'left'], [22, 'up_right'], [6, 'down_right'], [20, 'up_left'], [4, 'down_left']]]")
    assert(str(y[14]) == "['empty', [[22, 'up'], [6, 'down'], [15, 'right'], [13, 'left'], [23, 'up_right'], [7, 'down_right'], [21, 'up_left'], [5, 'down_left']]]")
    assert(str(y[15]) == "['empty', [[23, 'up'], [7, 'down'], [16, 'right'], [14, 'left'], [24, 'up_right'], [8, 'down_right'], [22, 'up_left'], [6, 'down_left']]]")
    assert(str(y[16]) == "['empty', [[24, 'up'], [8, 'down'], [15, 'left'], [23, 'up_left'], [7, 'down_left']]]")
    assert(str(y[17]) == "['empty', [[25, 'up'], [9, 'down'], [18, 'right'], [26, 'up_right'], [10, 'down_right']]]")
    assert(str(y[18]) == "['empty', [[26, 'up'], [10, 'down'], [19, 'right'], [17, 'left'], [27, 'up_right'], [11, 'down_right'], [25, 'up_left'], [9, 'down_left']]]")
    assert(str(y[19]) == "['empty', [[27, 'up'], [11, 'down'], [20, 'right'], [18, 'left'], [28, 'up_right'], [12, 'down_right'], [26, 'up_left'], [10, 'down_left']]]")
    assert(str(y[20]) == "['empty', [[28, 'up'], [12, 'down'], [21, 'right'], [19, 'left'], [29, 'up_right'], [13, 'down_right'], [27, 'up_left'], [11, 'down_left']]]")
    assert(str(y[21]) == "['empty', [[29, 'up'], [13, 'down'], [22, 'right'], [20, 'left'], [30, 'up_right'], [14, 'down_right'], [28, 'up_left'], [12, 'down_left']]]")
    assert(str(y[22]) == "['empty', [[30, 'up'], [14, 'down'], [23, 'right'], [21, 'left'], [31, 'up_right'], [15, 'down_right'], [29, 'up_left'], [13, 'down_left']]]")
    assert(str(y[23]) == "['empty', [[31, 'up'], [15, 'down'], [24, 'right'], [22, 'left'], [32, 'up_right'], [16, 'down_right'], [30, 'up_left'], [14, 'down_left']]]")
    assert(str(y[24]) == "['empty', [[32, 'up'], [16, 'down'], [23, 'left'], [31, 'up_left'], [15, 'down_left']]]")
    assert(str(y[25]) == "['empty', [[33, 'up'], [17, 'down'], [26, 'right'], [34, 'up_right'], [18, 'down_right']]]")
    assert(str(y[26]) == "['empty', [[34, 'up'], [18, 'down'], [27, 'right'], [25, 'left'], [35, 'up_right'], [19, 'down_right'], [33, 'up_left'], [17, 'down_left']]]")
    assert(str(y[27]) == "['empty', [[35, 'up'], [19, 'down'], [28, 'right'], [26, 'left'], [36, 'up_right'], [20, 'down_right'], [34, 'up_left'], [18, 'down_left']]]")
    assert(str(y[28]) == "['empty', [[36, 'up'], [20, 'down'], [29, 'right'], [27, 'left'], [37, 'up_right'], [21, 'down_right'], [35, 'up_left'], [19, 'down_left']]]")
    assert(str(y[29]) == "['empty', [[37, 'up'], [21, 'down'], [30, 'right'], [28, 'left'], [38, 'up_right'], [22, 'down_right'], [36, 'up_left'], [20, 'down_left']]]")
    assert(str(y[30]) == "['empty', [[38, 'up'], [22, 'down'], [31, 'right'], [29, 'left'], [39, 'up_right'], [23, 'down_right'], [37, 'up_left'], [21, 'down_left']]]")
    assert(str(y[31]) == "['empty', [[39, 'up'], [23, 'down'], [32, 'right'], [30, 'left'], [40, 'up_right'], [24, 'down_right'], [38, 'up_left'], [22, 'down_left']]]")
    assert(str(y[32]) == "['empty', [[40, 'up'], [24, 'down'], [31, 'left'], [39, 'up_left'], [23, 'down_left']]]")
    assert(str(y[33]) == "['empty', [[41, 'up'], [25, 'down'], [34, 'right'], [42, 'up_right'], [26, 'down_right']]]")
    assert(str(y[34]) == "['empty', [[42, 'up'], [26, 'down'], [35, 'right'], [33, 'left'], [43, 'up_right'], [27, 'down_right'], [41, 'up_left'], [25, 'down_left']]]")
    assert(str(y[35]) == "['empty', [[43, 'up'], [27, 'down'], [36, 'right'], [34, 'left'], [44, 'up_right'], [28, 'down_right'], [42, 'up_left'], [26, 'down_left']]]")
    assert(str(y[36]) == "['empty', [[44, 'up'], [28, 'down'], [37, 'right'], [35, 'left'], [45, 'up_right'], [29, 'down_right'], [43, 'up_left'], [27, 'down_left']]]")
    assert(str(y[37]) == "['empty', [[45, 'up'], [29, 'down'], [38, 'right'], [36, 'left'], [46, 'up_right'], [30, 'down_right'], [44, 'up_left'], [28, 'down_left']]]")
    assert(str(y[38]) == "['empty', [[46, 'up'], [30, 'down'], [39, 'right'], [37, 'left'], [47, 'up_right'], [31, 'down_right'], [45, 'up_left'], [29, 'down_left']]]")
    assert(str(y[39]) == "['empty', [[47, 'up'], [31, 'down'], [40, 'right'], [38, 'left'], [48, 'up_right'], [32, 'down_right'], [46, 'up_left'], [30, 'down_left']]]")
    assert(str(y[40]) == "['empty', [[48, 'up'], [32, 'down'], [39, 'left'], [47, 'up_left'], [31, 'down_left']]]")
    assert(str(y[41]) == "['empty', [[49, 'up'], [33, 'down'], [42, 'right'], [50, 'up_right'], [34, 'down_right']]]")
    assert(str(y[42]) == "['empty', [[50, 'up'], [34, 'down'], [43, 'right'], [41, 'left'], [51, 'up_right'], [35, 'down_right'], [49, 'up_left'], [33, 'down_left']]]")
    assert(str(y[43]) == "['empty', [[51, 'up'], [35, 'down'], [44, 'right'], [42, 'left'], [52, 'up_right'], [36, 'down_right'], [50, 'up_left'], [34, 'down_left']]]")
    assert(str(y[44]) == "['empty', [[52, 'up'], [36, 'down'], [45, 'right'], [43, 'left'], [53, 'up_right'], [37, 'down_right'], [51, 'up_left'], [35, 'down_left']]]")
    assert(str(y[45]) == "['empty', [[53, 'up'], [37, 'down'], [46, 'right'], [44, 'left'], [54, 'up_right'], [38, 'down_right'], [52, 'up_left'], [36, 'down_left']]]")
    assert(str(y[46]) == "['empty', [[54, 'up'], [38, 'down'], [47, 'right'], [45, 'left'], [55, 'up_right'], [39, 'down_right'], [53, 'up_left'], [37, 'down_left']]]")
    assert(str(y[47]) == "['empty', [[55, 'up'], [39, 'down'], [48, 'right'], [46, 'left'], [56, 'up_right'], [40, 'down_right'], [54, 'up_left'], [38, 'down_left']]]")
    assert(str(y[48]) == "['empty', [[56, 'up'], [40, 'down'], [47, 'left'], [55, 'up_left'], [39, 'down_left']]]")
    assert(str(y[49]) == "['empty', [[57, 'up'], [41, 'down'], [50, 'right'], [58, 'up_right'], [42, 'down_right']]]")
    assert(str(y[50]) == "['empty', [[58, 'up'], [42, 'down'], [51, 'right'], [49, 'left'], [59, 'up_right'], [43, 'down_right'], [57, 'up_left'], [41, 'down_left']]]")
    assert(str(y[51]) == "['empty', [[59, 'up'], [43, 'down'], [52, 'right'], [50, 'left'], [60, 'up_right'], [44, 'down_right'], [58, 'up_left'], [42, 'down_left']]]")
    assert(str(y[52]) == "['empty', [[60, 'up'], [44, 'down'], [53, 'right'], [51, 'left'], [61, 'up_right'], [45, 'down_right'], [59, 'up_left'], [43, 'down_left']]]")
    assert(str(y[53]) == "['empty', [[61, 'up'], [45, 'down'], [54, 'right'], [52, 'left'], [62, 'up_right'], [46, 'down_right'], [60, 'up_left'], [44, 'down_left']]]")
    assert(str(y[54]) == "['empty', [[62, 'up'], [46, 'down'], [55, 'right'], [53, 'left'], [63, 'up_right'], [47, 'down_right'], [61, 'up_left'], [45, 'down_left']]]")
    assert(str(y[55]) == "['empty', [[63, 'up'], [47, 'down'], [56, 'right'], [54, 'left'], [64, 'up_right'], [48, 'down_right'], [62, 'up_left'], [46, 'down_left']]]")
    assert(str(y[56]) == "['empty', [[64, 'up'], [48, 'down'], [55, 'left'], [63, 'up_left'], [47, 'down_left']]]")
    assert(str(y[57]) == "['empty', [[49, 'down'], [58, 'right'], [50, 'down_right']]]")
    assert(str(y[58]) == "['empty', [[50, 'down'], [59, 'right'], [57, 'left'], [51, 'down_right'], [49, 'down_left']]]")
    assert(str(y[59]) == "['empty', [[51, 'down'], [60, 'right'], [58, 'left'], [52, 'down_right'], [50, 'down_left']]]")
    assert(str(y[60]) == "['empty', [[52, 'down'], [61, 'right'], [59, 'left'], [53, 'down_right'], [51, 'down_left']]]")
    assert(str(y[61]) == "['empty', [[53, 'down'], [62, 'right'], [60, 'left'], [54, 'down_right'], [52, 'down_left']]]")
    assert(str(y[62]) == "['empty', [[54, 'down'], [63, 'right'], [61, 'left'], [55, 'down_right'], [53, 'down_left']]]")
    assert(str(y[63]) == "['empty', [[55, 'down'], [64, 'right'], [62, 'left'], [56, 'down_right'], [54, 'down_left']]]")
    assert(str(y[64]) == "['empty', [[56, 'down'], [63, 'left'], [55, 'down_left']]]")


def test_place_start_tile():
    x = Cells(8)
    y = x.dict
    x.place_start_tile(4, 3, "black")
    assert(x.tiles_placed == 1)
    cell = y[36]
    assert(cell.tile == 'black')
    x.place_start_tile(4, 4, "white")
    assert(x.tiles_placed == 2)
    cell = y[37]
    assert(cell.tile == 'white')
    x.place_start_tile(3, 4, "black")
    assert(x.tiles_placed == 3)
    cell = y[29]
    assert(cell.tile == 'black')
    x.place_start_tile(3, 3, "white")
    assert(x.tiles_placed == 4)
    cell = y[28]
    assert(cell.tile == 'white')


def test_place_tile():
    x = Cells(6)
    x.place_start_tile(3, 2, "black")
    x.place_start_tile(3, 3, "white")
    x.place_start_tile(2, 3, "black")
    x.place_start_tile(2, 2, "white")
    assert(x.place_tile(1, 2, "black") == {9, 15})
    x.place_tile(1, 2, "black")
    assert(x.place_tile(1, 1, "white") == {8, 15})


def test_get_key():
    x = Cells(8)
    assert(x.get_key(4, 3) == 36)
    assert(x.get_key(4, 4) == 37)
    assert(x.get_key(3, 4) == 29)
    assert(x.get_key(3, 3) == 28)


def test_game_state():
    x = Cells(6)
    x.place_start_tile(2, 3, "black")
    x.place_start_tile(3, 3, "white")
    x.place_start_tile(3, 2, "black")
    x.place_start_tile(2, 2, "white")
    assert(x.game_state("white") == "black")
    assert(x.game_state("black") == "white")
    y = x.dict[15]
    z = x.dict[22]
    y.add_tile("black")
    z.add_tile("black")
    assert(x.game_state("white") == "game_over")
    assert(x.game_state("black") == "game_over")
    z.add_tile("white")
    x.tiles_placed = 36
    assert(x.game_state("white") == "game_over")
    assert(x.game_state("black") == "game_over")


def test_validate_turn():
    x = Cells(6)
    x.place_start_tile(2, 3, "black")
    x.place_start_tile(3, 3, "white")
    x.place_start_tile(3, 2, "black")
    x.place_start_tile(2, 2, "white")
    assert(x.validate_turn("black") is True)
    assert(x.validate_turn("white") is True)
    y = x.dict[15]
    z = x.dict[22]
    y.add_tile("black")
    z.add_tile("black")
    assert(x.validate_turn("black") is False)
    assert(x.validate_turn("white") is False)


def test_valid_moves():
    x = Cells(6)
    x.place_start_tile(2, 3, "black")
    x.place_start_tile(3, 3, "white")
    x.place_start_tile(3, 2, "black")
    x.place_start_tile(2, 2, "white")
    assert(str(x.valid_moves("black")) == str([Valid_Move(10, 2, 'white', 0, [10, 16]), Valid_Move(17, 2, 'white', 6, [17, 16]), Valid_Move(27, 2, 'white', 4, [27, 21]), Valid_Move(20, 2, 'white', 2, [20, 21])]))


def test_validate_move():
    x = Cells(6)
    x.place_start_tile(2, 3, "black")
    x.place_start_tile(3, 3, "white")
    x.place_start_tile(3, 2, "black")
    x.place_start_tile(2, 2, "white")
    assert(str(x.validate_move("white", 9, 0)) ==
        str([Valid_Move(9, 2, "black", 0, [9, 15])])
        )
    assert(str(x.validate_move("white", 14, 2)) ==
        str([Valid_Move(14, 2, "black", 2, [14, 15])])
        )
    assert(x.validate_move("white", 8, 1) == [])
    assert(x.validate_move("white", 28, 0) == [])
    assert(str(x.validate_move("white", 23, 6)) ==
        str([Valid_Move(23, 2, "black", 6, [23, 22])])
        )
    assert(x.validate_move("white", 29, 5) == [])


def test_find_opp_color():
    x = Cells(6)
    assert(x.find_opp_color("black") == "white")
    assert(x.find_opp_color("white") == "black")
    assert(x.find_opp_color("empty") == "empty")
    assert(x.find_opp_color("Aunt Sherry" == "empty"))


def test_get_potentials():
    x = Cells(6)
    x.place_start_tile(2, 3, "black")
    x.place_start_tile(3, 3, "white")
    x.place_start_tile(3, 2, "black")
    x.place_start_tile(2, 2, "white")
    assert(x.get_potentials(15, "white") == [[9, 0], [14, 2], [8, 1]])
    assert(x.get_potentials(22, "white") == [[28, 4], [23, 6], [29, 5]])


def test_relative_cell_num():
    x = Cells(6)
    assert(x.relative_cell_num(14, 0) == 20)
    assert(x.relative_cell_num(14, 1) == 21)
    assert(x.relative_cell_num(14, 2) == 15)
    assert(x.relative_cell_num(14, 3) == 9)
    assert(x.relative_cell_num(14, 4) == 8)
    assert(x.relative_cell_num(14, 5) == 7)
    assert(x.relative_cell_num(14, 6) == 13)
    assert(x.relative_cell_num(14, 7) == 19)


def test_computer_move():
    x = Cells(6)
    x.place_start_tile(2, 3, "black")
    x.place_start_tile(3, 3, "white")
    x.place_start_tile(3, 2, "black")
    x.place_start_tile(2, 2, "white")
    x.place_tile(1, 2, "black")
    assert(x.computer_move() == {8, 15})


def test_calculate_comp_num():
    x = Cells(6)
    x.place_start_tile(2, 3, "black")
    x.place_start_tile(3, 3, "white")
    x.place_start_tile(3, 2, "black")
    x.place_start_tile(2, 2, "white")
    x.place_tile(1, 3, "black")
    assert(x.calculate_comp_num(20) == 2)
    assert(x.calculate_comp_num(10) == 2)
    assert(x.calculate_comp_num(15) == 3)
    assert(x.calculate_comp_num(29) == -17)
    assert(x.calculate_comp_num(6) == 106)
    assert(x.calculate_comp_num(35) == -16)
    assert(x.calculate_comp_num(31) == 106)
