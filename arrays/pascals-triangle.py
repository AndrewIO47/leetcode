def generate(numRows):

    result = [[1]]

    for i in range(numRows - 1):
        # temporary array to add zeros to both ends
        temp = [0] + result[-1] + [0]
        # current row that we will be adding 
        row = []
        for j in range(len(result[-1]) + 1):
            row.append(temp[j] + temp[j+1])
        
        result.append(row)
    
    return result
