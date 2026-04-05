package main

import (
	"fmt"
	"strings"
)

func judgeCircle(moves string) bool {
	movements := map[string][]int{
		"R": []int{1, 0},
		"L": []int{-1, 0},
		"U": []int{0, 1},
		"D": []int{0, -1},
	}

	sequences := strings.Split(moves, "")
	origin := []int{0, 0}
	for i := 0; i < len(moves); i++ {
		origin[0] += movements[sequences[i]][0]
		origin[1] += movements[sequences[i]][1]
	}

	if origin[0] == 0 && origin[1] == 0 {
		return true
	}

	return false
}

func main() {
	fmt.Println(judgeCircle("UD") == true)
	fmt.Println(judgeCircle("LL") == false)
	fmt.Println(judgeCircle("UDLR") == true)
	fmt.Println(judgeCircle("") == true)
}
