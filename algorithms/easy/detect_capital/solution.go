package main

import (
	"fmt"
	"strings"
)

func detectCapitalUse(word string) bool {
	first, upper, lower := 0, 0, 0
	for idx, w := range word {
		if strings.ToUpper(string(w)) == string(w) {
			upper += 1
			if idx == 0 {
				first += 1
			}
		} else {
			lower += 1
		}
	}

	if first == 1 && upper == 1 {
		return true
	}
	if upper == len(word) || lower == len(word) {
		return true
	}

	return false
}

func main() {
	fmt.Println(detectCapitalUse("USA") == true)
	fmt.Println(detectCapitalUse("FlaG") == false)
}
