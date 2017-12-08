package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strings"
)

type validatorInterface interface {
	addWord(string) bool
	reset()
}

type part1Validator struct {
	encounteredWords map[string]bool
}

type part2Validator struct {
	words []string
}

func (state *part1Validator) addWord(word string) bool {
	if state.encounteredWords[word] == true {
		return false
	}

	state.encounteredWords[word] = true
	return true
}

func (state *part1Validator) reset() {
	state.encounteredWords = map[string]bool{}
}

func (state *part2Validator) addWord(word string) bool {
	for _, knownWord := range state.words {
		if isAnagram(knownWord, word) {
			return false
		}
	}

	state.words = append(state.words, word)
	return true
}

func (state *part2Validator) reset() {
	state.words = []string{}
}

// splits words on each letter, sorts the array, and compares the new "sorted words"
// might be more performant with slices of runes, but at least with strings I
// don't have to implement the sort.Interface for runes ¯\_(ツ)_/¯
func isAnagram(word string, otherWord string) bool {
	letters := strings.Split(word, "")
	otherLetters := strings.Split(otherWord, "")

	sort.Strings(letters)
	sort.Strings(otherLetters)

	return strings.Join(letters, "") == strings.Join(otherLetters, "")
}

func validatePassphraseListWithValidator(passphraseList []string, validator validatorInterface) {
	total := 0

validationLoop:
	for _, passphrase := range passphraseList {
		words := strings.Split(passphrase, " ")
		validator.reset()

		for _, word := range words {
			success := validator.addWord(word)

			if !success {
				continue validationLoop
			}
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
	validatePassphraseListWithValidator(list, &part1Validator{map[string]bool{}})
	validatePassphraseListWithValidator(list, &part2Validator{[]string{}})
}
