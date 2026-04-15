# 143. Reorder-List

**Difficulty:** Medium

**Problem:** [Reorder-List](https://leetcode.com/problems/reorder-list)

---

You are given the head of a singly linked-list. The list can be represented as:

```
L 0  &rarr; L 1  &rarr; ... &rarr; L n - 1  &rarr; L n
```

Reorder the list to be on the following form:

```
L 0  &rarr; L n  &rarr; L 1  &rarr; L n - 1  &rarr; L 2  &rarr; L n - 2  &rarr; ...
```

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:

![](https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg)

```
Input:  head = [1,2,3,4]
Output:  [1,4,2,3]
```

Example 2:

![](https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg)

```
Input:  head = [1,2,3,4,5]
Output:  [1,5,2,4,3]
```

**Constraints:**

- The number of nodes in the list is in the range `[1, 5 * 10⁴]`.

- `1 <= Node.val <= 1000`