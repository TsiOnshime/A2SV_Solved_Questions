# [Inorder Successor in BST](https://www.geeksforgeeks.org/problems/inorder-successor-in-bst/1)
## Easy
Given a BST, and a reference to a Node k in the BST. Find the Inorder Successor of the given node in the BST. If there is no successor, return -1.&nbsp;
Examples :
Input: root = [2, 1, 3], k = 2
Output: 3 
Explanation: Inorder traversal : 1 2 3 Hence, inorder successor of 2 is 3.
Input: root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14], k = 8 &nbsp; &nbsp; 
Output: 10
Explanation: Inorder traversal: 4 8 10 12 14 20 22. Hence, successor of 8 is 10.
Constraints:1 ≤ n ≤ 105, where n is the number of nodes