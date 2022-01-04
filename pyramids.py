import sys  

x = int(sys.stdin.readline())

def pyra_seq(n): 

    if n == 0: 
        return 1 

    else: 
        return (2*n + 1)**2 + pyra_seq(n-1) 

def pyramid(n): 

    height = 0 
    total = 0 

    while True:
        total = pyra_seq(height) 

        if total < n: 
            height += 1 

        else: 
            break 
    
    return height 

print(pyramid(x))

