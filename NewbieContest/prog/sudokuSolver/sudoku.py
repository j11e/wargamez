import requests
from copy import deepcopy 

url_in = "https://www.newbiecontest.org/epreuves/prog/progsudoku.php"
url_out = "https://www.newbiecontest.org/epreuves/prog/verifprsudoku.php"

cookies = {
    "PHPSESSID": "0f5a68209c4d3306a80b40f70536937f",
    "SMFCookie89": "a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2266929%22%3Bi%3A1%3Bs%3A40%3A%228aa08e09e0976cb352be5a6eff657591f1b75e5e%22%3Bi%3A2%3Bi%3A1705080948%3Bi%3A3%3Bi%3A0%3B%7D"
}


def parse_grid_html(html):
    """Walk the HTML table, create a grid from it
    """
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    html = html.split("\n")

    i, j = 0, 0
    offset_i, offset_j = 0, 0

    for line in html:
        if '<td class="chiff' in line:
            grid[i+3*offset_i][j+3*offset_j] = int(line.split('>')[1].split('<')[0])

            # HTML tables are weird, arrays are logical... so we need to walk funny
            j += 1
            if j%3 == 0:
                j = 0
                i += 1

            if i%3 == 0 and i>0:
                i = 0
                offset_j += 1

            if offset_j % 3 == 0 and offset_j > 0:
                offset_i += 1
                offset_j = 0
                j = 0

    return grid


def pretty_print(grid):
    """Ok, it's not that pretty, but it's still better than printing the array"""
    print("-------------------------------------")
    for line in grid:
        line = list(map(str, line))

        print("| %s |" % ' | '.join(line))
        print("-------------------------------------")


def get_square(grid, i, flattened=True):
    """Squares are numbered as such:
     0  1  2
     3  4  5
     6  7  8
    because I say so.
    If flattened = true, returns a flat list. If not, three arrays of 3 numbers.
    """
    grid_corner = [
        [0, 0], [0, 3], [0, 6],
        [3, 0], [3, 3], [3, 6],
        [6, 0], [6, 3], [6, 6]
    ][i]

    square = []
    square.append(grid[grid_corner[0]][grid_corner[1]:grid_corner[1]+3])
    square.append(grid[grid_corner[0]+1][grid_corner[1]:grid_corner[1]+3])
    square.append(grid[grid_corner[0]+2][grid_corner[1]:grid_corner[1]+3])

    if flattened:
        flat = [] 
        for sublist in square:
            for value in sublist:
                flat.append(value)

        square = flat

    return square


def get_column(grid, i):
    """Columns are numbered naturally."""
    column = []
    for line in grid:
        column.append(line[i])
    return column


def get_missing_in_square(grid, i):
    """returns the numbers missing from a given square"""
    square = get_square(grid, i, True)
    missing = []

    for number in range(1, 10):
        if number not in square:
            missing.append(number)

    return missing


def get_missing_in_column(grid, column_number):
    """returns the numbers missing from a given square"""
    column = get_column(grid, column_number)

    missing = []
    for number in range(1, 10):
        if number not in column:
            missing.append(number)

    return missing


def get_missing_in_row(grid, row):
    """returns the numbers missing from a given square"""
    row = grid[row]

    missing = []
    for number in range(1, 10):
        if number not in row:
            missing.append(number)

    return missing


def get_square_box(row, column):
    """what square is box (row, column) in?"""
    grid_corners = [
        [0, 0], [0, 3], [0, 6],
        [3, 0], [3, 3], [3, 6],
        [6, 0], [6, 3], [6, 6]
    ]

    for index, corner in enumerate(grid_corners):
        if row >= corner[0] and row < corner[0]+3 \
               and column >= corner[1] and column < corner[1]+3:
            return index


def get_possible_values_for_box(grid, row, column):
    missing_in_square = get_missing_in_square(grid, get_square_box(row, column))
    missing_in_column = get_missing_in_column(grid, column)
    missing_in_row = get_missing_in_row(grid, row)

    return list(set(missing_in_square) & set(missing_in_column) & set(missing_in_row))


def solve(grid):
    """Solves the sudoku. Returns a pair of values: a boolean indicating success, and the grid.
    If, after walking the entire grid, no number is found
    """
    grid = deepcopy(grid)
    original_grid = deepcopy(grid) # keep an unmodified copy to return in case of failure (wrong assumptions)

    stop = False
    while not stop:
        not_found_yet = 0
        found_this_round = 0
        smallest_set_possible_vals = [0,0, [0,0,0,0,0,0,0,0,0,0]]

        for line_num, line in enumerate(grid):
            for box_num, box in enumerate(line):
                if box == 0:
                    not_found_yet += 1

                    possible_vals = get_possible_values_for_box(grid, line_num, box_num)

                    if len(possible_vals) == 0:
                        print("Error! No possible values for box (%d, %d)" % (line_num, box_num))
                        return False, grid
                    elif len(possible_vals) == 1:
                        grid[line_num][box_num] = possible_vals[0]
                        found_this_round += 1

                        # the grid's state changed: must invalidate earlier suspects 
                        smallest_set_possible_vals = [0,0, [0,0,0,0,0,0,0,0,0,0]]
                    elif len(possible_vals) < len(smallest_set_possible_vals[2]):
                        smallest_set_possible_vals = [line_num, box_num, possible_vals]

        
        if not_found_yet == 0:
            print("Whole grid solved.")
            return True, grid

        if found_this_round == 0:
            print("Walked through the entire grid, not found a single number :'( WE NEED TO GO DEEPER")
            for possible_val in smallest_set_possible_vals[2]:
                copy = list(grid)
                grid[smallest_set_possible_vals[0]][smallest_set_possible_vals[1]] = possible_val
                success, solved = solve(grid)

                if success:
                    return True, solved

            print("Tried all the possible values, none led to a valid solution! Bad speculative exec branch ;)")
            return False, original_grid


if __name__ == "__main__":
    r = requests.get(url_in, cookies=cookies)

    print(r.text)
    grid = parse_grid_html(r.text)
    pretty_print(grid)

    success, solved_grid = solve(grid)
    
    result = success and "Success" or "Failure"
    print("%s! Current grid state:" % result)
    pretty_print(solved_grid)

    if success:
        solution = []
        for line in solved_grid:
            solution.append(''.join(map(str, line)))
        
        solution = '-'.join(solution)

        # r = requests.get(url_out, cookies=cookies, params={"solution": solution})
        # print(r.text)
