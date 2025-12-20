package main

import (
	"fmt"
	"sort"
	"strings"
)

func minDeletionSize(strs []string) int {
	count := 0
	for i := 0; i < len(strs[0]); i++ {
		str, orders := "", make([]string, 0, len(strs))
		for j := 0; j < len(strs); j++ {
			str += string(strs[j][i])
			orders = append(orders, string(strs[j][i]))
		}

		sort.Strings(orders)
		sortedStr := strings.Join(orders, "")

		if str != sortedStr {
			count += 1
		}
	}

	return count
}

func main() {
	fmt.Println(minDeletionSize([]string{"cba", "daf", "ghi"}) == 1)
	fmt.Println(minDeletionSize([]string{"a", "b"}) == 0)
	fmt.Println(minDeletionSize([]string{"zyx", "wvu", "tsr"}) == 3)
}
