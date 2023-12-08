def text_to_padded_lines(text: str) -> list[str]:
    """Return text splitted into lines, but padded on all sides with dots"""
    lines = [line for line in text.split("\n") if line.strip()]
    len_line = len(lines[0])
    dots = "." * len_line
    return ["." + line + "." for line in [dots] + lines + [dots]]
