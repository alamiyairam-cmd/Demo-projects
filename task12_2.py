def analyze_string(s):
    if s == "":
        print("String is empty.")
        return

    print("Length:", len(s))
    print("Reverse:", s[::-1])

    vowels = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch in vowels:
            count += 1

    print("Number of vowels:", count)

    print("\nCharacter\tPositive\tNegative")
    for i in range(len(s)):
        print(s[i], "\t\t", i, "\t\t", i - len(s))


text = input("Enter a string: ")
analyze_string(text)