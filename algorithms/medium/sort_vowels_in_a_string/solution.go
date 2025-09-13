package main

import (
	"fmt"
	"sort"
	"strings"
)

func sortVowels(s string) string {
	if len(s) == 1 {
		return s
	}

	vowels := []rune{
		'a', 'e', 'i', 'o', 'u',
		'A', 'E', 'I', 'O', 'U',
	}
	vInS := make([]string, 0, len(s))
	for _, v := range s {
		for _, r := range vowels {
			if v == r {
				vInS = append(vInS, string(v))
			}
		}
	}

	sort.Slice(vInS, func(i, j int) bool {
		return vInS[i] < vInS[j]
	})

	if len(vInS) == len(s) {
		return strings.Join(vInS, "")
	}

	output, idx, exist := "", 0, false
	for _, v := range s {
		for _, r := range vowels {
			if v == r {
				output += vInS[idx]
				idx += 1
				exist = true
				continue
			}
		}
		if !exist {
			output += string(v)
		}
		exist = false
	}

	return output
}

func main() {
	fmt.Println(sortVowels("lEetcOde") == "lEOtcede")
	fmt.Println(sortVowels("lYmpH") == "lYmpH")
	fmt.Println(sortVowels("u") == "u")
	fmt.Println(sortVowels("OA") == "AO")
}
