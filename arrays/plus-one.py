from unicodedata import digit


def plusOne(digits):

    digits = digits[::-1]
    carry = 1
    i = 0

    while carry == 1:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += 1
                carry = 0

        else:
            carry = 0
            digits.append(1)
        i += 1

    return digits[::-1]


plusOne([1, 9, 9, 8])
