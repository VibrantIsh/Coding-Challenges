# https://www.codechef.com/practice/course/2to3stars/LP2TO301/problems/ALTER

for _ in range(int(input())):
    a, b, p, q = map(int, input().split())
    print("YES" if (p % a == 0 and q % b == 0 and (p // a == q // b or p // a == q // b + 1 or p // a + 1 == q // b)) else "NO")
