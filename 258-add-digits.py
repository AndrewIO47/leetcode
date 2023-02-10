from unittest import result


def addDigits(num):

    while num > 9:
        # reset every time num has two digits
        result = 0
        # sum every digit of num
        for number in str(num):
            result += int(number)
        # update num to the new number
        num = result
    return num

# LEETCODE SOLUTION NOT USING LOOPS
    # if num == 0 : return 0
    # if num % 9 == 0 : return 9
    # else : return (num % 9)


addDigits(9)
