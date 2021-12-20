package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Point struct {
	x, y int
}

func CountPoints(matrix map[Point]int) int {
	score := 0
	for _, v := range matrix {
		if v > 1 {
			score += 1
		}
	}
	return score
}

func main() {
	s, err := os.ReadFile("./day5.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(s), "\n")

	matrix := make(map[Point]int)

	for i := 0; i < len(lines); i++ {
		points := strings.Split(lines[i], " -> ")

		start := strings.Split(points[0], ",")
		x1, _ := strconv.Atoi(start[0])
		y1, _ := strconv.Atoi(start[1])

		end := strings.Split(points[1], ",")
		x2, _ := strconv.Atoi(end[0])
		y2, _ := strconv.Atoi(end[1])

		if x1 == x2 {
			if y1 < y2 {
				for i := y1; i <= y2; i++ {
					matrix[Point{x1, i}]++
				}
			} else {
				for i := y2; i <= y1; i++ {
					matrix[Point{x1, i}]++
				}
			}
		} else if y1 == y2 {
			if x1 < x2 {
				for i := x1; i <= x2; i++ {
					matrix[Point{i, y1}]++
				}
			} else {
				for i := x2; i <= x1; i++ {
					matrix[Point{i, y1}]++
				}
			}
		} else {
			if x1 < x2 {
				yStep := 1
				if y1 > y2 {
					yStep = -1
				}
				for i := x1; i <= x2; i++ {
					matrix[Point{i, y1}]++
					y1 += yStep
				}
			} else {
				yStep := 1
				if y2 > y1 {
					yStep = -1
				}
				for i := x2; i <= x1; i++ {
					matrix[Point{i, y2}]++
					y2 += yStep
				}
			}
		}
	}

	res := CountPoints(matrix)

	fmt.Println("There are ", res, " points where more than 2 lines intersect")
}
