package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strconv"
	"strings"
)

// takes an array of string, maps it with the int() function
func intify(array []string) []int {
	result := make([]int, len(array))

	for i, value := range array {
		integered, err := strconv.Atoi(value)
		if err != nil {
			panic(err)
		}

		result[i] = int(integered)
	}

	return result
}

func part1Selector(haystack []int) int {
	min := int(^uint(0) >> 1)
	max := 0

	for _, val := range haystack {
		if val > max {
			max = val
		}

		if val < min {
			min = val
		}
	}

	return max - min
}

func part2Selector(haystack []int) (resultValue int) {
	sort.Ints(haystack)

	for i := 0; i < len(haystack); i++ {
		for j := i + 1; j < len(haystack); j++ {
			if haystack[j]%haystack[i] == 0 {
				resultValue = haystack[j] / haystack[i]
				return
			}
		}
	}

	return
}

func sumSelectedIntsPerLineWithSelector(lines []string, selector func([]int) int) {
	total := int(0)

	for _, line := range lines {
		line = strings.TrimSpace(line)
		values := intify(strings.Split(line, "\t"))

		val := selector(values)
		total += val
	}

	fmt.Println(total)
}

func main() {
	data, err := ioutil.ReadFile("/tmp/aoc_day2.txt")
	if err != nil {
		panic(err)
	}

	challenge := strings.TrimSpace(string(data))
	lines := strings.Split(challenge, "\n")

	sumSelectedIntsPerLineWithSelector(lines, part1Selector)
	sumSelectedIntsPerLineWithSelector(lines, part2Selector)
}
