package main

import (
	"fmt"
	"reflect"
	"sort"
)

func threeSum(nums []int) [][]int {

	numMap := make(map[int]int, len(nums))
	answers := make([][]int, 0, len(nums))

	for _, num := range nums {
		numMap[num] += 1
	}
	if numMap[0] == len(nums) {
		return [][]int{{0, 0, 0}}
	}

	for idx, num := range nums {
		for jidx, jnum := range nums {
			answer := []int{}
			if idx <= jidx {
				continue
			}

			count := 1
			sum := num + jnum

			if 0-sum == num {
				count += 1
			}
			if 0-sum == jnum {
				count += 1
			}

			if numMap[0-sum] >= count {
				answer = append(answer, num, jnum, 0-sum)

				sort.Ints(answer)
				exists := false
				for _, ans := range answers {
					if answer[0] == ans[0] && answer[1] == ans[1] && answer[2] == ans[2] {
						exists = true
						break
					}
				}

				if !exists {
					answers = append(answers, answer)
				}
			}
		}
	}

	return answers
}

func main() {
	fmt.Println(reflect.DeepEqual(threeSum([]int{-1, 0, 1, 2, -1, -4}), [][]int{{-1, 0, 1}, {-1, -1, 2}}))
	fmt.Println(reflect.DeepEqual(threeSum([]int{0, 1, 1}), [][]int{}))
	fmt.Println(reflect.DeepEqual(threeSum([]int{0, 0, 0}), [][]int{{0, 0, 0}}))
}
