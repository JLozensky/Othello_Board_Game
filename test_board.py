from board import Board


def test_getcenter():

    b = Board(4)
    assert(b.get_center(0, 0) == (63, 38))
    assert(b.get_center(1, 1) == (138, 113))
    assert(b.get_center(2, 7) == (213, 563))
    assert(b.get_center(7, 3) == (588, 263))
