# https://www.codechef.com/practice/course/interview-dsa/DSAPREP_01/problems/LUCNUM
for _ in range(int(input())):
    x = int(input())
    if x % 2 == 1:
        print(1)
    else:
        c = 0
        while x > 0 and x % 2 == 0:
            c += 1
            x //= 2 
        print(1 if c % 2 == 0 else 0)
