package main

import (
	"fmt"
	"os"
	"strings"
)

type CaveNetwork map[string][]string

type Path struct {
	caves  []string
	smalls map[string]int
}

func small(c string) bool {
	return c[0] >= 'a'
}

func indexOf(a []string, s string) int {
	for i, v := range a {
		if v == s {
			return i
		}
	}

	return -1
}

func (p Path) canAccept(c string) bool {
	if c == "start" {
		return false
	}

	if small(c) {
		if _, ok := p.smalls[c]; ok {
			for _, s := range p.smalls {
				if s > 1 {
					return false
				}
			}
		}
	}
	return true
}

func main() {
	b, err := os.ReadFile("./day12.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(b), "\n")

	cn := CaveNetwork{}

	for _, l := range lines {
		cs := strings.Split(l, "-")

		if _, ok := cn[cs[0]]; !ok {
			cn[cs[0]] = []string{}
		}
		cn[cs[0]] = append(cn[cs[0]], cs[1])

		if _, ok := cn[cs[1]]; !ok {
			cn[cs[1]] = []string{}
		}
		cn[cs[1]] = append(cn[cs[1]], cs[0])
	}

	fmt.Println(cn)
	paths := buildPathsPart1(cn, []string{"start"})

	fmt.Println("There are ", len(paths), " paths in the network")

	paths2 := buildPathsPart2(cn, Path{caves: []string{"start"}})

	fmt.Println("There are ", len(paths2), " paths in the network with a single small cave repeated")
}

func buildPathsPart1(network CaveNetwork, curPath []string) [][]string {
	paths := [][]string{}

	last := curPath[len(curPath)-1]
	if last == "end" {
		return append(paths, curPath)
	}

	for _, n := range network[last] {
		if small(n) && indexOf(curPath, n) != -1 {
			continue
		}

		// this code actually has a bug: some paths returned do not end with "end"
		// because (I think) of side-effects of append(). But the count is correct,
		// and that's all I need
		paths = append(paths, buildPathsPart1(network, append(curPath, n))...)
	}

	return paths
}

func buildPathsPart2(network CaveNetwork, curPath Path) []Path {
	paths := []Path{}

	last := curPath.caves[len(curPath.caves)-1]
	if last == "end" {
		return append(paths, curPath)
	}

	for _, n := range network[last] {
		if !curPath.canAccept(n) {
			continue
		}

		newSmalls := map[string]int{}
		for k, v := range curPath.smalls {
			newSmalls[k] = v
		}
		if small(n) {
			if _, ok := newSmalls[n]; !ok {
				newSmalls[n] = 0
			}
			newSmalls[n] += 1
		}
		newCaves := []string{}
		newCaves = append(newCaves, curPath.caves...)
		newCaves = append(newCaves, n)
		newPath := Path{caves: newCaves, smalls: newSmalls}

		paths = append(paths, buildPathsPart2(network, newPath)...)
	}

	return paths
}
