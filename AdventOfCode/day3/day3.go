package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
)

func part1(challenge int) {
	/*
		below: cab distance is cut in two straight lines' distances
		d1: from the input square number to the middle of its "edge" (eg: from 16 to 15)
		d2: from the middle of the edge to the center of the grid (eg: from 15 to 1)

		d1 = "radius" of the spiral (variable r"")
		d2 = "offset" (variable "offset")
	*/

	size := int(math.Ceil(math.Sqrt(float64(challenge))))

	// offset = distance from nearest corner to middle of edge minus distance from challenge to corner
	// (in other words: go to corner, then walk back to center of edge)
	offset := int(size / 2)
	offset -= (size*size - challenge) % size

	total := int(size/2) + offset

	fmt.Printf("%d\n", total)
}

// let's use types for fun
type coordinates [2]int
type direction [2]int

// can you even do enums in go?
// also, these are uppercase because they're "constants", but
// 1) can't have constant arrays in go
// 2) because of that, they're exported, which makes little sense, but oh well
var (
	UP    = direction{-1, 0}
	DOWN  = direction{1, 0}
	LEFT  = direction{0, -1}
	RIGHT = direction{0, 1}
)

func takeStep(cursor coordinates, direction direction) coordinates {
	return coordinates{cursor[0] + direction[0], cursor[1] + direction[1]}
}

func sumAdjacent(grid [][]int, cursor [2]int) (total int) {
	total = grid[cursor[0]][cursor[1]-1]
	total += grid[cursor[0]][cursor[1]]
	total += grid[cursor[0]][cursor[1]+1]
	total += grid[cursor[0]+1][cursor[1]-1]
	total += grid[cursor[0]+1][cursor[1]]
	total += grid[cursor[0]+1][cursor[1]+1]
	total += grid[cursor[0]-1][cursor[1]-1]
	total += grid[cursor[0]-1][cursor[1]]
	total += grid[cursor[0]-1][cursor[1]+1]

	return
}

func part2(challenge int) {
	// let's build a more-than-big-enough grid and fill it until we find the challenge
	const GRIDSIZE = 101

	grid := make([][]int, GRIDSIZE)
	for i := range grid {
		grid[i] = make([]int, GRIDSIZE)
	}

	grid[int(GRIDSIZE/2)][int(GRIDSIZE/2)] = 1
	cursor := coordinates{int(GRIDSIZE / 2), int(GRIDSIZE / 2)}

	// walk the grid and fill it until we go over the challenge value
	currentValue := 0
	currentDirection := RIGHT
	count := 1
	size := 1

	for currentValue < challenge {
		// count == size: change direction or start next spiral turn
		if count == size {
			count = 1

			switch currentDirection {
			case RIGHT:
				// one more step right, then start next turn
				size += 2
				cursor = takeStep(cursor, currentDirection)
				currentValue = sumAdjacent(grid, cursor)
				grid[cursor[0]][cursor[1]] = currentValue

				count = 2 // because we don't start in the bottom right hand corner
				currentDirection = UP
			case UP:
				currentDirection = LEFT
			case LEFT:
				currentDirection = DOWN
			case DOWN:
				currentDirection = RIGHT
			}
		}

		cursor = takeStep(cursor, currentDirection)

		count++
		currentValue = sumAdjacent(grid, cursor)
		grid[cursor[0]][cursor[1]] = currentValue
	}

	fmt.Printf("%d\n", currentValue)
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println(`Usage: day3 CHALLENGE
With CHALLENGE being an integer.`)

		os.Exit(0)
	}

	challenge, error := strconv.Atoi(os.Args[1]) //277678
	if error != nil {
		panic(error)
	}

	part1(challenge)
	part2(challenge)
}
