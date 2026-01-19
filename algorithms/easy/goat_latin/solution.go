package main

import (
	"fmt"
	"strings"
)

func toGoatLatin(sentence string) string {
	vowels := []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
	words := strings.Split(sentence, " ")

	final := ""
	for idx, word := range words {
		if in(rune(word[0]), vowels) {
			final += word + "ma"
		} else {
			final += string(word[1:]) + string(word[0]) + "ma"
		}

		for _ = range idx + 1 {
			final += "a"
		}

		if idx != len(words)-1 {
			final += " "
		}
	}

	return final
}

func in(r rune, rs []rune) bool {
	for idx, _ := range rs {
		if rs[idx] == r {
			return true
		}
	}

	return false
}

func main() {
	fmt.Println(toGoatLatin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
	fmt.Println(toGoatLatin("The quick brown fox jumped over the lazy dog") == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")
}
