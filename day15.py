# https://www.codechef.com/practice/course/greedy-algorithms/INTGRA01/problems/MAXDIFF
for _ in range(int(input())):
    n, k = map(int, input().split())
    l = sorted(map(int, input().split()))
    c = min(k, n - k)
    print(sum(l[c:]) - sum(l[:c]))
