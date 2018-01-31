import copy # freakin' deep copying, man
import hashlib
import io

import requests
from PIL import Image

url_in = "https://www.newbiecontest.org/epreuves/prog/progshort.php"
url_out = "https://www.newbiecontest.org/epreuves/prog/verifprshort.php"
cookies = {
    "PHPSESSID": "0f5a68209c4d3306a80b40f70536937f",
    "SMFCookie89": "a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2266929%22%3Bi%3A1%3Bs%3A40%3A%228aa08e09e0976cb352be5a6eff657591f1b75e5e%22%3Bi%3A2%3Bi%3A1705080948%3Bi%3A3%3Bi%3A0%3B%7D"
}

START = 0
BLACK = 1
WHITE = 2
EXIT = 3
VISITED = 4

DIRECTIONS = {
    "R": (1, 0, "R"),
    "U": (0, -1, "U"),
    "D": (0, 1, "D")
    "L": (-1, 0, "L"),
}

BLOCK_SIZE = 5
def read_block(pixels, x, y):
    """the image is 55x50 px, each "cell" 5x5 px. This reads cell (i, j), using
    the fact that all 5 pixels are the same color, so reading the first is enough
    """
    return pixels[BLOCK_SIZE*x, BLOCK_SIZE*y]

def get_image():
    r = requests.get(url_in, cookies=cookies)
    image = Image.open(io.BytesIO(r.content))
    # image = Image.open('maze.png')
    return image

def get_maze_from_image(image):
    pixels = image.load()
    size_w, size_h = image.size
    size_w = int(size_w / BLOCK_SIZE)
    size_h = int(size_h / BLOCK_SIZE)

    maze = []

    value_mapping = {
        (0, 0, 0): BLACK,
        (255, 255, 255): WHITE,
        (255, 0, 0): EXIT,
        (0, 0, 255): START
    }

    for i in range(size_w):
        maze.append([])
        for j in range(size_h):
            pixel = read_block(pixels, i, j)
            value = value_mapping[pixel]
            maze[-1].append(value)

            if value == START:
                start = (i,j)

    return maze, start


def get_maze_solutions(maze, start, path=""):
    maze = copy.deepcopy(maze)

    cur_val = maze[start[0]][start[1]]
    if cur_val == BLACK \
            or (path != "" and cur_val == START) \
            or cur_val == VISITED:
        return False, []

    if cur_val == EXIT:
        return True, [path]

    maze[start[0]][start[1]] = VISITED

    solutions = []
    for direction in DIRECTIONS:
        direction = DIRECTIONS[direction]
        success, sols = get_maze_solutions(maze, (start[0]+direction[0], \
            start[1]+direction[1]), path+direction[2])
        if success:
            for solution in sols:
                solutions.append(solution)

    return True, solutions


if __name__ == '__main__':
    print("Getting image")
    img = get_image()
    img.save("maze.png", "PNG")

    print("Converting to maze")
    maze, start = get_maze_from_image(img)

    print("Solving maze")
    success, solutions = get_maze_solutions(maze, start)

    if not success:
        print("If there was a bug in this code, this message would be printed")

    print("Filtering solutions")
    min_length = len(solutions[0])
    for solution in solutions:
        if len(solution) < min_length:
            min_length = len(solution)

    solutions = list(filter(lambda x: len(x) == min_length, solutions))

    print("Submitting response")
    response = hashlib.sha1(''.join(sorted(solutions)).encode("utf8")).hexdigest()
    payload = {
        "solution": response
    }
    r = requests.get(url_out, cookies=cookies, params=payload)
    print(r.text)
