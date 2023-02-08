import numbers
from turtle import backward


def isPalindrome(x):

    # edge case when x is negative
    if (x < 0):
        return False

    backward_num = 0
    copy_of_x = x

    # reverse the number
    while (copy_of_x != 0):
        curr_num = copy_of_x % 10  # get the last number
        copy_of_x = copy_of_x/10  # get rid of the last number
        backward_num = (backward_num*10) + curr_num

    if (backward_num != x):
        return False

    return True


isPalindrome(121)

# NAIVE SOLUTION

# # edge case when the number is negative
# if(x < 0):
#     return False

# # reverse the integer
# str_number = str(x)
# arr_number = []
# for number in str_number:
#     arr_number.append(number)

# backwards_number = []
# for i in range(len(arr_number)-1, -1, -1):
#     backwards_number.append(arr_number[i])

# for i in range(len(arr_number)):
#     if (arr_number[i] != backwards_number[i]):
#         return False

# return True

# compare values

# edge case when the number is negative
