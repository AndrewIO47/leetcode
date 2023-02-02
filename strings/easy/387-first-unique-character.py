def firstUniqChar(s):

    dict = {}

    for letter in s:
        # if the key is in the dict, increase the count by 1
        if (letter in dict):
            value = dict.get(letter, 'default_value')
            dict[letter] = value + 1
        # if key is not in the dict, add it
        else:
            dict[letter] = 1

    # search the first unique char with value = 1
    for i in range(0, len(s)):
        letter = s[i]
        value = dict.get(letter, 'default_value')
        if (letter in dict and value == 1):
            print(i)
            return i

    return -1


firstUniqChar("aabb")
