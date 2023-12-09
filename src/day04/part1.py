import pathlib


class Card:
    line: str
    id: int
    winning_numbers: set[int]
    numbers_i_have: set[int]

    def __init__(self, line):
        self.line = line
        self.parse()

    def parse(self):
        full_name, numbers = self.line.split(":")
        self.id = int(full_name.split()[-1])
        winning_str, have_str = numbers.split("|")
        self.winning_numbers = set(
            [int(number) for number in winning_str.strip().split()]
        )
        self.numbers_i_have = set([int(number) for number in have_str.strip().split()])

    @property
    def matches(self) -> set[int]:
        return self.winning_numbers & self.numbers_i_have

    @property
    def points(self) -> int:
        if not self.matches:
            return 0
        return 2 ** (len(self.matches) - 1)

    @property
    def extra_ids(self) -> list[int]:
        """Part 2: return follow-up IDs the number of matches this gains us"""
        return [(self.id + 1 + i) for i in range(len(self.matches))]


def text_to_cards(text: str) -> list[Card]:
    lines = [line for line in text.split("\n") if line.strip()]
    cards = [Card(line) for line in lines]
    return cards


def total_points(cards: list[Card]) -> int:
    all_points = [card.points for card in cards]
    return sum(all_points)


def number_gained(original_cards: list[Card]) -> int:
    card_info = {card.id: card for card in original_cards}
    number_of_cards = {card.id: 1 for card in original_cards}
    known_ids = [card.id for card in original_cards]
    for card in original_cards:
        our_number = number_of_cards[card.id]
        for id in card.extra_ids:
            if id not in known_ids:
                continue
            number_of_cards[id] += our_number
    return sum(number_of_cards.values())


if __name__ == "__main__":
    source = pathlib.Path("src/day04/input.txt")
    contents = source.read_text()
    cards = text_to_cards(contents)
    print("Part 1")
    print(total_points(cards))
    print("Part 2")
    print(number_gained(cards))
