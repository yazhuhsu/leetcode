package main

import (
	"fmt"
	"reflect"
)

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	orders := []int{}
	traversal(root, &orders)

	return orders
}

func traversal(node *TreeNode, orders *[]int) {
	if node.Left != nil {
		traversal(node.Left, orders)
	}

	*orders = append(*orders, node.Val)

	if node.Right != nil {
		traversal(node.Right, orders)
	}
}

func main() {
	root := &TreeNode{1, nil, &TreeNode{2, &TreeNode{3, nil, nil}, nil}}
	fmt.Println(reflect.DeepEqual(inorderTraversal(root), []int{1, 3, 2}))
}
