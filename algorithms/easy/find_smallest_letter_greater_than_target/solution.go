package main

import "fmt"

func nextGreatestLetter(letters []byte, target byte) byte {
	for _, letter := range letters {
		if letter > target {
			return letter
		}
	}

	return letters[0]
}

func main() {
	fmt.Println(nextGreatestLetter([]byte{'c', 'f', 'j'}, 'a') == 'c')
	fmt.Println(nextGreatestLetter([]byte{'c', 'f', 'j'}, 'c') == 'f')
}
