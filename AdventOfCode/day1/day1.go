package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func addIfDigitEqualsWithOffset(challenge string, offset int) {
	total := 0
	lenChallenge := len(challenge)

	for i := 0; i < lenChallenge; i++ {
		if challenge[i] == challenge[(i+offset)%lenChallenge] {
			value, err := strconv.Atoi(string(challenge[i]))
			if err != nil {
				panic(err)
			}

			total += value
		}
	}

	fmt.Println(total)
}

func main() {
	var (
		challenge string
	)

	data, err := ioutil.ReadFile("/tmp/aoc_day1.txt")
	if err != nil {
		panic(err)
	}

	challenge = strings.TrimSpace(string(data))

	addIfDigitEqualsWithOffset(challenge, 1)
	addIfDigitEqualsWithOffset(challenge, len(challenge)/2)
}
