package main

import (
	"fmt"
	"unicode"
)

func reverseOnlyLetters(s string) string {
	letters := ""
	for _, ch := range s {
		if unicode.IsLetter(ch) {
			letters += string(ch)
		}
	}

	idx, reversed := 0, ""
	for _, ch := range s {
		if unicode.IsLetter(ch) {
			reversed += string(letters[len(letters)-idx-1])
			idx += 1
			continue
		}
		reversed += string(ch)
	}

	return reversed
}

func main() {
	fmt.Println(reverseOnlyLetters("ab-cd") == "dc-ba")
	fmt.Println(reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba")
	fmt.Println(reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!")
}
