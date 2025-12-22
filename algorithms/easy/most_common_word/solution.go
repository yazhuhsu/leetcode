package main

import (
	"fmt"
	"strings"
)

func mostCommonWord(paragraph string, banned []string) string {
	replacer := strings.NewReplacer(
		",", " ",
		"!", " ",
		"?", " ",
		"'", " ",
		";", " ",
		".", " ",
	)
	sentences := replacer.Replace(paragraph)
	words := strings.Split(sentences, " ")

	wordMap := make(map[string]int, len(words))
	for _, word := range words {
		if word == "" {
			continue
		}
		wordMap[strings.ToLower(word)] += 1
	}

	bannedMap := make(map[string]bool, len(banned))
	for _, word := range banned {
		bannedMap[strings.ToLower(word)] = true
	}

	max, maxWord := 0, ""
	for word, count := range wordMap {
		if count > max && !bannedMap[word] {
			max = count
			maxWord = word
		}
	}

	return maxWord
}

func main() {
	fmt.Println(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", []string{"hit"}) == "ball")
	fmt.Println(mostCommonWord("a.", []string{}) == "a")
	fmt.Println(mostCommonWord("Bob. hIt, baLl", []string{"bob", "hit"}) == "ball")
}
