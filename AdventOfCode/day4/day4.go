package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strings"
)

func part1WordProcessor(word string) string {
	return word
}

func part2WordProcessor(word string) string {
	return getSortedWord(word)
}

// splits the word on each letter, sorts the array, and concatenates it
// comparing "sorted words" is easy anagram detection
func getSortedWord(word string) string {
	letters := strings.Split(word, "")
	sort.Strings(letters)
	return strings.Join(letters, "")
}

func validatePassphraseListWithValidator(passphraseList []string, wordProcessor func(string) string) {
	total := 0

validationLoop:
	for _, passphrase := range passphraseList {
		words := strings.Split(passphrase, " ")
		encounteredWords := map[string]bool{}

		for _, word := range words {
			processed := wordProcessor(word)

			if encounteredWords[processed] == true {
				continue validationLoop
			}

			encounteredWords[processed] = true
		}

		total++
	}

	fmt.Printf("%d\n", total)
}

func main() {
	data, err := ioutil.ReadFile("/tmp/aoc_day4.txt")
	if err != nil {
		panic(err)
	}

	list := strings.Split(strings.TrimSpace(string(data)), "\n")
	validatePassphraseListWithValidator(list, part1WordProcessor)
	validatePassphraseListWithValidator(list, part2WordProcessor)
}
