from dataclasses import dataclass, field
import pathlib


@dataclass
class Subset:
    blue: int = 0
    red: int = 0
    green: int = 0


@dataclass
class Game:
    id: int
    subsets: list[Subset] = field(default_factory=list)


def game_from_line(line: str) -> Game:
    game_name_part, subsets_part = line.split(":")
    id = int(game_name_part.split()[-1])
    game = Game(id=id)
    subset_strings = subsets_part.split(";")
    for subset_string in subset_strings:
        color_strings = subset_string.split(",")
        subset = Subset()
        for color_string in color_strings:
            number, color = color_string.strip().split()
            setattr(subset, color, int(number))
        game.subsets.append(subset)
    return game


def biggest_subset(game: Game) -> Subset:
    """Return combined subset of the biggest numbers"""
    result = Subset()
    for color in ["blue", "red", "green"]:
        values = [getattr(subset, color) for subset in game.subsets]
        setattr(result, color, max(values))
    return result


def possible(game: Game, bag: Subset) -> bool:
    """Return if it is possible to grab subset from bag"""
    biggest = biggest_subset(game)
    for color in ["blue", "red", "green"]:
        if getattr(biggest, color) > getattr(bag, color):
            return False
    return True


def id_sum_possible_games(text: str, bag: Subset) -> int:
    lines = text.split("\n")
    games = [game_from_line(line) for line in lines if line.strip()]
    possible_game_ids = [game.id for game in games if possible(game, bag)]
    return sum(possible_game_ids)


if __name__ == "__main__":
    source = pathlib.Path("day02/input.txt")
    contents = source.read_text()
    bag = Subset(red=12, green=13, blue=14)
    print(id_sum_possible_games(contents, bag))
