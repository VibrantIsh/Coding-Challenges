# https://www.codechef.com/practice/course/arrays-strings-sorting/INTARR01/problems/EQUALELE
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = input().split()
    
    c = Counter(a)
    m = max(c.values())
    print(n - m)
