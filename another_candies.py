# text file contains: 
# number indicating no. of test cases 
# next para with 1st num indicating no. of students, 
# and the num of candies each student has 

# ensure that all test cases are accounted for 
# while loop that loops n times based on the first integer, n 
# readlines once to extract the integer, n 
# following paragraphs are all separated by a whiteline

a_file = open('a.txt', 'r' ) 

test_cases = int(a_file.readline().strip())

total = 0 
ans = [] 

for line in a_file: 
    if line == '\n': # search for newline
        line = next(a_file) 
        students = int(line.strip()) 

        for i in range(students):
            line = next(a_file) 
            total += int(line.strip())
        
        if (total % students) == 0: # check if total number of candies is divisable by total students 
            result = 1 # if divisible 

        else: 
            result = 0 

        ans.append(result) # for every new case, append the total into list, ans 
        total = 0 # reset the total count for next case 
    
    else: # do nothing
        pass 

a_file.close() 

for i in range(test_cases): 
    if ans[i] == 1: 
        print("YES")
    elif ans[i] == 0: 
        print("NO")

