import sys 

test_cases = int(sys.stdin.readline().strip())

total = 0 
ans = [] 

for line in sys.stdin: 
    if line == '\n': # search for newline
        line = next(sys.stdin) 
        students = int(line.strip()) 

        for i in range(students):
            line = next(sys.stdin) 
            total += int(line.strip())
        
        if (total % students) == 0: # check if total candies divisible 
            result = 1 # if divisible 

        else: 
            result = 0 

        ans.append(result) # for every new case, append the total into list, ans 
        total = 0 # reset the total count for next case 
    
    else: # do nothing
        pass  

for i in range(test_cases): 
    if ans[i] == 1: 
        print("YES")
    elif ans[i] == 0: 
        print("NO")

