package main

import "fmt"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}
	if p == nil || q == nil {
		return false
	}

	pOrders, qOrders := []int{}, []int{}
	traversal(p, &pOrders)
	traversal(q, &qOrders)

	for idx, _ := range pOrders {
		if pOrders[idx] != qOrders[idx] {
			return false
		}
	}

	return true
}

func traversal(node *TreeNode, orders *[]int) {
	*orders = append(*orders, node.Val)

	if node.Left != nil {
		traversal(node.Left, orders)
	} else {
		*orders = append(*orders, -100001)
	}

	if node.Right != nil {
		traversal(node.Right, orders)
	} else {
		*orders = append(*orders, -100001)
	}
}

func main() {
	p := &TreeNode{1, &TreeNode{2, nil, nil}, &TreeNode{3, nil, nil}}
	q := &TreeNode{1, &TreeNode{2, nil, nil}, &TreeNode{3, nil, nil}}
	fmt.Println(isSameTree(p, q) == true)

	p = &TreeNode{1, &TreeNode{2, nil, nil}, nil}
	q = &TreeNode{1, nil, &TreeNode{2, nil, nil}}
	fmt.Println(isSameTree(p, q) == false)

	p = &TreeNode{2, &TreeNode{2, nil, &TreeNode{2, &TreeNode{2, nil, nil}, nil}}, &TreeNode{2, nil, nil}}
	q = &TreeNode{2, &TreeNode{2, &TreeNode{2, nil, nil}, nil}, &TreeNode{2, &TreeNode{2, nil, nil}, nil}}
	fmt.Println(isSameTree(p, q) == false)
}
