import pathlib

NUMBERS = "0123456789"
MAPPING = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def find_first(line: str) -> int:
    for number in NUMBERS:
        if line.startswith(number):
            return int(number)
    for word in MAPPING:
        if line.startswith(word):
            return MAPPING[word]
    return find_first(line[1:])


def find_last(line: str) -> int:
    for number in NUMBERS:
        if line.endswith(number):
            return int(number)
    for word in MAPPING:
        if line.endswith(word):
            return MAPPING[word]
    return find_last(line[:-1])


def line_solution(line: str) -> int:
    return find_first(line) * 10 + find_last(line)


def solution(content: str) -> int:
    lines = [line for line in content.split("\n") if line]
    return sum([line_solution(line) for line in lines])


if __name__ == "__main__":
    source = pathlib.Path("src/day01/input.txt")
    contents = source.read_text()
    print(solution(contents))
