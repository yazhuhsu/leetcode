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

func postorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	if root.Left == nil && root.Right == nil {
		return []int{root.Val}
	}

	orders := []int{}
	postorder(root, &orders)

	return orders
}

func postorder(root *TreeNode, orders *[]int) {
	if root.Left != nil {
		postorder(root.Left, orders)
	}

	if root.Right != nil {
		postorder(root.Right, orders)
	}

	*orders = append(*orders, root.Val)
}

func main() {
	fmt.Println(reflect.DeepEqual(postorderTraversal(&TreeNode{Val: 1, Left: nil, Right: &TreeNode{Val: 2, Left: &TreeNode{Val: 3, Left: nil, Right: nil}, Right: nil}}), []int{3, 2, 1}))
	fmt.Println(reflect.DeepEqual(postorderTraversal(&TreeNode{Val: 1, Left: &TreeNode{Val: 2, Left: &TreeNode{Val: 4, Left: nil, Right: nil}, Right: &TreeNode{Val: 5, Left: &TreeNode{Val: 6, Left: nil, Right: nil}, Right: &TreeNode{Val: 7, Left: nil, Right: nil}}}, Right: &TreeNode{Val: 3, Left: nil, Right: &TreeNode{Val: 8, Left: &TreeNode{Val: 9, Left: nil, Right: nil}, Right: nil}}}), []int{4, 6, 7, 5, 2, 9, 8, 3, 1}))
	fmt.Println(reflect.DeepEqual(postorderTraversal(nil), []int{}))
	fmt.Println(reflect.DeepEqual(postorderTraversal(&TreeNode{Val: 1, Left: nil, Right: nil}), []int{1}))
}
