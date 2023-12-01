from day01 import script2

TESTDATA = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def test_find_first1():
    assert script2.find_first("two1nine") == 2


def test_find_first2():
    assert script2.find_first("twotwo") == 2


def test_find_first3():
    assert script2.find_first("eightwothree") == 8


def test_find_last1():
    assert script2.find_last("two1nine") == 9


def test_find_last2():
    assert script2.find_last("twotwo") == 2


def test_find_last3():
    assert script2.find_last("eightwothree") == 3


def test_line_solution1():
    assert script2.line_solution("two1nine") == 29


def test_line_solution2():
    assert script2.line_solution("4nineeightseven2") == 42


def test_solution():
    assert script2.solution(TESTDATA) == 281
