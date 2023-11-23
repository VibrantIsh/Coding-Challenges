# https://www.codechef.com/problems/ZEROSTRING
for _ in range(int(input())):
    a=int(input())
    b=input()
    c=b.count("0")
    d=b.count("1")
    if c>=d:
        print(a-c)
    else:
        print(a-d+1)

