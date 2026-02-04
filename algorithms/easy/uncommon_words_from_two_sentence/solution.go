package main

import (
	"fmt"
	"reflect"
	"strings"
)

func uncommonFromSentences(s1 string, s2 string) []string {
	words1 := strings.Split(s1, " ")
	words2 := strings.Split(s2, " ")

	wordMap := make(map[string]int, len(words1)+len(words2))
	for _, word := range append(words1, words2...) {
		if _, ok := wordMap[word]; !ok {
			wordMap[word] = 1
			continue
		}

		wordMap[word] += 1
	}

	uncommonWords := make([]string, 0, len(words1)+len(words2))
	for k, v := range wordMap {
		if v == 1 {
			uncommonWords = append(uncommonWords, k)
		}
	}

	return uncommonWords
}

func main() {
	fmt.Println(reflect.DeepEqual(uncommonFromSentences("this apple is sweet", "this apple is sour"), []string{"sweet", "sour"}))
	fmt.Println(reflect.DeepEqual(uncommonFromSentences("apple apple", "banana"), []string{"banana"}))
}
