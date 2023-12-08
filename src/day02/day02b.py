from day02.day02a import Game, Subset, game_from_line
import pathlib


def smallest_necessary_bag(game: Game) -> Subset:
    """Return minimum subset of the biggest numbers"""
    bag = Subset()
    for color in ["blue", "red", "green"]:
        values = [getattr(subset, color) for subset in game.subsets]
        setattr(bag, color, max(values))
    return bag


def power(bag: Subset) -> int:
    return bag.blue * bag.red * bag.green


def total_power(text: str) -> int:
    lines = text.split("\n")
    games = [game_from_line(line) for line in lines if line.strip()]
    smallest_bags = [smallest_necessary_bag(game) for game in games]
    return sum([power(bag) for bag in smallest_bags])


if __name__ == "__main__":
    source = pathlib.Path("src/day02/input.txt")
    contents = source.read_text()
    print(total_power(contents))
