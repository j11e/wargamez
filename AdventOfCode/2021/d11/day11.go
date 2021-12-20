package main

import (
	"fmt"
	"os"
	"strings"
)

type Elem struct {
	r, c int
}
type Matrix [][]int

func (m *Matrix) Neighbors(e Elem) []Elem {
	n := make([]Elem, 0)

	if e.r > 0 {
		n = append(n, Elem{e.r - 1, e.c})
	}
	if e.r < len(*m)-1 {
		n = append(n, Elem{e.r + 1, e.c})
	}
	if e.c > 0 {
		n = append(n, Elem{e.r, e.c - 1})
	}
	if e.c < len((*m)[e.r])-1 {
		n = append(n, Elem{e.r, e.c + 1})
	}
	if e.r > 0 && e.c > 0 {
		n = append(n, Elem{e.r - 1, e.c - 1})
	}
	if e.r > 0 && e.c < len((*m)[e.r])-1 {
		n = append(n, Elem{e.r - 1, e.c + 1})
	}
	if e.r < len(*m)-1 && e.c > 0 {
		n = append(n, Elem{e.r + 1, e.c - 1})
	}
	if e.r < len(*m)-1 && e.c < len((*m)[e.r])-1 {
		n = append(n, Elem{e.r + 1, e.c + 1})
	}

	return n
}

func (m *Matrix) Flash(e Elem, f map[Elem]bool) {
	n := m.Neighbors(e)
	f[e] = true

	for i := 0; i < len(n); i++ {
		p := n[i]
		(*m)[p.r][p.c] += 1

		if _, ok := f[p]; (*m)[p.r][p.c] > 9 && !ok {
			f[p] = true
			n = append(n, m.Neighbors(p)...)
		}
	}

	for p := range f {
		(*m)[p.r][p.c] = 0
	}
}

func (m *Matrix) Print() {
	for _, r := range *m {
		for _, v := range r {
			fmt.Print(v)
		}
		fmt.Println("")
	}
}

func main() {
	b, err := os.ReadFile("./day11.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(b), "\n")

	m := make(Matrix, 10)
	for r, l := range lines {
		m[r] = make([]int, 10)
		for c, o := range l {
			m[r][c] = int(o - '0')
		}
	}

	f := 0
	for t := 0; t < 10000; t++ {
		for r, l := range m {
			for c := range l {
				m[r][c] += 1
			}
		}

		flashes := map[Elem]bool{}
		for r, l := range m {
			for c, o := range l {
				if o > 9 {
					m.Flash(Elem{r, c}, flashes)
				}
			}
		}
		f += len(flashes)

		if len(flashes) == 100 {
			fmt.Println("All octopuses flashed (flosh?) sync'ly on turn ", (t + 1))
			return
		}

		for e := range flashes {
			m[e.r][e.c] = 0
		}

		if t == 99 {
			fmt.Println("After 100 rounds, there's been ", f, " flashes")
		}
	}

}
