from src.day03.day03a import find_segments, text_to_padded_matrix
from src.day03.day03b import (
    find_gears,
    gear_next_to_segment,
    is_relevant_partnumber,
    neighbouring_segments_per_gear,
    gear_ratios,
)

TESTDATA = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def test_is_relevant_partnumber():
    matrix = text_to_padded_matrix(TESTDATA)
    segments = find_segments(matrix)
    valid_one = segments[0]
    assert is_relevant_partnumber(matrix, valid_one)


def test_is_relevant_partnumber2():
    matrix = text_to_padded_matrix(TESTDATA)
    segments = find_segments(matrix)
    invalid_one = segments[1]
    assert not is_relevant_partnumber(matrix, invalid_one)


def test_find_gears1():
    matrix = text_to_padded_matrix(TESTDATA)
    assert len(find_gears(matrix)) == 3


def test_find_gears2():
    matrix = text_to_padded_matrix(TESTDATA)
    assert find_gears(matrix)[0].line_number == 2
    assert find_gears(matrix)[0].position == 4


def test_gear_next_to_segment1():
    matrix = text_to_padded_matrix(TESTDATA)
    segment = find_segments(matrix)[0]
    gear = find_gears(matrix)[0]
    assert gear_next_to_segment(gear, segment)


def test_gear_next_to_segment2():
    matrix = text_to_padded_matrix(TESTDATA)
    segment = find_segments(matrix)[1]
    gear = find_gears(matrix)[0]
    assert not gear_next_to_segment(gear, segment)


def test_neighbouring_segments_per_gear1():
    matrix = text_to_padded_matrix(TESTDATA)
    result = neighbouring_segments_per_gear(matrix)
    first_gear = find_gears(matrix)[0]
    assert len(result[first_gear]) == 2


def test_sum_gear_ratios1():
    matrix = text_to_padded_matrix(TESTDATA)
    assert len(gear_ratios(matrix)) == 2


def test_sum_gear_ratios2():
    matrix = text_to_padded_matrix(TESTDATA)
    assert 16345 in gear_ratios(matrix)

    # {gear: [matching segments]} en dan welke heeft er twee
