# This is a sample Python script.

import re


# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import fall2025

words = ["afterburner"]


def validatedata(grid):
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


def search_word_by_row(word, grid):
    rownum = 0
    # pattern = re.compile(r"{word.upper()}")
    for row in grid:
        matches = re.findall(word, row)
        rownum += 1
        if matches:
            print(
                f"{"search_word_by_row":42} ({rownum:02},{row.index(word):02}) {matches}"
            )


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


def show(grid):
    letters_found = []
    print("==========================")
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


def bottom_left_up(grid, word):
    y = 0
    x = 0
    z = 0
    letters = ""
    letters_found = []
    # print(f"looking for {word}")
    # upper left to lower left
    for z in range(0, len(grid[0])):
        x_loop = z
        while x < x_loop:
            y = 0
            y_loop = len(grid) - x
            while y < y_loop:
                try:
                    letters += grid[x][y]
                    # letters_found.append(grid[x][y])
                    # print(grid[x][y], end="")
                except IndexError as e:
                    print(f"\nx={x}, y={y}, z={z} {e}")
                    exit()
                y += 1
                x += 1
            # print(letters)
            matches = re.findall(word, letters[::-1])
            if matches:
                x = letters.index(word[::-1]) + len(word) - 1
                print(
                    f"{"bottom_left_up [::-1]":42} ({x:02},{x + len(word):02}) {matches}"
                )
                return letters
            matches = re.findall(word, letters)
            if matches:
                # "XXXXXXTESTPILOT"
                # "TESTPILOTXXXXXX"
                x1 = letters.index(word)
                y1 = len(grid[0]) - letters[::-1].index(word[::-1]) - len(word)
                print(f"{"bottom_left_up":42} ({x1:02},{y1:02}) {matches}")
                return letters
            # print(f"{letters}")
            letters = ""
        # letters_found.clear()

        x = z
    row = 0
    column = 0


def search_word_left_to_right_and_down(grid, word):
    y = 0
    x = 0
    z = 0
    letters = ""
    letters_found = []
    for column in range(1, len(grid[0]) - 1):  # columns are accross
        column_loop = column
        for row in range(0, len(grid) - column):
            letters += grid[row][column_loop]
            column_loop += 1
        matches = re.findall(word, letters)
        if matches:
            x = letters.index(word)
            print(
                f"{"search_word_left_to_right_and_down":42} ({letters.index(word) + column:02},{x:02}) {matches}"
            )
        matches = re.findall(word, letters[::-1])
        if matches:
            print(
                f"{"search_word_left_to_right_and_down":42} Reverse Found Match (column={column_loop},row={row}) {matches}"
            )
        letters = ""
    # print(letters)


def search_word_by_column(grid, word):
    letters = ""
    for y in range(0, 19):
        for x in range(0, 20):
            letters += grid[x][y]
        # print(f"{letters}")
        matches = re.findall(word, letters)
        if matches:
            print(
                f"{"search_word_by_column":42} ({y:02},{letters.index(word):02}) {matches}"
            )
        matches = re.findall(word, letters[::-1])
        if matches:
            print(
                f"{"search_word_by_column [::-1]":42} ({y:02},{19 - letters[::-1].index(word):02}) {matches}"
            )
        letters = ""


def bottom_right_up(grid, word):
    y = 19
    x = 19
    grid_len = len(grid[0])
    letters = ""
    # columns count down from 19 to 0
    for cnt in range(20, -1, -1):
        y = 19
        for x in range(cnt, 20):
            letters += grid[x][y]
            y -= 1
        # print(f"{letters}")
        matches = re.findall(word, letters)
        if matches:
            x = letters.index(word)
            print(f"{"bottom_right_up":42} ({letters.index(word) + y:02},) {matches}")
        matches_reverse = re.findall(word, letters[::-1])
        if matches_reverse:
            print(f"{"bottom_right_up [::-1]":42} ({y:02},{x:02}) {matches_reverse}")
        letters = ""


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    validatedata(fall2025.words2025)
    # find3chars("int", fall2025.words2025)
    words_fall2025 = [
        "AFTERBURN",
        "BATMAN",
        "INTERCEPTOR",
        "FLIGHTENGINEER",
        "FOKKERTRIPLANE",
        "GROUNDSUPPORT",
        "MONOPLANE",
        "PURPLEHEART",
        "SHOOTINGSTAR",
        "SPADVII",
        "STRATOTANKER",
        "TAYNINHVILLAGE",
        "TESTPILOT",
        "TURBINE",
        "WILDWEASEL",
    ]

    for word in words_fall2025:
        search_word_by_column(fall2025.words2025, word)
        search_word_by_row(word, fall2025.words2025)
        search_word_left_to_right_and_down(fall2025.words2025, word)
        bottom_left_up(fall2025.words2025, word)
        bottom_right_up(fall2025.words2025, word)
        search_row_for_word_rl(word, fall2025.words2025)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
