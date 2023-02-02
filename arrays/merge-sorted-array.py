
def merge_sorted_arrays(arr1, arr2):

    pointer1 = 0
    pointer2 = 0
    answer = []

    if (len(arr1) == 0):
        return arr2

    if (len(arr2) == 0):
        return arr1

    while (pointer1 < len(arr1) and pointer2 < len(arr2)):

        curArr1 = arr1[pointer1]
        curArr2 = arr2[pointer2]

        if (curArr1 < curArr2):
            answer.append(curArr1)
            pointer1 += 1
        elif (curArr1 > curArr2):
            answer.append(curArr2)
            pointer2 += 1
        else:
            answer.append(curArr1)
            pointer1 += 1

    if (pointer1 < len(arr1)):
        for number in range(pointer1, len(arr1)):
            answer.append(arr1[number])

    elif (pointer2 < len(arr2)):
        for number in range(pointer2, len(arr2)):
            answer.append(arr2[number])

    print(answer)


merge_sorted_arrays([1, 2], [1, 2, 4, 5])
