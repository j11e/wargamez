package main

import (
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func scorePart1(target int, crabs []int) int {
	fuel := 0
	for i := 0; i < len(crabs); i++ {
		fuel += int(math.Abs(float64(crabs[i] - target)))
	}

	return fuel
}

func scorePart2(target int, crabs []int) int {
	fuel := 0
	for i := 0; i < len(crabs); i++ {
		dist := int(math.Abs(float64(crabs[i] - target)))
		cost := 0
		for j := 0; j <= dist; j++ {
			cost += j
		}
		fuel += cost
	}

	return fuel
}

func main() {
	b, err := os.ReadFile("./day7.txt")
	if err != nil {
		panic(err)
	}
	s := string(b)

	crabsStr := strings.Split(s, ",")

	var crabs []int
	for i := 0; i < len(crabsStr); i++ {
		n, err := strconv.Atoi(crabsStr[i])
		if err != nil {
			panic(err)
		}
		crabs = append(crabs, n)
	}

	// part 1: median
	sort.Ints(crabs)
	var target int
	if len(crabs)%2 == 1 {
		target = crabs[int(len(crabs)/2)+1]
	} else {
		target = (crabs[len(crabs)/2] + crabs[len(crabs)/2-1]) / 2
	}

	fuel := scorePart1(target, crabs)

	fmt.Println("target: ", target, " fuel: ", fuel)

	// part 2: average
	sum := 0
	for i := 0; i < len(crabs); i++ {
		sum += crabs[i]
	}

	avg := float64(sum) / float64(len(crabs))

	score1 := scorePart2(int(math.Ceil(avg)), crabs)
	score2 := scorePart2(int(math.Floor(avg)), crabs)

	if score1 < score2 {
		fmt.Println("target: ", int(math.Ceil(avg)), " fuel: ", score1)
	} else {
		fmt.Println("target: ", int(math.Floor(avg)), " fuel: ", score2)
	}
}
