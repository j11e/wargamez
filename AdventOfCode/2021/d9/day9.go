package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
)

type Elem struct {
	x, y int
}
type HeightMatrix [][]int
type Basins map[Elem]Elem

func (m HeightMatrix) Neighbors(e Elem) []Elem {
	n := make([]Elem, 0)

	if e.x > 0 {
		n = append(n, Elem{e.x - 1, e.y})
	}

	if e.x < len(m)-1 {
		n = append(n, Elem{e.x + 1, e.y})
	}

	if e.y > 0 {
		n = append(n, Elem{e.x, e.y - 1})
	}

	if e.y < len(m[e.x])-1 {
		n = append(n, Elem{e.x, e.y + 1})
	}

	return n
}

func (m HeightMatrix) LowPoint(e Elem) bool {
	for _, n := range m.Neighbors(e) {
		if m[n.x][n.y] <= m[e.x][e.y] {
			return false
		}
	}

	return true
}

func (m HeightMatrix) ExpandBasin(b Basins, lp Elem) (Basins, int) {
	//b := Basins{lp: lp} // hashmap for quicker lookup during iteration
	b[lp] = lp
	n := m.Neighbors(lp)
	c := 1

	// for _, e := range n {
	for i := 0; i < len(n); i++ {
		e := n[i]
		if _, ok := b[e]; ok {
			continue
		}

		if m[e.x][e.y] == 9 {
			continue
		}

		b[e] = lp
		c += 1
		n = append(n, m.Neighbors(e)...)
	}

	return b, c
}

func main() {
	b, err := os.ReadFile("./day9.txt")
	if err != nil {
		panic(err)
	}
	l := strings.Split(string(b), "\n")

	hm := make(HeightMatrix, 0)
	for _, line := range l {
		row := make([]int, 0)
		for _, i := range line {
			row = append(row, int(i-'0')) // int('1') == 49. int('1' - '0') == 1.
		}
		hm = append(hm, row)
	}

	basins := make(Basins, 0)
	sizes := make(map[Elem]int, 0)
	riskSum := 0
	var s int
	for ir, r := range hm {
		for ic, _ := range r {
			p := Elem{ir, ic}
			if hm.LowPoint(p) {
				basins, s = hm.ExpandBasin(basins, p)

				riskSum += 1 + hm[ir][ic]
				sizes[p] = s
			}
		}
	}

	sizeProduct := 1
	r := make([]int, 0)
	for _, c := range sizes {
		r = append(r, c)
	}
	sort.Ints(r)

	fmt.Println(r[len(r)-3:])
	for _, v := range r[len(r)-3:] {
		sizeProduct *= v
	}

	fmt.Println("(part 1) Sum of risk values of low points: ", riskSum)
	fmt.Println("(part 2) Product of sizes of 3 largest basins: ", sizeProduct)
}
