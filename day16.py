# https://www.codechef.com/practice/course/interview-dsa/DSAPREP_01/problems/LUCNUM
for _ in range(int(input())):
    n = int(input())
    if n % 2 == 1:
        print(1)
    else:
        count = 0
        while n > 0 and n % 2 == 0:
            count += 1
            n //= 2 
        print(1 if count % 2 == 0 else 0)
