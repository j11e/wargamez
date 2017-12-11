package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func intify(array []string) []int {
	intified := make([]int, len(array))

	for i := 0; i < len(array); i++ {
		value, err := strconv.Atoi(array[i])
		if err != nil {
			panic(err)
		}

		intified[i] = value
	}

	return intified
}

func part1Modifier(offset int) int {
	return offset + 1
}

func part2Modifier(offset int) int {
	if offset >= 3 {
		return offset - 1
	}

	return offset + 1
}

func followOffsetsWithModifier(offsets []int, offsetModifier func(int) int) {
	total := 0
	currentIndex := 0

	for currentIndex < len(offsets) {
		total++

		offset := offsets[currentIndex]

		offsets[currentIndex] = offsetModifier(offset)
		currentIndex += offset
	}

	fmt.Printf("%d\n", total)
}

func main() {
	challenge, err := ioutil.ReadFile("/tmp/aoc_day5.txt")
	if err != nil {
		panic(err)
	}

	offsets := intify(strings.Split(strings.TrimSpace(string(challenge)), "\n"))
	followOffsetsWithModifier(offsets, part1Modifier)

	offsets = intify(strings.Split(strings.TrimSpace(string(challenge)), "\n"))
	followOffsetsWithModifier(offsets, part2Modifier)
}
