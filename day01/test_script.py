from day01 import script

TESTDATA = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""


def test_line_solution2():
    assert script.line_solution("1abc2") == 12


def test_line_solution1():
    assert script.line_solution("treb7uchet") == 77


def test_solution():
    assert script.solution(TESTDATA) == 142
