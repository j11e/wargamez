package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func simulateFish(initialState []int, turns int) int {
	var timerCounts [9]int
	for i := 0; i < len(initialState); i++ {
		timerCounts[initialState[i]]++
	}

	for i := 0; i < turns; i++ {
		newAdditions := timerCounts[0]
		tmp := timerCounts[0]
		for j := 0; j < 8; j++ {
			timerCounts[j] = timerCounts[j+1]

			if j == 6 {
				timerCounts[j] += tmp
			}
		}
		timerCounts[8] = newAdditions
	}

	count := 0
	for i := 0; i < 9; i++ {
		count += timerCounts[i]
	}

	return count
}

func main() {
	b, err := os.ReadFile("./day6.txt")
	if err != nil {
		panic(err)
	}
	s := string(b)

	stateStr := strings.Split(s, ",")

	var state []int
	for i := 0; i < len(stateStr); i++ {
		n, err := strconv.Atoi(stateStr[i])
		if err != nil {
			panic(err)
		}
		state = append(state, n)
	}

	fmt.Println(simulateFish(state, 80))
	fmt.Println(simulateFish(state, 256))
}
