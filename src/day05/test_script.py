import pytest
from src.day05.script import find_seeds, map_value, parse_and_run


TESTDATA = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


@pytest.mark.parametrize(
    "value, expected", [[98, 50], [99, 51], [100, None], [13, None]]
)
def test_map_value(value, expected):
    assert map_value(value, "50 98 2") == expected


def test_find_seeds():
    assert find_seeds(TESTDATA) == [79, 14, 55, 13]


def test_parse_and_run():
    assert parse_and_run(TESTDATA) == 35
