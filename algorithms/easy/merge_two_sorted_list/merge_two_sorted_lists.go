package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// ListNode definition
type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	result := &ListNode{}
	l3 := &ListNode{}

	if l1 == nil && l2 == nil {
		return nil
	}

	if l1 == nil && l2 != nil {
		return l2
	}

	if l1 != nil && l2 == nil {
		return l1
	}
	if l1.Val <= l2.Val {
		l3 = l1
		l1 = l1.Next
	} else {
		l3 = l2
		l2 = l2.Next
	}

	result = l3

	for l1 != nil && l2 != nil {
		if l1.Val <= l2.Val {
			l3.Next = l1
			l1 = l1.Next
		} else {
			l3.Next = l2
			l2 = l2.Next
		}
		l3 = l3.Next
	}

	for l1 != nil {
		l3.Next = l1
		l1 = l1.Next
		l3 = l3.Next
	}

	for l2 != nil {
		l3.Next = l2
		l2 = l2.Next
		l3 = l3.Next
	}

	return result
}

func main() {}
