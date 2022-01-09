package main

import (
	"container/heap"
	"fmt"
	"math"
	"os"
	"strings"
)

type Coord struct {
	x, y int
}

type CoordMap map[Coord]int

type PriorityQueue struct {
	elems     *[]Coord // the pointer makes Pop() easier to implement
	positions CoordMap // makes calling Fix easier
	scores    CoordMap
}

func (q PriorityQueue) Len() int {
	return len(*q.elems)
}

func (q PriorityQueue) Less(i, j int) bool {
	return q.scores[(*q.elems)[i]] < q.scores[(*q.elems)[j]]
}

func (q PriorityQueue) Swap(i, j int) {
	(*q.elems)[i], (*q.elems)[j] = (*q.elems)[j], (*q.elems)[i]
	q.positions[(*q.elems)[i]], q.positions[(*q.elems)[j]] = q.positions[(*q.elems)[j]], q.positions[(*q.elems)[i]]
}

func (q PriorityQueue) Push(e interface{}) {
	q.positions[e.(Coord)] = len(*q.elems)
	*q.elems = append(*q.elems, e.(Coord))
}

func (q PriorityQueue) Pop() interface{} {
	e := (*q.elems)[len(*q.elems)-1]
	old := (*q.elems)
	old = old[:len(old)-1]
	*q.elems = old
	delete(q.positions, e)
	return e
}

func (q PriorityQueue) Position(p Coord) int {
	if pos, ok := q.positions[p]; ok {
		return pos
	}
	return -1
}

func (m CoordMap) neighbors(c Coord) []Coord {
	r := []Coord{}

	if c.x > 0 {
		r = append(r, Coord{c.x - 1, c.y})
	}
	if c.y > 0 {
		r = append(r, Coord{c.x, c.y - 1})
	}
	if _, ok := m[Coord{c.x + 1, c.y}]; ok {
		r = append(r, Coord{c.x + 1, c.y})
	}
	if _, ok := m[Coord{c.x, c.y + 1}]; ok {
		r = append(r, Coord{c.x, c.y + 1})
	}

	return r
}

func reconstructPath(cameFrom map[Coord]Coord, current Coord) []Coord {
	path := []Coord{current}

	for {
		previous, ok := cameFrom[current]

		if !ok {
			break
		}

		path = append(path, previous)
		current = previous
	}

	return path
}

func heuristic(n Coord, target Coord) int {
	return int(math.Abs(float64(n.x-target.x))) + int(math.Abs(float64(n.y-target.y)))
}

func aStarPath(rm CoordMap, start, target Coord) []Coord {
	gScore := CoordMap{start: 0}
	fScore := CoordMap{start: heuristic(start, target)}
	worklist := PriorityQueue{&[]Coord{start}, CoordMap{}, fScore}
	heap.Init(&worklist)
	cameFrom := map[Coord]Coord{}

	for len(*worklist.elems) != 0 {
		current := heap.Pop(&worklist).(Coord)

		if current == target {
			return reconstructPath(cameFrom, current)
		}

		for _, n := range rm.neighbors(current) {
			proposedScore := gScore[current] + rm[n]

			if previousScore, ok := gScore[n]; !ok || proposedScore < previousScore {
				cameFrom[n] = current
				gScore[n] = proposedScore
				fScore[n] = proposedScore + heuristic(n, target)

				if pos := worklist.Position(n); pos == -1 {
					heap.Push(&worklist, n)
				} else {
					heap.Fix(&worklist, pos)
				}
			}
		}
	}

	fmt.Println("Could not find path!")
	return []Coord{}
}

func main() {
	b, err := os.ReadFile("./day15.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(b), "\n")
	width := len(lines)
	height := len(lines[0])

	rm := make(CoordMap)
	for i, l := range lines {
		for j := 0; j < len(l); j++ {
			rm[Coord{i, j}] = int(l[j] - '0')
		}
	}

	p := aStarPath(rm, Coord{0, 0}, Coord{len(lines) - 1, len(lines[0]) - 1})

	score := 0
	for i := 0; i < len(p); i++ {
		score += rm[p[i]]
	}
	score -= rm[Coord{0, 0}]

	fmt.Println(score)

	for coord, risk := range rm {
		for i := 0; i < 5; i++ {
			for j := 0; j < 5; j++ {
				r := risk + i + j
				if r > 9 {
					r = r % 9
				}
				rm[Coord{coord.x + i*width, coord.y + j*height}] = r
			}
		}
	}

	p = aStarPath(rm, Coord{0, 0}, Coord{width*5 - 1, height*5 - 1})

	score = 0
	for i := 0; i < len(p); i++ {
		score += rm[p[i]]
	}
	score -= rm[Coord{0, 0}]

	fmt.Println(score)
}
