"""
    
    [0 0 0 0 0]
    [0 0 0 0 0]
    [0 0 0 0 1]
    [0 0 0 0 0]
    [0 0 0 0 0]
    
    row = 2
    col = 2
    
    o_row = 2
    o_col = 4
    
    col_swap = abs(o_col - col) => 2
    row_swap = abs(o_row - row) => 0
    
    full swap = col_swap + row_swap => 2

    [0 0 0 0 0]
    [0 0 0 0 0]
    [0 0 0 0 0]
    [0 0 0 1 0]
    [0 0 0 0 0]
    
    col = row = 2
    
    o_col = 3
    o_row = 3
    
    row_swap = 3 - 2 = 1
    col_swap = 3 - 2 = 1
    
    full_swap = 2
    
"""
matrix = []

for i in range(5):
    row = list(map(int, input().split(" ")))
    
    if 1 in row:
        r = i
        c = row.index(1)
        
    
    matrix.append(row)



row_swap = abs(r - 2)
col_swap = abs(c - 2)

full_swap = row_swap + col_swap

print(full_swap)
