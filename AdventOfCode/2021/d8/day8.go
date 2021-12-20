package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
)

// key: signal patterns; value: output
type InputEntry map[[10]string][4]string

// mapping of unscrambled segments to numbers
var segmentsMap map[string]int = map[string]int{
	"abcefg":  0,
	"cf":      1,
	"acdeg":   2,
	"acdfg":   3,
	"bcdf":    4,
	"abdfg":   5,
	"abdefg":  6,
	"acf":     7,
	"abcdefg": 8,
	"abcdfg":  9,
}

var segmentFrequencies map[rune]int = map[rune]int{
	'a': 8,
	'b': 6,
	'c': 8,
	'd': 7,
	'e': 4,
	'f': 9,
	'g': 7,
}

// recognizes that fc is the same as cf, which is number 1
func matchNumberSegments(scrambled string) *int {
	runes := []rune(scrambled)
	sort.Slice(runes, func(i, j int) bool { return runes[i] < runes[j] })
	if matched, ok := segmentsMap[string(runes)]; ok {
		return &matched
	}

	return nil
}

// mapping from encrypted signal to the original one (eg f -> a)
type DecryptionKey map[rune]rune

func (d DecryptionKey) decrypt(input string) string {
	// bca.decrypt(bca) --> abc
	in := []rune(input)
	clear := make([]rune, len(in))

	for i, c := range in {
		clear[i] = d[c]
	}

	return string(clear)
}

func main() {
	b, err := os.ReadFile("./day8.txt")
	if err != nil {
		panic(err)
	}
	l := strings.Split(string(b), "\n")

	inputEntries := make(InputEntry)
	part1 := 0
	for i := 0; i < len(l); i++ {
		s := strings.Split(l[i], " | ")
		patterns := strings.Split(s[0], " ")
		output := strings.Split(s[1], " ")

		var l [10]string
		for idx, inp := range patterns {
			l[idx] = inp
		}

		var r [4]string
		for idx, out := range output {
			r[idx] = out
			switch len(out) {
			case 2:
				fallthrough
			case 3:
				fallthrough
			case 4:
				fallthrough
			case 7:
				part1++
			}
		}

		inputEntries[l] = r
	}

	fmt.Println(part1, " easy numbers found")

	sum := 0
	c := make(chan int, len(inputEntries))
	for left, right := range inputEntries {
		go processEntry(left, right, c)
	}

	for range inputEntries {
		sum += <-c
	}

	fmt.Println("Part 2:", sum)
}

func processEntry(left [10]string, right [4]string, c chan int) {
	frequencies := map[rune]int{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
	decryptionKey := make(DecryptionKey)

	pByLen := map[int][]string{
		2: {},
		3: {},
		4: {},
		5: {},
		6: {},
		7: {},
	}

	for _, s := range left {
		for _, c := range s {
			frequencies[rune(c)] += 1
		}

		pByLen[len(s)] = append(pByLen[len(s)], s)
	}

	// deduce Xc, Xf from 1
	if frequencies[rune(pByLen[2][0][0])] == 8 {
		decryptionKey[rune(pByLen[2][0][0])] = 'c'
		decryptionKey[rune(pByLen[2][0][1])] = 'f'
	} else {
		decryptionKey[rune(pByLen[2][0][0])] = 'f'
		decryptionKey[rune(pByLen[2][0][1])] = 'c'
	}

	// deduce Xa from 7
	for _, c := range pByLen[3][0] {
		if decryptionKey[c] == 0 {
			decryptionKey[c] = 'a'
		}
	}

	// deduce Xb, Xd from 4
	for _, c := range pByLen[4][0] {
		if decryptionKey[c] == 0 {
			if frequencies[c] == 6 {
				decryptionKey[c] = 'b'
			} else {
				decryptionKey[c] = 'd'
			}
		}
	}

	// remains: Xe, Xg
	for _, c := range pByLen[7][0] {
		if decryptionKey[c] == 0 {
			if frequencies[c] == 4 {
				decryptionKey[c] = 'e'
			} else {
				decryptionKey[c] = 'g'
			}
		}
	}

	sum := 0
	powerOfTen := 1000
	for _, c := range right {
		sum += powerOfTen * *matchNumberSegments(decryptionKey.decrypt(c))
		powerOfTen /= 10
	}

	c <- sum
}
