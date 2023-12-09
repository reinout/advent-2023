from dataclasses import dataclass
import pathlib

NUMBERS = "0123456789"
SYMBOLS = "!@#$%^&*()_+/=-"


@dataclass
class Segment:
    """Line number and character number from/to, 0-based

    The 'end' is inclusive, btw.

    """

    line_number: int
    start: int
    end: int
    value: int


@dataclass
class Box:
    """Box coordinates around characters.

    Character 0 on line 0 has box coordinates 0,0 (top left) to 1,1 (bottom right).

    """

    left: int
    right: int
    top: int
    bottom: int


@dataclass
class Matrix:
    lines: list[str]


def text_to_padded_matrix(text: str) -> Matrix:
    """Return text splitted into lines, but padded on all sides with dots"""
    lines = [line for line in text.split("\n") if line.strip()]
    len_line = len(lines[0])
    dots = "." * len_line
    padded_lines = ["." + line + "." for line in [dots] + lines + [dots]]
    return Matrix(lines=padded_lines)


def segment_to_box(segment: Segment) -> Box:
    top = segment.line_number
    bottom = segment.line_number + 1
    left = segment.start
    right = segment.end + 1
    return Box(top=top, bottom=bottom, left=left, right=right)


def box_with_padding(box: Box) -> Box:
    """Return box, padded on all sides by one character"""
    return Box(
        top=box.top - 1, bottom=box.bottom + 1, left=box.left - 1, right=box.right + 1
    )


def find_segments(matrix: Matrix) -> list[Segment]:
    segments: list[Segment] = []
    for line_number, line in enumerate(matrix.lines):
        found = ""
        start = 0
        end = 0
        for position, character in enumerate(line):
            # Note: line always starts and ends with "."!
            if character in NUMBERS:
                if not found:
                    start = position
                found += character
                end = position
            else:
                if found:
                    # End the segment
                    segment = Segment(
                        line_number=line_number, start=start, end=end, value=int(found)
                    )
                    segments.append(segment)
                    found = ""
    return segments


def characters_in_box(matrix: Matrix, box: Box) -> str:
    result: str = ""
    for line_number, line in enumerate(matrix.lines):
        if line_number < box.top or line_number > (box.bottom - 1):
            continue
        for position, character in enumerate(line):
            if position < box.left or position > (box.right - 1):
                continue
            result += character
    return result


def is_valid_partnumber(matrix: Matrix, segment: Segment) -> bool:
    box = box_with_padding(segment_to_box(segment))
    for character in characters_in_box(matrix, box):
        if character in SYMBOLS:
            print(f"{segment.value}: {characters_in_box(matrix, box)}")
            return True
    return False


def sum_partnumbers(matrix: Matrix) -> int:
    segments = find_segments(matrix)
    valid_segments = [
        segment for segment in segments if is_valid_partnumber(matrix, segment)
    ]
    return sum([segment.value for segment in valid_segments])


def check_missing_symbols(matrix: Matrix):
    for line in matrix.lines:
        for character in line:
            if character not in ("." + NUMBERS + SYMBOLS):
                raise ValueError(f"Missing symbol: {character}")


if __name__ == "__main__":
    source = pathlib.Path("src/day03/input.txt")
    contents = source.read_text()
    matrix = text_to_padded_matrix(contents)
    print("\n".join(matrix.lines))
    check_missing_symbols(matrix)
    print(sum_partnumbers(matrix))
