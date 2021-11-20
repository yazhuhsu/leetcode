package main

import (
	"strings"
)

func longestCommonPrefix(strs []string) string {

	if len(strs) == 0 {
		return ""
	}
	if len(strs) == 1 {
		return strs[0]
	}

	minSize := int(^uint(0) >> 1)
	minPos := 0

	for i := 0; i < len(strs); i++ {
		if len(strs[i]) < minSize {
			minSize = len(strs[i])
			minPos = i
		}
	}

	minStrs := strings.Split(strs[minPos], "")

	same := true
	pos := 0
	for j := 0; j < minSize; j++ {
		for k := 0; k < len(strs); k++ {
			m := strings.Split(strs[k], "")
			if m[j] != minStrs[j] {
				same = false
			}
		}
		if !same {
			break
		}
		pos++
	}

	result := ""
	for l := 0; l < pos; l++ {
		result += minStrs[l]
	}

	return result
}

func main() {
}
