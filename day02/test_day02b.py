from day02.day02a import game_from_line
from day02.day02b import power, smallest_necessary_bag, total_power
from day02.test_day02a import EXAMPLE_LINE_1, TESTDATA


def test_smallest_necessary_bag1():
    game = game_from_line(EXAMPLE_LINE_1)
    assert smallest_necessary_bag(game).red == 4


def test_power1():
    game = game_from_line(EXAMPLE_LINE_1)
    bag = smallest_necessary_bag(game)
    assert power(bag) == 48


def test_total_power1():
    assert total_power(TESTDATA) == 2286
