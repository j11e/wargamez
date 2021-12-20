package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func part1(file io.Reader) (int, int) {
	horiz_poz := 0
	depth := 0

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		instruction := strings.Split(scanner.Text(), " ")

		number, err := strconv.Atoi(instruction[1])
		if err != nil {
			panic(err)
		}

		switch instruction[0] {
		case "forward":
			horiz_poz += number
		case "down":
			depth += number
		case "up":
			depth -= number
		}
	}

	return horiz_poz, depth
}

func part2(file io.Reader) (int, int) {
	scanner := bufio.NewScanner(file)

	hp, d, aim := 0, 0, 0

	for scanner.Scan() {
		instruction := strings.Split(scanner.Text(), " ")

		number, err := strconv.Atoi(instruction[1])
		if err != nil {
			panic(err)
		}

		switch instruction[0] {
		case "forward":
			hp += number
			d += number * aim
		case "down":
			aim += number
		case "up":
			aim -= number
		}
	}

	return hp, d
}

func main() {
	file, err := os.Open("./day2.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	hp, d := part1(file)
	fmt.Printf("%d\n", hp*d)

	file.Seek(0, io.SeekStart)

	hp, d = part2(file)
	fmt.Printf("%d\n", hp*d)
}
