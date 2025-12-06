package main

import (
	"fmt"
	"strconv"
)

func calPoints(operations []string) int {
	scores := make([]int, 0, len(operations))
	for _, operation := range operations {
		switch operation {
		case "+":
			scores = append(scores, scores[len(scores)-2]+scores[len(scores)-1])
		case "C":
			scores = scores[:len(scores)-1]
		case "D":
			scores = append(scores, scores[len(scores)-1]*2)
		default:
			score, _ := strconv.Atoi(operation)
			scores = append(scores, score)
		}
	}

	totalScore := 0
	for _, score := range scores {
		totalScore += score
	}

	return totalScore
}

func main() {
	fmt.Println(calPoints([]string{"5", "2", "C", "D", "+"}) == 30)
	fmt.Println(calPoints([]string{"5", "-2", "4", "C", "D", "9", "+", "+"}) == 27)
	fmt.Println(calPoints([]string{"1", "C"}) == 0)
}
