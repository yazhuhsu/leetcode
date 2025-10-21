package main

import "fmt"

func countSegments(s string) int {

	word, words := "", make([]string, 0, len(s))
	for _, r := range s {
		if string(r) == " " {
			if word != "" {
				words = append(words, word)
				word = ""
			}
			continue
		}

		word += string(r)
	}

	if word != "" {
		words = append(words, word)
	}

	return len(words)
}

func main() {
	fmt.Println(countSegments("Hello, my name is John") == 5)
	fmt.Println(countSegments("Hello") == 1)
}
