def reverse(x):

    result = 0
    remeinder = x

# handle negative integers pt.1
    if (x < 0):
        remeinder *= -1

# reverse the integer -> 123 = 321
    for i in range(len(str(remeinder))):
        num = remeinder % 10
        remeinder = remeinder/10
        result = (result*10) + num

# Revert integer to negative
    if (x < 0):
        result *= -1


reverse(123)
reverse(-666)
reverse(1200)
reverse(-4500)
reverse(-45001)
