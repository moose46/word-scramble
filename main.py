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
    # then increment x by 1 and set y = 0 back to 0 and increment to x
    # start a new letter row
    rownum = 0
    gridxy = []
    gridrow = []
    letters = ""
    x = 0
    y = 0
    column_number = 0
    y_len = len(grid) - 1
    letters_found = []
    # letters_found.append(grid[x][y])
    # looking for (0,0) (0,1) (1,0) (0,2) (1,1) (2,0) (0,3) (1,2) (2,2) (3,1) (4,0)
    for x in range(0, len(grid[0])):  # count up accross
        for column_number in range(0, len(grid[0]) - (len(grid[0]) - x)):
            print(f"({x},{column_number})={grid[x][column_number]}")
            # column_number += 1
        # for y in range(0, len(grid)):
        # for y in range(0, x, -1):
        #     for x1 in range(y, x, -1):  # down
        #         letters += grid[x1][y]
        # letters_found.append(letters)
        # letters = ""

    gridrow.append(letters)
    print(f"left to right, down and accross {letters}")


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
    for word in words_fall2025:
        search_row_for_word_lr(word, fall2025.words2025)
        search_row_for_word_rl(word, fall2025.words2025)
        search_row_for_word_right_diagonal(word, fall2025.words2025)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
