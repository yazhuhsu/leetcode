package main

import "fmt"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return false
	}
	if root.Left == nil && root.Right == nil {
		return true
	} else if root.Left == nil || root.Right == nil {
		return false
	}

	left, right := []int{}, []int{}
	preorder(root.Left, &left)
	levelorder(root.Right, &right)

	for i := range left {
		if left[i] != right[i] {
			return false
		}
	}

	return true
}

func preorder(node *TreeNode, orders *[]int) {
	if node.Left == nil && node.Right == nil {
		*orders = append(*orders, node.Val)
		return
	}

	*orders = append(*orders, node.Val)

	if node.Left != nil {
		preorder(node.Left, orders)
	} else {
		*orders = append(*orders, -101)
	}

	if node.Right != nil {
		preorder(node.Right, orders)
	} else {
		*orders = append(*orders, -101)
	}
}

func levelorder(node *TreeNode, orders *[]int) {
	if node.Left == nil && node.Right == nil {
		*orders = append(*orders, node.Val)
		return
	}

	*orders = append(*orders, node.Val)

	if node.Right != nil {
		levelorder(node.Right, orders)
	} else {
		*orders = append(*orders, -101)
	}

	if node.Left != nil {
		levelorder(node.Left, orders)
	} else {
		*orders = append(*orders, -101)
	}
}

func main() {
	fmt.Println(isSymmetric(&TreeNode{Val: 1, Left: &TreeNode{Val: 2, Left: &TreeNode{Val: 3, Left: nil, Right: nil}, Right: &TreeNode{Val: 4, Left: nil, Right: nil}}, Right: &TreeNode{Val: 2, Left: &TreeNode{Val: 4, Left: nil, Right: nil}, Right: &TreeNode{Val: 3, Left: nil, Right: nil}}}) == true)
	fmt.Println(isSymmetric(&TreeNode{Val: 1, Left: &TreeNode{Val: 2, Left: nil, Right: &TreeNode{Val: 3, Left: nil, Right: nil}}, Right: &TreeNode{Val: 2, Left: nil, Right: &TreeNode{Val: 3, Left: nil, Right: nil}}}) == false)
	fmt.Println(isSymmetric(&TreeNode{Val: 2, Left: &TreeNode{Val: 3, Left: &TreeNode{Val: 4, Left: nil, Right: nil}, Right: &TreeNode{Val: 5, Left: &TreeNode{Val: 8, Left: nil, Right: nil}, Right: &TreeNode{Val: 9, Left: nil, Right: nil}}}, Right: &TreeNode{Val: 3, Left: &TreeNode{Val: 5, Left: &TreeNode{Val: 9, Left: nil, Right: nil}, Right: &TreeNode{Val: 8, Left: nil, Right: nil}}, Right: &TreeNode{Val: 4, Left: nil, Right: nil}}}) == true)
	fmt.Println(isSymmetric(&TreeNode{Val: 5, Left: &TreeNode{Val: 2, Left: &TreeNode{Val: 4, Left: nil, Right: &TreeNode{Val: 1, Left: &TreeNode{Val: 2, Left: nil, Right: nil}, Right: nil}}, Right: nil}, Right: &TreeNode{Val: 2, Left: nil, Right: &TreeNode{Val: 1, Left: nil, Right: &TreeNode{Val: 4, Left: &TreeNode{Val: 2, Left: nil, Right: nil}, Right: nil}}}}) == false)
}
