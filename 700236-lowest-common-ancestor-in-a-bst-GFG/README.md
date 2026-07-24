# [Lowest Common Ancestor in a BST](https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1)
## Medium
Given the root of a Binary Search Tree (with all values unique) and two nodes n1 and n2 (n1 != n2). You may assume that both nodes exist in the tree. Find the Lowest Common Ancestor (LCA) of the given two nodes in the BST.
Note: LCA between two nodes n1 and n2 is defined as the deepest node that has both n1 and n2 as descendants (where we allow a node to be a descendant of itself).
Examples:
Input: root = [5, 4, 6, 3, N, N, 7, N, N, N, 8], n1-&gt;data = 7, n2-&gt;data = 8
      
Output: 7Explanation: 7 is the lowest node that has both 7 and 8 as descendants.

Input: root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14], n1-&gt;data = 8, n2-&gt;data = 14       &nbsp; &nbsp; 
Output: 8Explanation: 8 is the lowest node that has both 8 and 14 as descendants.
Input: root = [2, 1, 3], n1-&gt;data = 1, n2-&gt;data = 3
        
Output: 2Explanation: 2 is the lowest node that has both 1 and 3 as descendants.
Constraints:1 ≤&nbsp;number of nodes ≤ 1051 ≤ node-&gt;data ≤&nbsp;1051 ≤ n1-&gt;data, n2-&gt;data ≤ 105