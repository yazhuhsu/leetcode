package main

import (
	"fmt"
	"reflect"
)

func reverseString(s []byte) {
	length := len(s) / 2
	if length%2 == 1 {
		length = (len(s) + 1) / 2
	}

	for i := 0; i < length; i++ {
		s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
	}

	return
}

func main() {
	s := []byte{'h', 'e', 'l', 'l', 'o'}
	reverseString(s)
	fmt.Println(reflect.DeepEqual(s, []byte{'o', 'l', 'l', 'e', 'h'}))

	s = []byte{'H', 'a', 'n', 'n', 'a', 'h'}
	reverseString(s)
	fmt.Println(reflect.DeepEqual(s, []byte{'h', 'a', 'n', 'n', 'a', 'H'}))
}
