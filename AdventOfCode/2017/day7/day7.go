package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type node struct {
	name          string
	weight        int
	subtreeWeight int
	childrenNames []string // useful only for the initial parsing of the data
	childrenNodes []*node
	parent        *node
}

func getTree(treeData []string) *node {
	nodes := map[string]*node{}

	// create map of nodes
	for _, nodeData := range treeData {
		// "jfmuzo (164) -> istoj, jyzrmnp"
		splitData := strings.Split(nodeData, " ")

		node := &node{}
		node.name = splitData[0]

		splitData[1] = splitData[1][1 : len(splitData[1])-1]
		weight, convErr := strconv.Atoi(splitData[1])
		if convErr != nil {
			panic(convErr)
		}
		node.weight = weight

		if len(splitData) > 3 {
			childrenStr := strings.Join(splitData[3:], "")
			node.childrenNames = strings.Split(childrenStr, ",")
		}

		nodes[node.name] = node
	}

	// update map of nodes to include parents and form tree structure
	// by setting childrenNodes properly
	for name, node := range nodes {
		for _, childName := range node.childrenNames {
			child := nodes[childName]
			child.parent = nodes[name]

			node.childrenNodes = append(node.childrenNodes, nodes[childName])
		}
	}

	// find the tree's root now
	var root *node
	for _, node := range nodes {
		if node.parent == nil {
			root = node
		}
	}

	// update the tree to contain weight info now
	computeSubtreeWeight(root)

	return root
}

// set each node's subtree weight = node.weight + sum of children subtree weights
func computeSubtreeWeight(node *node) {
	node.subtreeWeight = node.weight

	for _, child := range node.childrenNodes {
		computeSubtreeWeight(child)
		node.subtreeWeight += child.subtreeWeight
	}
}

// starting at root, follow the imbalanced subtowers until all subtowers are balanced
// the root of the top-level imbalanced subtree is the root of all evil
func findImbalance(root *node) *node {
	// less than 2 children? there cannot be an imbalance
	if len(root.childrenNodes) < 2 {
		return root
	}

	// find the imbalanced subtower: group the children by subtree weight
	weightOccurences := map[int][]*node{}
	for _, child := range root.childrenNodes {
		if _, ok := weightOccurences[child.subtreeWeight]; !ok {
			weightOccurences[child.subtreeWeight] = []*node{child}
		} else {
			weightOccurences[child.subtreeWeight] = append(weightOccurences[child.subtreeWeight], child)
		}
	}

	// which weight only appears once?
	for _, children := range weightOccurences {
		if len(children) == 1 {
			// note: if there are only two children, both imbalanced subtrees can
			// be considered as the root of the problem
			return findImbalance(children[0])
		}
	}

	// all subtowers balanced: this tree is balanced
	return root
}

func main() {
	challenge, err := ioutil.ReadFile("/tmp/aoc_day7.txt")
	if err != nil {
		panic(err)
	}

	treeData := strings.Split(strings.TrimSpace(string(challenge)), "\n")

	tree := getTree(treeData)
	fmt.Printf("The tree's root node's name is %s\n", tree.name)

	rootOfAllEvil := findImbalance(tree)

	// the weight the root of all evil should be for the tree to be balanced is
	// its current weight, plus the difference with any of its balanced siblings
	var balancedSibling *node
	for _, sibling := range rootOfAllEvil.parent.childrenNodes {
		if sibling != rootOfAllEvil {
			balancedSibling = sibling
			break
		}
	}

	requiredWeight := rootOfAllEvil.weight + (balancedSibling.subtreeWeight - rootOfAllEvil.subtreeWeight)

	fmt.Printf("Root of all evil is %s with a weight of %d (should be %d)\n", rootOfAllEvil.name, rootOfAllEvil.weight, requiredWeight)
}
