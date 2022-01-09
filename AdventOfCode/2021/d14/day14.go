package main

import (
	"fmt"
	"math"
	"os"
	"strings"
)

type Pair struct {
	left, right byte
}

type Polymer struct {
	pairs map[Pair]int
	outer [2]byte
}

func main() {
	b, err := os.ReadFile("./day14.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(b), "\n")

	template := lines[0]
	p := Polymer{pairs: map[Pair]int{}}
	for i := 0; i < len(template)-1; i++ {
		pair := Pair{template[i], template[i+1]}

		if _, ok := p.pairs[pair]; !ok {
			p.pairs[pair] = 0
		}

		p.pairs[pair] += 1
	}
	p.outer[0] = template[0]
	p.outer[1] = template[len(template)-1]

	rules := map[Pair]byte{}
	lines = lines[2:]
	for _, l := range lines {
		bits := strings.Split(l, " -> ")
		rules[Pair{bits[0][0], bits[0][1]}] = bits[1][0]
	}

	for t := 0; t < 40; t++ {
		newPolymer := Polymer{pairs: map[Pair]int{}}
		newPolymer.outer = p.outer
		for pair, number := range p.pairs {
			if i, ok := rules[pair]; ok {
				np := Pair{pair.left, i}

				if _, ok := newPolymer.pairs[np]; !ok {
					newPolymer.pairs[np] = 0
				}
				newPolymer.pairs[np] += number

				np = Pair{i, pair.right}

				if _, ok := newPolymer.pairs[np]; !ok {
					newPolymer.pairs[np] = 0
				}
				newPolymer.pairs[np] += number
			}
		}

		p = newPolymer

		if t == 9 {
			min, max := getMinMaxFrequencies(p)
			fmt.Println("After 10 turns, difference between most and least common elements: ", (max - min))
		}
	}

	min, max := getMinMaxFrequencies(p)
	fmt.Println("After 40 turns, difference between most and least common elements: ", (max - min))
}

func getMinMaxFrequencies(polymer Polymer) (int, int) {
	freqs := map[byte]int{}

	for k, v := range polymer.pairs {
		if _, ok := freqs[k.left]; !ok {
			freqs[k.left] = 0
		}
		freqs[k.left] += v

		if _, ok := freqs[k.right]; !ok {
			freqs[k.right] = 0
		}
		freqs[k.right] += v
	}

	freqs[polymer.outer[0]] += 1
	freqs[polymer.outer[1]] += 1

	max := 0
	min := math.MaxInt
	for _, v := range freqs {
		if v < min {
			min = v
		}

		if v > max {
			max = v
		}
	}

	return min / 2, max / 2
}
