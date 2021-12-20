#!/usr/bin/env zsh

lastDay=`find . -type d | awk -F'd' '{print $2}' | sort -n | tail -1`
newDay="$((lastDay+1))"

mkdir "d${newDay}"
cd "d${newDay}"
touch "day${newDay}.go"
touch "day${newDay}.txt"
touch "day${newDay}_test.txt"

cat > "day${newDay}.go" <<- EOF
package main

import (
	"os"
	"strings"
)

func main() {
	b, err := os.ReadFile("./day${newDay}_test.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(b), "\n")


}

EOF
