def valid_phone(num):
    s = str(num)
    return len(s) == 5 and s[0] != '0'

T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    print("YES" if valid_phone(N * X) else "NO")
