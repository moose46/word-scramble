# This is a sample Python script.

import re

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import fall2025

words = ["afterburner"]


def validateData(grid):
    for row in grid:
        if len(row) != 20:
            print(f"{row} {len(row)} is not 20 chars long, exiting!")
            exit(0)


def find3chars(word, grid):
    # loop through the word , one char at a time
    rownum = 0
    for row in grid:
        # print(f"Searching row {row}", end="  ")
        for letter in word:
            print(
                f"searching for {letter.upper()} in {row} {search_row_for_letter(letter, row, rownum)}"
            )
        rownum += 1


def search_row_for_word_lr(word, grid):
    rownum = 0
    # pattern = re.compile(r"{word.upper()}")
    for row in grid:
        matches = re.findall(word, row)
        rownum += 1
        if matches:
            print(f"ROW {rownum}: {row} {word} {matches}")


def search_row_for_word_rl(word, grid):
    rownum = 0
    for row in grid:
        matches = re.findall(word, row[::-1])
        rownum += 1
        if matches:
            print(f"ROW {rownum}: {row[::-1]} {word} {matches}")


def search_row_for_letter(letter, row, rownum):
    # returns a list of found letter positions
    # print(f"searching for {letter}", end='  ')
    letters_found = []
    for x in range(len(row) - 1):
        if letter.upper() == row[x]:
            # ADD ONE TO ROW AND LETTER NUMBER
            letters_found.append((rownum + 1, letter, x + 1))
    if not letters_found:
        row_reversed = row[::-1]
        for x in range(len(row_reversed) - 1):
            if letter.upper() == row_reversed[x]:
                # ADD ONE TO ROW AND LETTER NUMBER
                letters_found.append((rownum + 1, letter, x + 1))

    return letters_found


def search_row_for_word_right_diagonal(word, grid):
    # Start at row x=0, column y=0
    letters = ""
    for z in range(0, len(grid[0])):  # left row numbers 0,1,2,3 ...
        # print(f"z=({z},0)", end="")
        letters += grid[z][0]
        x = z - 1
        for y in range(1, (z - len(grid[0])) + len(grid[0]) + 1):
            # print(f"({x},{y})", end="")
            letters += grid[x][y]
            x -= 1
            matches = re.findall(word, letters)
            if matches:
                print(f"\n\nFound Match ({z},{y}) {matches}")

                return letters
    # ======================================================
    letters = ""
    # x = 0
    for z in range(0, 20):  # bottom column numbers
        # letters += grid[19][0]
        x = z
        for y in range(19, -1, -1):
            # print(f" z={z} x={x} y={y} {letters}", end="")
            letters += grid[x][y]
            x += 1
            # print(f"{grid[x][y]}", end="")
        print(f"-- {letters}")
        letters = ""
        print()
    exit()


def show(grid):
    # for row in grid:
    #     for letter in row:
    #         print(letter, end=" ")
    #     print()
    # y = 19
    # letter = 0
    letters_found = []
    print("==========================")
    # for bottom_column in range(0, 19):
    #     letters_found.clear()
    #     for x in range(19, 0, -1):
    #         for y in range(0, 19 - x + 1):
    #             letters_found.append((x, y, grid[x][y]))
    #             print(f"{grid[x][y]}", end=" ")
    #     print()
    # for x in range(19, 0, -1):
    letters_found.clear()
    for z in range(0, len(grid[0])):
        x = 19 - z
        while x >= 0:
            y = 0
            while y <= 19:
                letters_found.append((x, y, grid[x][y]))
                x -= 1
                y += 1
            letters_found.clear()


def test_grid_coordinates(grid):
    y = 0
    x = 0
    z = 0
    # upper left to lower left
    for z in range(0, len(grid[0])):
        x_loop = z
        while x < x_loop:
            y = 0
            y_loop = len(grid) - x
            while y < y_loop:
                try:
                    print(grid[x][y], end="")
                except IndexError as e:
                    print(f"\nx={x}, y={y}, z={z} {e}")
                    exit()
                y += 1
                x += 1
            print()

        x = z

    exit()


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    validateData(fall2025.words2025)
    # find3chars("int", fall2025.words2025)
    words_fall2025 = [
        "AFTERBURN",
        "BATMAN",
        "INTERCEPTOR",
        "FLIGHTENGINEER",
        "FOKKERTRIPLANE",
        "GROUND SUPPORT",
        "MONOPLANE",
        "PURPLEHEART",
        "SHOOTINGSTAR",
        "SPADVII",
        "STRATOTANKER",
        "TAYNINHVILLAGE",
        "TESTPILOT",
        "TURBINE",
        "WILDWEASEL",
        "DEON",  # REVERSE TEST
        "NOED",  # REVERSE TEST
    ]
    test_grid_coordinates(fall2025.words2025)

    show(fall2025.words2025)
    exit()
    for word in words_fall2025:
        search_row_for_word_lr(word, fall2025.words2025)
        search_row_for_word_rl(word, fall2025.words2025)
        search_row_for_word_right_diagonal(word, fall2025.words2025)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
