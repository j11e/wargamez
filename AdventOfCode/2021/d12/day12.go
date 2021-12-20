package main

import (
"os"
"strings"
)

func main() {
b, err := os.ReadFile("./day12_test.txt")
if err != nil {
panic(err)
}
lines := strings.Split(string(b), "\n")


}

