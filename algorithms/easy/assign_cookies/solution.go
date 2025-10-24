package main

import (
	"fmt"
	"slices"
)

func findContentChildren(g []int, s []int) int {
	slices.Sort(g)
	slices.Sort(s)

	successCount, failedCount := 0, 0
	success := false
	for _ = range g {
		success = false
		failedCount = 0
		for j := range s {
			if s[j] >= g[0] {
				success = true
				successCount += 1
				s = append(s[:j], s[j+1:]...)
				break
			} else {
				failedCount += 1
			}
		}
		g = append(g[1:])

		if !success && failedCount == len(s) {
			break
		}

		if len(g) == 0 {
			break
		}
	}
	return successCount
}

func main() {
	fmt.Println(findContentChildren([]int{1, 2, 3}, []int{1, 1}) == 1)
	fmt.Println(findContentChildren([]int{1, 2}, []int{1, 2, 3}) == 2)
}
