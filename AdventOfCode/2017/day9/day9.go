package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

type node struct {
	nodeType string // "group" or "garbage"
	children []*node
	parent   *node
}

func parse(streamData string) (root *node) {
	nextCharDisabled := false

	// the first character always starts a group; easy way to get a pointer to
	// the root right away
	currentNode := &node{"group", []*node{}, nil}
	root = currentNode
	currentDepth := 1
	currentState := "group" // will be either "group" or "garbage"

	for i := 1; i < len(streamData); i++ {
		curCharacter := streamData[i]

		if nextCharDisabled == true {
			nextCharDisabled = false
			continue
		}

		if currentState == "garbage" {
			switch curCharacter {
			case '>':
				currentNode = currentNode.parent
				currentDepth--
				currentState = currentNode.nodeType
			case '!':
				nextCharDisabled = true
			}
		} else {
			switch curCharacter {
			case '{':
				newNode := &node{"group", []*node{}, currentNode}
				currentNode = newNode
				currentDepth++
				currentState = "group"
			case '}':
				currentNode = currentNode.parent
				currentDepth--
			case '<':
				newNode := &node{"garbage", []*node{}, currentNode}
				currentDepth++
				currentState = "garbage"
				currentNode = newNode
			case '>':
				// nothing to do: > is a legit character in a group
			case '!':
				nextCharDisabled = true
			default:
				// noth'n to do
			}
		}

	}

	return root
}

func main() {
	challenge, err := ioutil.ReadFile("/tmp/aoc_day9.txt")
	if err != nil {
		panic(err)
	}

	streamData := strings.TrimSpace(string(challenge))

	score := parse(streamData)

	fmt.Printf("Total score: %d\n", score)
}
