# 2193C-Replace-and-Sum

**Problem:** [2193C-Replace-and-Sum](https://codeforces.com/contest/2193/problem/C)

**time limit per test:** 2 seconds

**memory limit per test:** 256 megabytes

---

Today, KQ has an exam at the Grail Academy. A strict teacher gave a task that KQ could not solve. He was given two arrays a and b of length n. KQ is allowed to perform the following operations on the arrays: 

 
-  Choose an index i (1≤ i\lt n) and replace a_i with a_{i+1}. 
-  Choose an index i (1≤ i≤ n) and replace a_i with b_i. 
 Now he has q queries. Each query is described by two numbers l and r. His task is to find the maximum value of the sum (a_l + a_{l+1} + a_{l+2} + … + a_r) for each query, if he can perform any number of operations on any elements of the array. Since he is not skilled enough for this, he asks for your help.


**Input**

Each test consists of several test cases. The first line contains one integer t (1≤ t≤ 10⁴) — the number of test cases. The description of the test cases follows.

The first line of each test case contains two integers n, q (1≤ n, q≤ 2 ⋅ 10⁵).

The second line of each test case contains n integers a_1, a_2,...,a_n (1≤ a_i≤ 10⁴).

The third line of each test case contains n integers b_1, b_2,...,b_n (1≤ b_i≤ 10⁴).

The following q lines contain two integers l and r (1≤ l≤ r≤ n).

It is guaranteed that the sum of the values of n and the sum of the values of q across all test cases do not exceed 2 ⋅ 10⁵.


**Output**

For each test case, output q numbers separated by spaces — the maximum values of the sums (a_l + a_{l+1} + a_{l+2} + … + a_r).


**Example**

**Input**

```
4
3 1
3 2 1
1 2 3
1 3
1 1
1
2
1 1
3 2
6 7 5
9 6 8
1 2
2 3
4 3
4 3 2 1
5 1 3 1
1 2
2 4
3 4
```

**Output**

```
9
2
17 16
8 7 4
```


**Note**

Consider the first test case. Replace a_3 with b_3, a = [3, 2, 3]. Replace a_2 with a_3, a = [3, 3, 3]. The sum a_1 + a_2 + a_3 = 9.
