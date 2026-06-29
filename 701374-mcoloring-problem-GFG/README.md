# [M-Coloring Problem](https://www.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1)
## Medium
You are given an undirected graph consisting of&nbsp;V&nbsp;vertices and&nbsp;E&nbsp;edges represented by a list&nbsp;edges[][], along with an integer&nbsp;m. Your task is to determine whether it is possible to&nbsp;color the graph&nbsp;using at most&nbsp;m&nbsp;different colors such that no two adjacent vertices share the&nbsp;same color. Return&nbsp;true&nbsp;if the graph can be colored with at most&nbsp;m&nbsp;colors, otherwise return&nbsp;false.
Note:&nbsp;The graph is indexed with 0-based indexing.
Examples:
Input: V = 4, edges[][] = [[0, 1], [1, 3], [2, 3], [3, 0], [0, 2]], m = 3
Output: true
Explanation: It is possible to color the given graph using 3 colors, for example, one of the possible ways vertices can be colored as follows:Vertex 0: Color 1
Vertex 1: Color 2
Vertex 2: Color 2
Vertex 3: Color 3

Input: V = 3, edges[][] = [[0, 1], [1, 2], [0, 2]], m = 2
Output: falseExplanation: It is not possible to color the given graph using only 2 colors because vertices 0, 1, and 2 form a triangle.
Constraints:1 ≤ V ≤ 101 ≤ E = edges.size() ≤ (V*(V-1))/20 ≤ edges[i][j] ≤ V-11 ≤ m ≤ V