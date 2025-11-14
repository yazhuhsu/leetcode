package main

import (
	"fmt"
	"reflect"
)

func constructRectangle(area int) []int {
	w, l, diff := 0, 0, area
	for i := 1; i <= area; i++ {
		if area%i == 0 {
			j := area / i
			if j-i <= diff && j-i >= 0 {
				w = i
				l = j
				diff = j - i
			}
		}
	}

	return []int{l, w}
}

func main() {
	fmt.Println(reflect.DeepEqual(constructRectangle(37), []int{37, 1}))
	fmt.Println(reflect.DeepEqual(constructRectangle(122122), []int{427, 286}))
	fmt.Println(reflect.DeepEqual(constructRectangle(1), []int{1, 1}))
}
