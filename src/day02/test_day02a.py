from day02.day02a import (
    Subset,
    biggest_subset,
    game_from_line,
    id_sum_possible_games,
    possible,
)


TESTDATA = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
EXAMPLE_LINE_1 = TESTDATA.split("\n")[0]


def test_game_from_line1():
    game = game_from_line(EXAMPLE_LINE_1)
    assert game.id == 1


def test_game_from_line2():
    game = game_from_line(EXAMPLE_LINE_1)
    assert len(game.subsets) == 3


def test_game_from_line3():
    game = game_from_line(EXAMPLE_LINE_1)
    assert game.subsets[1].blue == 6


def test_biggest_subset1():
    game = game_from_line(EXAMPLE_LINE_1)
    assert biggest_subset(game).blue == 6


def test_possible1():
    bag = Subset(red=12, green=13, blue=14)
    game = game_from_line(EXAMPLE_LINE_1)
    assert possible(game, bag)


def test_possible2():
    example_line_3 = TESTDATA.split("\n")[2]
    bag = Subset(red=12, green=13, blue=14)
    game = game_from_line(example_line_3)
    assert not possible(game, bag)


def test_id_sum_possible_games():
    bag = Subset(red=12, green=13, blue=14)
    assert id_sum_possible_games(TESTDATA, bag) == 8
