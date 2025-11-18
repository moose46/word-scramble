# This is a sample Python script.

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
    for c in range(len(word)):
        print(f"looking for: {word[c]}")
        for rownum in range(len(grid)):
            print(f"\tgrid row={rownum}")
            for rowcharnum in range(len(grid[rownum])):
                # print(rowchar, end=" ")
                if word[c].upper() == grid[rownum][rowcharnum].upper():
                    if rowcharnum < len(grid[rownum]) - 1:
                        if word[c+1] == grid[rownum][rowcharnum+1 and rowcharnum+2]:
                            print(f"\t\trow={rownum} rowchar={rowcharnum} {word[c]}", end=None)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    validateData(fall2025.words2025)
    find3chars("int", fall2025.words2025)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
