# https://www.codechef.com/problems/COUPON2
for _ in range(int(input())):
    a, b = map(int, input().split())
    c = sum(map(int, input().split()))
    d = sum(map(int, input().split()))
    if c >= 150 and d >= 150:
        print("YES" if c + d + b < c + d + 2 * a else "NO")
    elif c < 150 and d < 150:
        print("NO")
    else:
        print("YES" if c + d + b + a < c + d + 2 * a else "NO")

