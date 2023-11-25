# https://www.codechef.com/problems/NAME2
def marriage_check(s1, s2):
    i = 0
    for j in range(len(s2)):
        if i < len(s1) and s1[i] == s2[j]:
            i += 1
    return "YES" if i == len(s1) else "NO"

for _ in range(int(input())):
    partner1, partner2 = input().split()
    if len(partner1) > len(partner2):
        partner1, partner2 = partner2, partner1
    print(marriage_check(partner1, partner2))
