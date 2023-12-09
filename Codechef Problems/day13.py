#https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/SMOL?tab=statement
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(n if k == 0 else n % k if n >= k else n)
