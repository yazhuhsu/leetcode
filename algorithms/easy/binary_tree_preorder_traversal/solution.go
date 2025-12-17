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

func preorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	if root.Left == nil && root.Right == nil {
		return []int{root.Val}
	}

	orders := []int{}
	preorder(root, &orders)

	return orders
}

func preorder(root *TreeNode, orders *[]int) {
	*orders = append(*orders, root.Val)

	if root.Left != nil {
		preorder(root.Left, orders)
	}

	if root.Right != nil {
		preorder(root.Right, orders)
	}
}

func main() {
	fmt.Println(reflect.DeepEqual(preorderTraversal(&TreeNode{Val: 1, Left: nil, Right: &TreeNode{Val: 2, Left: &TreeNode{Val: 3, Left: nil, Right: nil}, Right: nil}}), []int{1, 2, 3}))
	fmt.Println(reflect.DeepEqual(preorderTraversal(&TreeNode{Val: 1, Left: &TreeNode{Val: 2, Left: &TreeNode{Val: 4, Left: nil, Right: nil}, Right: &TreeNode{Val: 5, Left: &TreeNode{Val: 6, Left: nil, Right: nil}, Right: &TreeNode{Val: 7, Left: nil, Right: nil}}}, Right: &TreeNode{Val: 3, Left: nil, Right: &TreeNode{Val: 8, Left: &TreeNode{Val: 9, Left: nil, Right: nil}, Right: nil}}}), []int{1, 2, 4, 5, 6, 7, 3, 8, 9}))
	fmt.Println(reflect.DeepEqual(preorderTraversal(nil), []int{}))
	fmt.Println(reflect.DeepEqual(preorderTraversal(&TreeNode{Val: 1, Left: nil, Right: nil}), []int{1}))
}
