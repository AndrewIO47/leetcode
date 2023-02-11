def isUgly(n):

    if n == 1:
        return True

    for prime_factor in [2, 3, 5]:
        #  devide n by the prime factor until it is no longer divisible by it
        while n % prime_factor == 0:
            n = n / prime_factor

        if n == 1:
            return True
    return False


isUgly(6)
isUgly(14)
isUgly(1)
