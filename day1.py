# https://www.codechef.com/practice/course/arrays-cpp/PCPPAR01/problems/KITCHENCOST

def tc(N, X, A, B):
    t = 0
    for i in range(N):
        if A[i] >= X:
            t += B[i]
    return t

def htc():
    n = int(input("Enter the number of items: "))
    x = int(input("Enter the minimum freshness value required: "))
    
    print("Enter freshness values for each item (space-separated):")
    a = list(map(int, input().split()))
    
    print("Enter the cost of each item (space-separated):")
    b = list(map(int, input().split()))
    
    if len(a) != n or len(b) != n:
        print("Error: Mismatch")
        return
    
    t = tc(n, x, a, b)
    
    print("Total cost:", t)

htc()
