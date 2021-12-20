package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func runInstructions(instructions []string) (largestFinal int, largestEver int) {
	registers := map[string]int{}

	for i := 0; i < len(instructions); i++ {
		// a inc 1 if b < 5
		parts := strings.Split(instructions[i], " ")

		if _, ok := registers[parts[0]]; !ok {
			registers[parts[0]] = 0
		}

		// evaluate condition
		operandLeft := parts[4]
		if _, ok := registers[operandLeft]; !ok {
			registers[operandLeft] = 0
		}

		condition := parts[5]
		operandRight, err := strconv.Atoi(parts[6])
		if err != nil {
			panic(err)
		}

		executeOperation := false
		switch condition {
		case "<":
			if registers[operandLeft] < operandRight {
				executeOperation = true
			}
		case "<=":
			if registers[operandLeft] <= operandRight {
				executeOperation = true
			}
		case ">":
			if registers[operandLeft] > operandRight {
				executeOperation = true
			}
		case ">=":
			if registers[operandLeft] >= operandRight {
				executeOperation = true
			}
		case "!=":
			if registers[operandLeft] != operandRight {
				executeOperation = true
			}
		case "==":
			if registers[operandLeft] == operandRight {
				executeOperation = true
			}
		}

		if executeOperation {
			increment, err := strconv.Atoi(parts[2])
			if err != nil {
				panic(err)
			}

			factor := 1
			if parts[1] == "dec" {
				factor = -1
			}

			registers[parts[0]] += factor * increment
			if registers[parts[0]] > largestEver {
				largestEver = registers[parts[0]]
			}
		}
	}

	for _, value := range registers {
		if value > largestFinal {
			largestFinal = value
		}
	}

	return
}

func main() {
	challenge, err := ioutil.ReadFile("/tmp/aoc_day8.txt")
	if err != nil {
		panic(err)
	}

	instructions := strings.Split(strings.TrimSpace(string(challenge)), "\n")

	largestFinal, largestEver := runInstructions(instructions)
	fmt.Printf("Largest register after running the instructions: %d\n", largestFinal)
	fmt.Printf("Largest register value ever during the processing of instructions: %d\n", largestEver)
}
