from day04.part1 import Card, number_gained, text_to_cards, total_points

TESTDATA = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

SAMPLE_LINE = "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"


def test_card_parse1():
    card = Card(SAMPLE_LINE)
    assert card.id == 3


def test_card_parse2():
    card = Card(SAMPLE_LINE)
    assert 53 in card.winning_numbers


def test_card_parse3():
    card = Card(SAMPLE_LINE)
    assert len(card.numbers_i_have) == 8


def test_card_matches1():
    card = Card(SAMPLE_LINE)
    assert len(card.matches) == 2


def test_card_points1():
    card = Card(SAMPLE_LINE)
    assert card.points == 2


def test_integration():
    cards = text_to_cards(TESTDATA)
    assert total_points(cards) == 13


# Part 2 below


def test_card_extra_ids():
    card = Card(SAMPLE_LINE)
    # 2 matching numbers
    assert card.extra_ids == [4, 5]


def test_handle_stack():
    cards = text_to_cards(TESTDATA)
    assert  number_gained(cards) == 30
