"""
3 2 4
91 94
92 97
97 99
92 94
93 97
95 96
90 100

n k q

n = number of receipis
k = number of range a temprature should appear in to be addmissible
q = number of questions she asks (for eg 4 then for each number in this question range we calculate the admissible tempratures and print that number)



90 91 92 93 94 95 96 97 98 99 100 

OHMYGOD

accept the first n elements as ranges=
accept the last q elements as queries = 


then create an array starting at the smallest element of the queries to the largest element

90 91 92 93 94 95 96 97 98 99 100 
offset = 90
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] => are the indexes

then iterate through the ranges and find (91, 94)
we iterate in range(91, 95)
mark the elements starting from 1th index to the 4th index += 1

when we're done we'll have

[0, 1, 2, 2, 2, 1, 1, 2, 1, 1, 0]
when we do our prefix we mark the elements with value greater than or equal to k
[0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0]
[0, 0, 1, 2, 3, 3, 3, 4, 4, 4, 4]

so when we're asked how many admissible temps between the queries we simply do prefix[queries[1] - offset] - prefix[queries[0] - 0ffset - 1] if queries[0] - offset > 0 else res = prefix[queries[1] - offset]

then we will print the result

"""
n, k, q = list(map(int, input().split(" ")))

freq = [0] * 200005
temps = []
for i in range(n):
    l, r = list(map(int, input().split(" ")))
    temps.append([l, r])
    freq[l] += 1
    freq[r + 1] -= 1


for i in range(1, len(freq)):
    freq[i] += freq[i - 1]


queries = []
for i in range(q):
    queries.append(list(map(int, input().split(" "))))




prefix = [0] * len(freq)

for i in range(len(freq)):
    if freq[i] >= k:
        prefix[i] = 1


for i in range(1, len(prefix)):
    prefix[i] += prefix[i - 1]


for query in queries:
    start = query[0]
    end = query[1]


    if start > 0:
        print(prefix[end] - prefix[start - 1])
    else: print(prefix[end])
        
    

    
