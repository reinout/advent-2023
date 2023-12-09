import pathlib
from dataclasses import dataclass
from day03.day03a import (
    Matrix,
    Segment,
    box_with_padding,
    characters_in_box,
    find_segments,
    segment_to_box,
    text_to_padded_matrix,
)

GEAR = "*"


@dataclass(frozen=True)
class Gear:
    line_number: int
    position: int


def is_relevant_partnumber(matrix: Matrix, segment: Segment) -> bool:
    """Return partnumber only if it has a gear next to it

    Similar to is_valid_partnumber() from part 1, but then it only looks at *.

    """
    box = box_with_padding(segment_to_box(segment))
    for character in characters_in_box(matrix, box):
        if character in GEAR:
            return True
    return False


def find_gears(matrix: Matrix) -> list[Gear]:
    gears: list[Gear] = []
    for line_number, line in enumerate(matrix.lines):
        for position, character in enumerate(line):
            if character == GEAR:
                gears.append(Gear(line_number=line_number, position=position))
    return gears


def gear_next_to_segment(gear: Gear, segment: Segment) -> bool:
    box = box_with_padding(segment_to_box(segment))
    if gear.line_number < box.top:
        return False
    if (gear.line_number + 1) > box.bottom:
        return False
    if gear.position < box.left:
        return False
    if (gear.position + 1) > box.right:
        return False
    return True


def neighbouring_segments_per_gear(matrix: Matrix) -> dict[Gear, list[Segment]]:
    result: dict[Gear, list[Segment]] = {}
    segments = find_segments(matrix)
    gears = find_gears(matrix)
    for gear in gears:
        matches: list[Segment] = []
        for segment in segments:
            if gear_next_to_segment(gear, segment):
                matches.append(segment)
        result[gear] = matches
    return result


def gear_ratios(matrix: Matrix) -> list[int]:
    ratios: list[int] = []
    for neighbouring_segments in neighbouring_segments_per_gear(matrix).values():
        if len(neighbouring_segments) == 2:
            values = [segment.value for segment in neighbouring_segments]
            ratios.append(values[0] * values[1])
    return ratios


if __name__ == "__main__":
    source = pathlib.Path("src/day03/input.txt")
    contents = source.read_text()
    matrix = text_to_padded_matrix(contents)
    print(sum(gear_ratios(matrix)))
