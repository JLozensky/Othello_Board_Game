from cell import Cell


def test_add_tile():

    cell = Cell()
    cell.add_tile("black")
    assert(cell.tile == "black")
    cell.add_tile("white")
    assert(cell.tile == "white")
    cell.add_tile("empty")
    assert(cell.tile == "empty")
