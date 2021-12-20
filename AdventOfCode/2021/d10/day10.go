package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
)

type Chunk struct {
	oc rune // opening rune, eg "("
}

func main() {
	b, err := os.ReadFile("./day10.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(b), "\n")

	delimiterChars := map[rune]rune{
		'(': ')',
		'{': '}',
		'[': ']',
		'<': '>',
	}

	p1score := 0
	p2scores := make([]int, 0)

outer:
	for _, l := range lines {
		cs := make([]Chunk, 0)
		var cc Chunk

		for _, c := range l {
			if _, ok := delimiterChars[c]; ok {
				// new sub-chunk
				cc = Chunk{oc: c}
				cs = append(cs, cc)
			} else if c == delimiterChars[cc.oc] {
				cs = cs[:len(cs)-1]

				if len(cs) > 0 {
					cc = cs[len(cs)-1]
				}
			} else {
				// corrupted line
				switch c {
				case ')':
					p1score += 3
				case ']':
					p1score += 57
				case '}':
					p1score += 1197
				case '>':
					p1score += 25137
				}

				continue outer
			}
		}

		s := 0
		for j, _ := range cs {
			s *= 5
			switch delimiterChars[cs[len(cs)-1-j].oc] {
			case ')':
				s += 1
			case ']':
				s += 2
			case '}':
				s += 3
			case '>':
				s += 4
			}
		}
		p2scores = append(p2scores, s)
	}

	sort.Ints(p2scores)
	fmt.Println("p1score = ", p1score)
	fmt.Println("middle p2score =", p2scores[len(p2scores)/2])
}
