package main

import "fmt"

func findJudge(n int, trust [][]int) int {
	if len(trust) == n {
		return -1
	}
	if len(trust) == 0 && n == 1 {
		return 1
	}

	judgeMap := make(map[int][]int, n)
	trustMap := make(map[int][]int, n)
	for _, trusts := range trust {
		trustMap[trusts[0]] = append(trustMap[trusts[0]], trusts[1])
		judgeMap[trusts[1]] = append(judgeMap[trusts[1]], trusts[0])
	}

	for k, v := range judgeMap {
		if len(v) == n-1 {
			trusts := trustMap[k]
			if len(trusts) == 0 {
				return k
			}
		}
	}

	return -1
}

func main() {
	fmt.Println(findJudge(2, [][]int{{1, 2}}) == 2)
	fmt.Println(findJudge(3, [][]int{{1, 3}, {2, 3}}) == 3)
	fmt.Println(findJudge(3, [][]int{{1, 3}, {2, 3}, {3, 1}}) == -1)
}
