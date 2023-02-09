def isHappy(n):

    visited = set()

    while n != 1:
        n = sum([int(number)**2 for number in str(n)])
        print(n)

        if n is not visited:
            visited.add(n)
        else:
            return False

        if n == 1:
            return True

    return False


print(isHappy(19))
