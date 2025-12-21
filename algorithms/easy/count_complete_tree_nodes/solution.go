package main

import "fmt"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func countNodes(root *TreeNode) int {
	if root == nil {
		return 0
	}

	counter := 0
	count(root, &counter)

	return counter
}

func count(node *TreeNode, counter *int) {
	if isComplete(node) {
		*counter += 1
	}

	if node.Left != nil {
		count(node.Left, counter)
	}

	if node.Right != nil {
		count(node.Right, counter)
	}

}

func isComplete(node *TreeNode) bool {
	if node.Left != nil && node.Right != nil {
		return true
	}
	if node.Left == nil && node.Right == nil {
		return true
	}
	if node.Left != nil && node.Right == nil {
		return true
	}

	return false
}

func main() {
	fmt.Println(countNodes(nil) == 0)
	fmt.Println(countNodes(&TreeNode{Val: 1, Left: &TreeNode{Val: 2, Left: &TreeNode{Val: 4, Left: nil, Right: nil}, Right: &TreeNode{Val: 5, Left: nil, Right: nil}}, Right: &TreeNode{Val: 3, Left: &TreeNode{Val: 6, Left: nil, Right: nil}, Right: nil}}) == 6)
	fmt.Println(countNodes(&TreeNode{Val: 1, Left: nil, Right: nil}) == 1)

}
