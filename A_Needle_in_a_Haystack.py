test = int(input())

for _ in range(test):
    s = input()

    t = input()
    
    offset = 97
    count_s = [0] * 26
    for ch in s:
        count_s[ord(ch) - offset] += 1
    # print(count_t)  
    count_t = [0] * 26
    for ch in t: 
        count_t[ord(ch) - offset] += 1
    
    # ddcbe
#bedbaecfc
# baecf
    
    
    count_diff = [0]*26
    Flag = False
    for i in range(26):
        diff = count_t[i] - count_s[i]
        if diff < 0:
            print("Impossible")
            Flag = True
            break
        else:
            count_diff[i] = diff      
            
    if Flag:
        continue
    
    t_diff = []
    for i in range(len(count_diff)):
        if count_diff[i] != 0:
            t_diff.append((chr(97+i) * count_diff[i]))

    t_diff = ("").join(t_diff)

      
#abacabadabacaba
    # s = dcbe t_diff = abcef 
    # res = [a] [a,b] [abcdcbeef]
    i = j = 0  # i for pointing at s and j for pointing at t_diff
    res_i = []
    
    while i < len(s) and j < len(t_diff):
        if t_diff[j] < s[i]:
            res_i.append(t_diff[j])
            j += 1
        else:
            res_i.append(s[i])
            i += 1

    if j < len(t_diff):
        res_i.extend(t_diff[j:])
    elif i < len(s):
        res_i.extend(s[i:])
        
    
    i = j = 0  # i for pointing at s and j for pointing at t_diff
    res_j = []
    
    while i < len(s) and j < len(t_diff):
        if t_diff[j] <= s[i]:
            res_j.append(t_diff[j])
            j += 1
        else:
            res_j.append(s[i])
            i += 1

    if j < len(t_diff):
        res_j.extend(t_diff[j:])
    elif i < len(s):
        res_j.extend(s[i:])
        
    print(min("".join(res_i), "".join(res_j)))
    
