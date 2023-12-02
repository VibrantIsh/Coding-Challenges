# https://www.codechef.com/practice/course/interview-dsa/DSAPREP_01/problems/MONSTER1
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(0 if c >= b else 1)
