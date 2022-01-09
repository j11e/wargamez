package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Coord struct {
	x, y int
}
type Matrix map[Coord]bool

func (m Matrix) print() {
	w := 0
	h := 0
	for k, _ := range m {
		if k.x > w {
			w = k.x
		}

		if k.y > h {
			h = k.y
		}
	}

	fmt.Println("Matrix is ", w, "x", h)
	fmt.Println("")
	pm := make([][]bool, w+1)
	for i := range pm {
		nr := make([]bool, h+1)
		pm[i] = nr
	}

	for k := range m {
		pm[k.x][k.y] = true
	}

	for i := range pm {
		line := ""
		for j := range pm[i] {
			if pm[i][j] {
				line += "X"
			} else {
				line += " "
			}
		}
		fmt.Println(line)
	}
}

func main() {
	b, err := os.ReadFile("./day13.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(b), "\n")

	m := Matrix{}

	instructions := []string{}
	set := "dots"
	for _, l := range lines {
		if l == "" {
			set = "instructions"
		} else {
			if set == "dots" {
				bits := strings.Split(l, ",")
				x, _ := strconv.Atoi(bits[1])
				y, _ := strconv.Atoi(bits[0])

				c := Coord{x, y}
				m[c] = true
			} else {
				instructions = append(instructions, l)
			}
		}
	}

	for c, i := range instructions {
		i = strings.Split(i, " ")[2]

		m = fold(m, i)

		if c == 1 {
			count := len(m)
			fmt.Println(count, " points left in the matrix after the 1st fold")
		}
	}

	m.print()
}

func fold(m Matrix, i string) Matrix {
	s := strings.Split(i, "=")
	l, _ := strconv.Atoi(s[1])

	nm := Matrix{}
	if s[0] == "y" {
		for k, v := range m {
			if k.x < l {
				nm[k] = v
			} else {
				nm[Coord{l - (k.x - l), k.y}] = v
			}
		}
	} else {
		for k, v := range m {
			if k.y < l {
				nm[k] = v
			} else {
				nm[Coord{k.x, l - (k.y - l)}] = v
			}
		}
	}

	return nm
}
