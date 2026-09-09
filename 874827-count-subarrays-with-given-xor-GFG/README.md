# [Count Subarrays with given XOR](https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/1)
## Medium
Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.
Note:&nbsp;It is guranteed that the total count will fit within a 32-bit integer.
Examples:&nbsp;
Input: arr[] = [4, 2, 2, 6, 4], k = 6Output: 4Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], and [6]. Hence, the answer is 4.
Input: arr[] = [5, 6, 7, 8, 9], k = 5Output: 2Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]. Hence, the answer is 2.
Input: arr[] = [1, 1, 1, 1], k = 0Output: 4Explanation: The subarrays are [1, 1], [1, 1], [1, 1] and [1, 1, 1, 1].
Constraints:1&nbsp;≤&nbsp;arr.size()&nbsp;≤&nbsp;1050&nbsp;≤ arr[i] ≤ 1050&nbsp;≤ k&nbsp;≤&nbsp;105