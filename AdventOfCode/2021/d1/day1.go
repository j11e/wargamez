package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
)

func ReadNextIntFromScanner(scanner *bufio.Scanner) (int, error) {
	return strconv.Atoi(scanner.Text())
}

func GetInitialSlidingWindowSum(scanner *bufio.Scanner, windowSize int) (int, []int) {
	sum := 0
	var elements []int

	for i := 0; i < windowSize; i++ {
		scanner.Scan()
		num, err := ReadNextIntFromScanner(scanner)
		if err != nil {
			panic(err)
		}

		elements = append(elements, num)
		sum += num
	}

	return sum, elements
}

func CountIncrementsInSlidingWindows(input io.Reader, windowSize int) {
	scanner := bufio.NewScanner(input)

	curWindow, curElems := GetInitialSlidingWindowSum(scanner, windowSize)

	numberOfIncrements := 0

	for scanner.Scan() {
		current, err := ReadNextIntFromScanner(scanner)
		if err != nil {
			panic(err)
		}

		if (curWindow + current - curElems[0]) > curWindow {
			numberOfIncrements += 1
		}

		curWindow = curWindow + current - curElems[0]
		curElems = curElems[1:]
		curElems = append(curElems, current)
	}

	fmt.Println("There are ", numberOfIncrements, " increments of size ", windowSize)
}

func part1() {
	file, err := os.Open("./day1.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close() // https://www.joeshaw.org/dont-defer-close-on-writable-files/

	CountIncrementsInSlidingWindows(file, 1)
}

func part2() {
	file, err := os.Open("./day1.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	CountIncrementsInSlidingWindows(file, 3)
}

func main() {
	part1()
	part2()
}
