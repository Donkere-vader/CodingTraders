""" Have the terminal output colors here """

__COLORS = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

__EFFECTS = {
    "bold": 1,
    "faint": 2,
    "italic": 3,
    "underline": 4,
    "slowblink": 5,
    "rapidblink": 6,
    "conceal": 8,
    "crossedout": 9,
    "fraktur": 20,
    "doubleunderline": 21
}

COLOR_RESET = "\u001b[0;0;0m"


def __get_color_code(color: str) -> int:
    """Translates a color in string like 'bright red' to a integer of
    this table: https://i.stack.imgur.com/9UVnC.png
    """
    code = 0
    color = __clear_string(color)
    if 'bright' in color:
        color = color.replace('bright', '')
        code += 60

    code += __COLORS.index(color)

    return code


def __clear_string(string: str) -> str:
    return string.lower().strip().replace(" ", "").replace("-", "")


def color(fg="", bg="", effects=[]) -> str:
    """For generating a unicode escape sequence for the colors in the terminal/ console """
    codes = []

    # foreground color
    if fg:
        fg_code = __get_color_code(fg) + 30
        codes.append(fg_code)

    # background color
    if bg:
        bg_code = __get_color_code(bg) + 40
        codes.append(bg_code)

    for effect in effects:
        if __clear_string(effect) in __EFFECTS:
            codes.append(__EFFECTS[__clear_string(effect)])

    codes = [str(code) for code in codes]
    return f"\u001b[{';'.join(codes)}m"
