package main

import (
	"fmt"
	"io/ioutil"
	"reflect"
	"strconv"
	"strings"
)

const (
	maxUint = ^uint(0)
	maxInt  = int(maxUint >> 1)
	minInt  = -maxInt - 1
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

func findMaxBank(array []int) (maxIdx int) {
	max := minInt

	for i := 0; i < len(array); i++ {
		if array[i] > max {
			max = array[i]
			maxIdx = i
		}
	}

	return
}

func redistributeUntilStateRepeats(banks []int) ([]int, int) {
	total := 0
	knownStates := [][]int{}

	tmp := make([]int, len(banks))
	copy(tmp, banks)
	knownStates = append(knownStates, tmp)

	for {
		total++

		idx := findMaxBank(banks)
		redistributed := banks[idx]
		banks[idx] = 0

		for redistributed > 0 {
			idx = (idx + 1) % len(banks)
			banks[idx]++
			redistributed--
		}

		for _, knownState := range knownStates {
			if reflect.DeepEqual(knownState, banks) {
				return banks, total
			}
		}

		tmp := make([]int, len(banks))
		copy(tmp, banks)
		knownStates = append(knownStates, tmp)
	}
}

func main() {
	challenge, err := ioutil.ReadFile("/tmp/aoc_day6.txt")
	if err != nil {
		panic(err)
	}

	banks := intify(strings.Split(strings.TrimSpace(string(challenge)), "\t"))

	banks, total := redistributeUntilStateRepeats(banks)
	fmt.Printf("Loop state: %v (reached after %d cycles) \n", banks, total)

	banks, total = redistributeUntilStateRepeats(banks)
	fmt.Printf("Loop state: %v (reached after %d cycles) \n", banks, total)
}
