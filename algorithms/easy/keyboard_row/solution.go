package main

import (
	"fmt"
	"reflect"
	"slices"
	"strings"
)

func findWords(words []string) []string {
	rows := map[int][]string{
		1: {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"},
		2: {"a", "s", "d", "f", "g", "h", "j", "k", "l", "A", "S", "D", "F", "G", "H", "J", "K", "L"},
		3: {"z", "x", "c", "v", "b", "n", "m", "Z", "X", "C", "V", "B", "N", "M"},
	}

	outputs := make([]string, 0, len(words))
	for _, word := range words {
		ss := strings.Split(word, "")
		row1, row2, row3 := 0, 0, 0
		for _, s := range ss {
			if slices.Contains(rows[1], s) {
				row1 += 1
			} else if slices.Contains(rows[2], s) {
				row2 += 1
			} else if slices.Contains(rows[3], s) {
				row3 += 1
			}
		}

		if row1 == len(word) || row2 == len(word) || row3 == len(word) {
			outputs = append(outputs, word)
		}
	}

	return outputs
}

func main() {
	fmt.Println(reflect.DeepEqual(findWords([]string{"Hello", "Alaska", "Dad", "Peace"}), []string{"Alaska", "Dad"}))
	fmt.Println(reflect.DeepEqual(findWords([]string{"omk"}), []string{}))
	fmt.Println(reflect.DeepEqual(findWords([]string{"adsdf", "sfd"}), []string{"adsdf", "sfd"}))
}
