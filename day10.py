class P:
    def c(self, n, a):
        return "YES" if all(a.count(x) % 2 == 0 for x in set(a)) else "NO"


def m():
    t = int(input())
    p = P()
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        r = p.c(n, a)
        print(r)


if __name__ == "__main__":
    m()

