package main

import (
	"fmt"
	"strings"
)

func numberOfSpecialChars(word string) int {
	upperCase, lowerCase := map[string]int{}, map[string]int{}
	for i := 0; i < len(word); i++ {
		w := string(word[i])
		if strings.ToUpper(w) == w {
			upperCase[w] += 1
			continue
		}
		lowerCase[w] += 1
	}

	count := 0
	for w := range upperCase {
		if _, exist := lowerCase[strings.ToLower(w)]; exist {
			count += 1
		}
	}

	return count
}

func main() {
	fmt.Println(numberOfSpecialChars("aaAbcBC") == 3)
	fmt.Println(numberOfSpecialChars("abc") == 0)
	fmt.Println(numberOfSpecialChars("aA") == 1)
	fmt.Println(numberOfSpecialChars("AbBCc") == 2)
	fmt.Println(numberOfSpecialChars("") == 0)
}
