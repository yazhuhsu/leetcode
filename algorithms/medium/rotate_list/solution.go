package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func buildList(vals []int) *ListNode {
	if len(vals) == 0 {
		return nil
	}
	head := &ListNode{Val: vals[0]}
	cur := head
	for _, v := range vals[1:] {
		cur.Next = &ListNode{Val: v}
		cur = cur.Next
	}
	return head
}

func listVals(head *ListNode) []int {
	vals := []int{}
	for head != nil {
		vals = append(vals, head.Val)
		head = head.Next
	}
	return vals
}

func equal(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil {
		return head
	}

	origin := []int{}
	for head.Next != nil {
		origin = append(origin, head.Val)
		head = head.Next
	}
	origin = append(origin, head.Val)

	if k > len(origin) {
		k = k % len(origin)
	}

	new := []int{}
	new = append(new, origin[len(origin)-k:]...)
	new = append(new, origin[:len(origin)-k]...)

	head.Val = new[len(new)-1]
	for idx := len(new) - 2; idx >= 0; idx-- {
		head = &ListNode{Val: new[idx], Next: head}
	}

	return head
}

func main() {
	fmt.Println(equal(listVals(rotateRight(buildList([]int{1, 2, 3, 4, 5}), 2)), []int{4, 5, 1, 2, 3}))
	fmt.Println(equal(listVals(rotateRight(buildList([]int{0, 1, 2}), 4)), []int{2, 0, 1}))
	fmt.Println(equal(listVals(rotateRight(buildList([]int{1, 2}), 0)), []int{1, 2}))
	fmt.Println(equal(listVals(rotateRight(buildList([]int{1}), 5)), []int{1}))
	fmt.Println(rotateRight(nil, 3) == nil)
}
