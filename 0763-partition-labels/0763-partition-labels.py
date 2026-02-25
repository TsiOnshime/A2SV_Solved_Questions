class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
ababcbacadefegdehijhklij
last[a] = 8
last[b] = 5
last[c] = 7

last[d] = 14
last[e] = 15
last[f] = 11
last[g] = 13

last[h] = 19
last[i] = 22
last[j] = 23
last[k] = 20 

First we find the last occurence of each element

we do that by using enumerate and adding a key:index into our dict

one thing to notice while iteration if it finds a at 0 and added it like a:0 when it again finds a at 5 it will update the value to 5

initialize a res list to append our result to

then we will have two pointers l and r

l starting at zero and r staring at the last occurence of the first element

we will iterate through the string

we find the last occurence of each element at that index

assign the maximum(r, last_occurence[s[i]]) to r

and we keep going until we find out that r == i

which means if we have said the last occurence of a was 8 all the elements in between 0 and 8 are in the boundary 

which makes us think they do only appear with in this boundary

so after that we add the value r - l + 1 to our result array, because we are asked to find the length of the partitions.

and update the value of l to be r + 1, the value of r to last_occurence[s[l]]
        """
        last_occurence = {}

        for i, ch in enumerate(s):
            last_occurence[ch] = i


        res = []
        l = 0
        r = last_occurence[s[l]]

        for i in range(len(s)):
            last = last_occurence[s[i]]
            r = max(last, r)

            if i == r:
                res.append(r-l+1)
                l = r + 1
                if l < len(s):
                    r = last_occurence[s[l]]
                

        return res



