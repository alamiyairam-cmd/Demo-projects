def analyze_string(s):
        print("length of the string :", len(s))
        print("reverse string:", s[::-1])
        vowels = "aeiou"
        count = 0

        for ch in s.lower():
            if ch in vowels:
                count += 1
                
                print("Number of vowels:", count)
                print ("\nCharacter position ")

                for i in range(len(s)):
                    print(
                         "Characrter:", s[i],
                         "| positive Index:",i,
                         " Negative Index:", i - len(s)
                    )
                    text = input("Enter a string:")
                    if text == "":
                        print("Empty string is not allowe.")
                    else:
                         pass
                    analyze_string(text)


                    