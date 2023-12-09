from day03.day03a import (
    Box,
    Segment,
    box_with_padding,
    characters_in_box,
    find_segments,
    is_valid_partnumber,
    segment_to_box,
    sum_partnumbers,
    text_to_padded_matrix,
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


MORE_TESTDATA = """\
12.......*..
+.........34
.......-12..
..78........
..*....60...
78.........9
.5.....23..$
8...90*12...
............
2.2......12.
.*.........*
1.1..503+.56
"""


def test_text_to_padded_lines1():
    matrix = text_to_padded_matrix(TESTDATA)
    assert len(matrix.lines) == 1 + 10 + 1


def test_segment_to_box1():
    segment = Segment(line_number=2, start=1, end=3, value=123)
    box = segment_to_box(segment)
    assert box.top == 2
    assert box.bottom == 3
    assert box.left == 1
    assert box.right == 4


def test_padded_box1():
    segment = Segment(line_number=2, start=1, end=3, value=123)
    box = segment_to_box(segment)
    padded_box = box_with_padding(box)
    assert padded_box.top == 1
    assert padded_box.bottom == 4
    assert padded_box.left == 0
    assert padded_box.right == 5


def test_find_segments1():
    matrix = text_to_padded_matrix(TESTDATA)
    segments = find_segments(matrix)
    assert len(segments) == 10


def test_find_segments2():
    matrix = text_to_padded_matrix(TESTDATA)
    segments = find_segments(matrix)
    last_one = segments[-1]
    assert last_one.value == 598
    # For the tests below: remember there's 1 cell of padding everywhere!
    assert last_one.line_number == 10
    assert last_one.start == 6
    assert last_one.end == 8  # inclusive, btw


def test_characters_in_box():
    matrix = text_to_padded_matrix(TESTDATA)
    box = Box(top=1, bottom=4, left=1, right=4)
    result = characters_in_box(matrix, box)
    assert result == "467.....3"


def test_is_valid_partnumber1():
    matrix = text_to_padded_matrix(TESTDATA)
    segments = find_segments(matrix)
    valid_one = segments[0]
    assert is_valid_partnumber(matrix, valid_one)


def test_is_valid_partnumber2():
    matrix = text_to_padded_matrix(TESTDATA)
    segments = find_segments(matrix)
    invalid_one = segments[1]
    assert not is_valid_partnumber(matrix, invalid_one)


def test_sum_partnumbers():
    matrix = text_to_padded_matrix(TESTDATA)
    assert sum_partnumbers(matrix) == 4361


def test_sum_partnumbers2():
    matrix = text_to_padded_matrix(MORE_TESTDATA)
    assert sum_partnumbers(matrix) == 925
