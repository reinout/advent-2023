from dataclasses import dataclass


@dataclass
class Segment:
    """Line number and character number from/to, 0-based

    The 'end' is inclusive, btw.

    """

    line: int
    start: int
    end: int


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
    top = segment.line
    bottom = segment.line + 1
    left = segment.start
    right = segment.end + 1
    return Box(top=top, bottom=bottom, left=left, right=right)


def box_with_padding(box: Box) -> Box:
    """Return box, padded on all sides by one character"""
    return Box(
        top=box.top - 1, bottom=box.bottom + 1, left=box.left - 1, right=box.right + 1
    )
