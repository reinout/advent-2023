import pathlib


def line_solution(line):
    numbers = [character for character in line if character in "0123456789"]
    first = numbers[0]
    last = numbers[-1]
    return int(first + last)


def solution(content):
    lines = [line for line in content.split("\n") if line]
    return sum([line_solution(line) for line in lines])


if __name__ == "__main__":
    source = pathlib.Path("day01/input.txt")
    contents = source.read_text()
    print(solution(contents))
