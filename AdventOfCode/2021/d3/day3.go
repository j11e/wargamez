package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func CountZeroesAtPositions(input []string, lineSize int) ([]int, int) {
	lines := 0
	bitcounts := make([]int, lineSize)

	for i := 0; i < len(input); i++ {
		lines += 1
		line := input[i]

		number, err := strconv.ParseInt(line, 2, 32)
		if err != nil {
			panic(err)
		}

		for i := 0; i < lineSize; i++ {
			if number&1 == 0 {
				bitcounts[lineSize-1-i] += 1 // endianness...
			}
			number >>= 1
		}
	}

	return bitcounts, lines
}

func part1(input []string, lineSize int) (int, int) {
	bitcounts, lines := CountZeroesAtPositions(input, lineSize)

	var gamma, epsilon string
	for i := 0; i < lineSize; i++ {
		if bitcounts[i] > lines/2 {
			gamma = gamma + "0"
			epsilon = epsilon + "1"
		} else {
			gamma = gamma + "1"
			epsilon = epsilon + "0"
		}
	}

	g, err := strconv.ParseInt(gamma, 2, 32)
	if err != nil {
		panic(err)
	}
	e, err := strconv.ParseInt(epsilon, 2, 32)
	if err != nil {
		panic(err)
	}

	return int(e), int(g)
}

func part2(input []string, lineSize int) (int, int) {
	// O rating
	selected := input[:]

	for i := 0; i < lineSize && len(selected) > 1; i++ {
		zeroesAtPos, lines := CountZeroesAtPositions(selected, lineSize)
		mostCommon := "1"
		if zeroesAtPos[i] > lines/2 {
			mostCommon = "0"
		}
		var kept []string
		for j := 0; j < len(selected); j++ {
			if string(selected[j][i]) == mostCommon {
				kept = append(kept, selected[j])
			}
		}

		selected = kept
	}
	o, err := strconv.ParseInt(selected[0], 2, 32)
	if err != nil {
		panic(err)
	}

	// CO2 rating
	selected = input[:]

	for i := 0; i < lineSize && len(selected) > 1; i++ {
		zeroesAtPos, lines := CountZeroesAtPositions(selected, lineSize)
		leastCommon := "0"
		if zeroesAtPos[i] > lines/2 {
			leastCommon = "1"
		}
		var kept []string
		for j := 0; j < len(selected); j++ {
			if string(selected[j][i]) == leastCommon {
				kept = append(kept, selected[j])
			}
		}

		selected = kept
	}
	co2, err := strconv.ParseInt(selected[0], 2, 32)
	if err != nil {
		panic(err)
	}

	return int(o), int(co2)
}

func main() {
	s, err := os.ReadFile("./day3.txt")
	if err != nil {
		panic(err)
	}
	input := strings.Split(string(s), "\n")

	g, e := part1(input, 12)
	fmt.Println(g * e)

	o, co2 := part2(input, 12)
	fmt.Println(o * co2)
}
