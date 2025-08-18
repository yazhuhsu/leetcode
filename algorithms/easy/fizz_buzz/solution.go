package main

import (
	"fmt"
	"strconv"
)

func fizzBuzz(n int) []string {
	output := make([]string, 0, n)
	for i := 1; i <= n; i++ {
		s := ""
		if i%3 == 0 {
			s += "Fizz"
		}
		if i%5 == 0 {
			s += "Buzz"
		}

		if s == "" {
			s += strconv.Itoa(i)
		}

		output = append(output, s)
	}

	return output
}

func main() {
	outputs := map[int][]string{
		3:  {"1", "2", "Fizz"},
		5:  {"1", "2", "Fizz", "4", "Buzz"},
		15: {"1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"},
	}

	for n, output := range outputs {
		answers := fizzBuzz(n)
		for i, answer := range answers {
			if output[i] != answer {
				fmt.Println("n =", n, "Wrong! ")
				fmt.Println("output: ", output, " answer: ", answer)
				break
			}
		}

		fmt.Println("n =", n, " Correct! ")
	}
}
