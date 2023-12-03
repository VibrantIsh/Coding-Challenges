# https://www.codechef.com/practice/course/number-theory/INTNT01/problems/BETDEAL
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    if 100 - a == 200 - 2 * b:
        print("BOTH")
    elif 100 - a < 200 - 2 * b:
        print("FIRST")
    else:
        print("SECOND")
