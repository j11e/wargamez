package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const BINGO_BOARD_WIDTH = 5
const BINGO_BOARD_HEIGHT = 5

type BingoRow struct {
	cells  [BINGO_BOARD_WIDTH]int
	states [BINGO_BOARD_WIDTH]bool // true = marked
}

type BingoBoard struct {
	winning bool
	rows    [BINGO_BOARD_HEIGHT]BingoRow
}

func GetInstructionsAndBoards(lines []string) ([]int, []BingoBoard) {
	iStr := strings.Split(lines[0], ",")

	var instructions []int
	for i := 0; i < len(iStr); i++ {
		c, err := strconv.ParseInt(iStr[i], 10, 64)
		if err != nil {
			panic(err)
		}

		instructions = append(instructions, int(c))
	}

	// iterate over blocks of 5 lines to create the boards
	var boards []BingoBoard
	for i := 0; (i*6)+2 < len(lines); i++ {
		var board BingoBoard
		for j := 0; j < 5; j++ {
			s := strings.Split(lines[2+(6*i)+j], " ")
			var is []int

			// convert the string values to ints
			for k := 0; k < len(s); k++ {
				// one-digit values are padded with spaces, creating empties in the split
				if s[k] != "" {
					convd, err := strconv.ParseInt(s[k], 10, 64)
					if err != nil {
						panic(err)
					}
					is = append(is, int(convd))
				}
			}

			board.rows[j].cells = *(*[5]int)(is)
		}

		boards = append(boards, board)
	}

	return instructions, boards
}

func Mark(board BingoBoard, number int) BingoBoard {
	for i := 0; i < len(board.rows); i++ {
		r := &board.rows[i]
		for j := 0; j < len(r.cells); j++ {
			if r.cells[j] == number {
				r.states[j] = true
			}
		}
	}

	return board
}

func IsWinning(board BingoBoard) bool {
	for i := 0; i < len(board.rows); i++ {
		winningRow := true
		winningCol := true

		for j := 0; j < len(board.rows[i].states); j++ {
			winningRow = winningRow && board.rows[i].states[j]
			winningCol = winningCol && board.rows[j].states[i]
		}

		if winningRow {
			return true
		}

		if winningCol {
			return true
		}
	}
	return false
}

func CalculateBaseScore(board BingoBoard) int {
	score := 0
	for i := 0; i < len(board.rows); i++ {
		for j := 0; j < len(board.rows[i].cells); j++ {
			if !board.rows[i].states[j] {
				score += board.rows[i].cells[j]
			}
		}
	}

	return score
}

func part1(instructions []int, boards []BingoBoard) int {
	for i := 0; i < len(instructions); i++ {
		for j := 0; j < len(boards); j++ {
			boards[j] = Mark(boards[j], instructions[i])

			if IsWinning(boards[j]) {
				return CalculateBaseScore(boards[j]) * instructions[i]
			}
		}
	}

	return -1
}

func part2(instructions []int, boards []BingoBoard) int {
	boardsLeft := len(boards)

	for i := 0; i < len(instructions); i++ {
		for j := 0; j < len(boards); j++ {
			if boards[j].winning {
				continue
			}

			boards[j] = Mark(boards[j], instructions[i])

			if IsWinning(boards[j]) {
				if boardsLeft == 1 {
					return CalculateBaseScore(boards[j]) * instructions[i]
				}

				boards[j].winning = true
				boardsLeft -= 1
			}
		}
	}

	return -1
}

func main() {
	content, err := os.ReadFile("./day4.txt")
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(content), "\n")
	is, bs := GetInstructionsAndBoards(lines)

	score := part1(is, bs)
	fmt.Println(score)

	score = part2(is, bs)
	fmt.Println(score)
}
