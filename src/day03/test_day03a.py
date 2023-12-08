from day03.day03a import Segment, box_with_padding, segment_to_box, text_to_padded_matrix


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
    matrix = text_to_padded_matrix(TESTDATA)
    assert len(matrix.lines) == 1 + 10 + 1


def test_segment_to_box1():
    segment = Segment(line=2, start=1, end=3)
    box = segment_to_box(segment)
    assert box.top == 2
    assert box.bottom == 3
    assert box.left == 1
    assert box.right == 4

def test_padded_box1():
    segment = Segment(line=2, start=1, end=3)
    box = segment_to_box(segment)
    padded_box = box_with_padding(box)
    assert padded_box.top == 1
    assert padded_box.bottom == 4
    assert padded_box.left == 0
    assert padded_box.right == 5
