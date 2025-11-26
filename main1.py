import re
from pkgutil import resolve_name

import summer2025
import pandas as pd

WORD = "RADOME"


def word_search_rows(word, grid):
    for x, row_of_letters in enumerate(grid):
        match = re.findall(word["word"], row_of_letters)
        match_reversed = re.findall(word["word"][::-1], row_of_letters)
        if match:
            print(f"Row {word["word"]}: ({x}, {row_of_letters.index(word['word'])})")
            word["found"] = True
        if match_reversed:
            print(
                f"Row[::-1] {word["word"]}: ({x}, {len(row_of_letters) - row_of_letters[::-1].index(word['word']) -1})"
            )
            word["found"] = True


def word_search_columns(word, grid):
    grid_to_columns = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    column_of_letters = ""
    # transform grid columns into grid rows
    for x, row_of_letters in enumerate(grid):
        for y in range(len(row_of_letters)):
            grid_to_columns[y][x] = grid[x][y]
            # column_of_letters += grid[x][y]
    for x, column_of_letters in enumerate(grid_to_columns):
        # use .join to convert list of letters to a string of letters
        match = re.findall(word["word"], "".join(column_of_letters))
        match_reversed = re.findall(word["word"], "".join(column_of_letters[::-1]))
        if match:
            print(
                f"Column {word["word"]}: ({"".join(column_of_letters).index(word['word'])},{x})"
            )
        if match_reversed:
            print(
                f"Column[::-1] {word["word"]}: ({ len(column_of_letters) - "".join(column_of_letters)[::-1].index(word['word']) - 1},{x})"
            )
        column_of_letters = ""


def word_search_bottom_left_up_diagonal(word, grid):
    grid_to_columns = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    found_letters = ""
    found_rows = []
    for loop_cnt in range(0, len(grid[0])):
        y = loop_cnt
        x = 19

        while y >= 0:
            # print(f"({x},{y}) = {grid[x][y]}")
            found_letters += grid[x][y]
            x -= 1
            y -= 1
        print(found_letters)
        found_rows.append(found_letters)
        found_letters = ""

    exit()

    # for x, row in enumerate(grid):
    #     for y, column in enumerate(row):
    #         print(f"({y} - {x} {y - x}) ")
    exit()


def list_to_diagonal_string(strings):
    """
    Convert a list of strings into a diagonal multi-line string.
    Each subsequent string is indented one space more than the previous.
    """
    # Validate input type
    if not isinstance(strings, list):
        raise TypeError("Input must be a list.")

    # Ensure all elements are strings
    safe_strings = []
    for i, s in enumerate(strings):
        if not isinstance(s, str):
            s = str(s)  # Convert non-string to string
        safe_strings.append(s)

    # Build diagonal string
    diagonal_lines = []
    for i, word in enumerate(safe_strings):
        diagonal_lines.append(" " * i + word)

    return "\n".join(diagonal_lines)


summer2025words = [
    {"word": "BOCKSCAR", "found": False},
    {"word": "ENOLAGAY", "found": False},
    {"word": "SENTINEL", "found": False},
    {"word": "OSCILLOSCOPE", "found": False},
    {"word": "TEXASTOWERS", "found": False},
    {"word": "BEETLEBAILEY", "found": False},
    {"word": "GOLIATH", "found": False},
    {"word": "TYPHOONZOLA", "found": False},
    {"word": "TURBULENCE", "found": False},
    {"word": "WARSAWPACT", "found": False},
    {"word": "BUSHMASTERS", "found": False},
    {"word": "VICTORALERT", "found": False},
    {"word": "BIGSKYTHEORY", "found": False},
    {"word": "KAMIKAZE", "found": False},
    {"word": "RADOME", "found": False},
    {"word": "BALQP", "found": False},
    {"word": "PQLAB", "found": False},
]
if __name__ == "__main__":

    for find_words in summer2025words:
        word_search_bottom_left_up_diagonal(find_words, summer2025.words_summer2025)
    exit()
    for row in summer2025words:
        word_search_rows(row, summer2025.words_summer2025)
    for w in summer2025words:
        word_search_columns(w, summer2025.words_summer2025)
["Hello", "World", "Python", "Rocks!"]
