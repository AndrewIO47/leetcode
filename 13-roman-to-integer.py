def romanToInt(s):

    roman = {}
    roman["I"] = 1
    roman["V"] = 5
    roman["X"] = 10
    roman["L"] = 50
    roman["C"] = 100
    roman["D"] = 500
    roman["M"] = 1000

    result = 0

    for i in range(len(s)):
        curr_letter = s[i]

        # checks that we are on bound and if the current letter is < next letter
        if i + 1 < len(s) and roman[curr_letter] < roman[s[i+1]]:
            result -= roman[curr_letter]
        # checks that we are on bound and if the current letter is > or = next letter
        else:
            result += roman[curr_letter]

    print(result)
    return result


romanToInt("MCMXCIV")
