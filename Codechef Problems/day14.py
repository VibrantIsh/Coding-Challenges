# https://www.codechef.com/problems/LONGSEQ
for _ in range(int(input())):
    x = input()
    print("Yes" if x.count('0') in (1, len(x) - 1) else "No")
