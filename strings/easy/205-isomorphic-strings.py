def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # Hashamap map from key 's' to value 't'
    mapST = {}
    # Hashamap map from key 't' to value 's'
    mapTS = {}

    # iterate over each letter of the string. since both are the same length
    # it doesn't matter which string length we choose
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        #  checks if the key already exists and if their value is the same as the current we are looking at
        if char_s in mapST and mapST[char_s] != char_t or char_t in mapTS and mapTS[char_t] != char_s:
            return False
        # if key and value is not in the hashmap, add it
        else:
            mapST[char_s] = char_t
            mapTS[char_t] = char_s
    return True


a = "gg"
b = "dd"
print(isIsomorphic(a, b))
