package main

import (
	"fmt"
	"strings"
)

func reverseWords(s string) string {
	reversed := ""
	words := strings.Split(s, " ")

	for idx, word := range words {
		for widx := 0; widx < len(word); widx++ {
			reversed += string(word[len(word)-widx-1])
		}

		if idx < len(words)-1 {
			reversed += " "
		}
	}

	return reversed
}

func main() {
	fmt.Println(reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc")
	fmt.Println(reverseWords("Mr Ding") == "rM gniD")
}
