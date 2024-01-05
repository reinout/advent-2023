import pathlib


class Slice:
    original_start: int
    original_end: int
    modifiers: list[int]

    def __init__(self, start: int, end: int, modifiers: list[int] | None = None):
        self.original_start = start
        self.original_end = end
        if not modifiers:
            self.modifiers = []
        else:
            self.modifiers = modifiers

    @property
    def start(self):
        return sum([self.original_start] + self.modifiers)

    @property
    def end(self):
        return sum([self.original_end] + self.modifiers)

    def __repr__(self) -> str:
        return f"Slice {self.start}-{self.end}"

    # def apply_mapping
    #     split on start/end, return new slices


def map_value(value: int, line: str) -> int | None:
    parts = line.split()
    (destination, source, range_length) = [int(part) for part in parts]
    if value < source or value > source + range_length - 1:
        return
    increase = destination - source
    return value + increase


def find_seed_slices(text: str) -> list[int]:
    slices = []
    for line in text.split("\n"):
        if "seeds:" in line:
            line = line.lstrip("seeds:").strip()
            instructions = [int(part) for part in line.split()]
            for i in range(len(instructions) // 2):
                start = instructions[2 * i]
                length = instructions[2 * i + 1]
                slices.append(Slice(start, start + length))
    return slices


def parse_and_run(text) -> int:
    slices_to_handle: list[Slice] = find_seed_slices(text)
    handled_slices: list[Slice] = []

    current_map: str = ""
    for line in text.split("\n"):
        if "map:" in line:
            current_map = line
            continue
        if not current_map:
            continue
        if not line.strip():
            # reset handled_slices, add them to slices_to_handle
            continue
        # Regular mapping line, so try to map the value.
        for slice in slices_to_handle:
            # possible_new_value = map_value(current_value, line)
            # if possible_new_value:
            #     current_value = possible_new_value
            #     print(f"{current_map} mapped to {current_value}")
            #     current_map = ""


if __name__ == "__main__":
    source = pathlib.Path("src/day05/input.txt")
    contents = source.read_text()
    # print(parse_and_run(contents))
    print(find_seed_slices(contents))
