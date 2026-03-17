# to be legal i + 1 - prefix[i] == prefix[i]
    for i in range(n):
        if i + 1 - prefix[i] == prefix[i]:
            legal.add(i)
    if a == b:
        print("YES")   
    else:
        if not legal:
            print("NO")     
        else:
            flipped = 0
            for i in range(n - 1, -1, -1):
                current = a[i] 
                
                if flipped % 2: 
                    current = "1" if current == "0" else "0"
                if current != b[i]:
                    if i not in legal:
                        print("NO")
                        break
                    flipped += 1
            else:
                print("YES")