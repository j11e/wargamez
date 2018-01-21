import requests

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
    grid = grid[:]
    print("-------------------------------------")
    for line in grid:
        line = list(map(str, line))

        print("| %s |" % ' | '.join(line))
        print("-------------------------------------")


def get_square(grid, i):
    """Squares are numbered as such:
     0  1  2
     3  4  5
     6  7  8
    because I say so.
    """
    grid = grid[:] # work on a copy!

    grid_corner = [
        [0, 0], [0, 3], [0, 6],
        [3, 0], [3, 3], [3, 6],
        [6, 0], [6, 3], [6, 6]
    ][i]

    square = []
    square.append(grid[grid_corner[0]][grid_corner[1]:grid_corner[1]+3])
    square.append(grid[grid_corner[0]+1][grid_corner[1]:grid_corner[1]+3])
    square.append(grid[grid_corner[0]+2][grid_corner[1]:grid_corner[1]+3])

    return square


def get_column(grid, i):
    """Columns are numbered naturally."""
    grid = grid[:] # work on a copy!
    column = []
    for j in range(9):
        column.append(grid[j][i])
    return column


def get_missing_in_square(grid, i):
    """returns the numbers missing from a given square"""
    square = get_square(grid, i)
    square = square[0] + square[1] + square[2] # flatten the square
    missing = []

    for number in range(1, 10):
        if number not in square:
            missing.append(number)

    return missing


def get_missing_in_column(grid, i):
    """returns the numbers missing from a given square"""
    column = get_column(grid, i)
    for row in grid:
        column.append(row[i])

    missing = []
    for number in range(1, 10):
        if number not in column:
            missing.append(number)

    return missing


def get_missing_in_row(grid, i):
    """returns the numbers missing from a given square"""
    row = grid[i]

    missing = []
    for number in range(1, 10):
        if number not in row:
            missing.append(number)

    return missing


def get_square_box(i,j):
    """what square is box (i,j) in?"""
    grid_corners = [
        [0, 0], [0, 3], [0, 6],
        [3, 0], [3, 3], [3, 6],
        [6, 0], [6, 3], [6, 6]
    ]

    for index, corner in enumerate(grid_corners):
        if i >= corner[0] and i < corner[0]+3 \
               and j >= corner[1] and j < corner[1]+3:
            return index


if __name__ == "__main__":
    r = requests.get(url_in, cookies=cookies)

    print(r.text)
    grid = parse_grid_html(r.text)
    
    pretty_print(grid)
