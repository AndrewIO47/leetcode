def strStr(haystack, needle):

    #  len(haystack) + 1 - len(needle)
    # -> so we dont have to search at the last letter in the string
    #  since there are no other letter beyond that point (index out of bound)
    for i in range(len(haystack) + 1 - len(needle)):
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
            if j == len(needle) - 1:
                return i


strStr("adbutsad", "sad")
