package main

import (
	"fmt"
	"strings"
)

func canBeTypedWords(text string, brokenLetters string) int {
	words := strings.Split(text, " ")

	count, exist := 0, false
	for _, word := range words {
		for _, letter := range word {
			for _, brokenLetter := range brokenLetters {
				if letter == brokenLetter {
					count += 1
					exist = true
					break
				}
			}
			if exist {
				break
			}
		}
		exist = false
	}

	return len(words) - count
}

func main() {
	cases := [][]string{
		{"hello world", "ad"},
		{"leet code", "lt"},
		{"leetcode", "e"},
	}

	answers := []int{1, 1, 0}

	for idx, v := range cases {
		fmt.Println(canBeTypedWords(v[0], v[1]) == answers[idx])
	}
}
