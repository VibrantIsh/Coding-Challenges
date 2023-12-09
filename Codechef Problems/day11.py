# https://www.codechef.com/practice/course/two-pointers/POINTERF/problems/PREP17
for _ in range(int(input())):
    N = int(input())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    print(len(A.intersection(B)))

