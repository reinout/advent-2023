import pathlib


def map_value(value: int, line: str) -> int | None:
    parts = line.split()
    (destination, source, range_length) = [int(part) for part in parts]
    if value < source or value > source + range_length - 1:
        return
    increase = destination - source
    return value + increase


def find_seeds(text: str) -> list[int]:
    for line in text.split("\n"):
        if "seeds:" in line:
            line = line.lstrip("seeds:").strip()
            return [int(seed) for seed in line.split()]


def parse_and_run(text) -> int:
    seeds = find_seeds(text)
    locations: list[int] = []

    for seed in seeds:
        print(f"Seed: {seed}")
        current_value = seed
        current_map = ""
        for line in text.split("\n"):
            if "map:" in line:
                current_map = line
                continue
            if not current_map:
                continue
            if not line.strip():
                continue
            # Regular mapping line, so try to map the value.
            possible_new_value = map_value(current_value, line)
            if possible_new_value:
                current_value = possible_new_value
                print(f"{current_map} mapped to {current_value}")
                current_map = ""
        # Last value is the location, store it.
        locations.append(current_value)
    return min(locations)


if __name__ == "__main__":
    source = pathlib.Path("src/day05/input.txt")
    contents = source.read_text()
    print(parse_and_run(contents))
