# https://www.codechef.com/practice/course/strings-cpp/PCPPST01/problems/TWOSTR
for _ in range(int(input())):
    x, y = input(), input()
    print("Yes" if all(a == b or '?' in {a, b} for a, b in zip(x, y)) else "No")
