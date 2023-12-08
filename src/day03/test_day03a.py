from day03.day03a import text_to_padded_lines


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


def test_text_to_padded_lines1():
    padded_lines = text_to_padded_lines(TESTDATA)
    assert len(padded_lines) == 1 + 10 + 1
