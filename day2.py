# https://www.codechef.com/practice/course/strings-cpp/PCPPST01/problems/TWOSTR
def check_matching_strings(x, y):
    for j in range(len(x)):
        if x[j] != y[j] and x[j] != "?" and y[j] != "?":
            return "No"
    else:
        return "Yes"

def main():
    test_cases = int(input("Enter the number of test cases: "))

    for _ in range(test_cases):
        x = input("Enter the first string: ")
        y = input("Enter the second string: ")

        result = check_matching_strings(x, y)
        print("Output:", result)
        print()

if __name__ == "__main__":
    main()

