package main

import (
	"fmt"
	"reflect"
)

func largeGroupPositions(s string) [][]int {
	groups := make([][]int, 0)
	letter, start, end := "", -1, -1
	for idx, l := range s {
		if string(l) == letter {
			end = idx
		} else {
			if end-start+1 >= 3 {
				groups = append(groups, []int{start, end})
			}
			letter = string(l)
			start, end = idx, idx
		}
	}

	if end == len(s)-1 && end-start+1 >= 3 {
		groups = append(groups, []int{start, end})
	}

	return groups
}

func main() {
	fmt.Println(reflect.DeepEqual(largeGroupPositions("abbxxxxzzy"), [][]int{{3, 6}}))
	fmt.Println(reflect.DeepEqual(largeGroupPositions("abc"), [][]int{}))
	fmt.Println(reflect.DeepEqual(largeGroupPositions("abcdddeeeeaabbbcd"), [][]int{{3, 5}, {6, 9}, {12, 14}}))
	fmt.Println(reflect.DeepEqual(largeGroupPositions("aaa"), [][]int{{0, 2}}))
}
