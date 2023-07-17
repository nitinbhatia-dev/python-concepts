def generateCoordinates(matrix):

    #for a nxn matrix...generate the coordinates of all the square
    #example 5x5 matrix will have only 1 square with length 5
    #but multiple squares of length 4, 3 and 2
    #currently this generates only the corner cordinates
    
    matrix_len = len(matrix)
    if matrix_len < 2:
        return []
    
    result = []
    i = matrix_len
    
    while i > 1:
        getCoordinates(i, matrix_len, matrix, result)
        i = i - 1
    
    #print(result)
    return result


def getCoordinates(square_size, matrix_len, matrix, result):
    if square_size > matrix_len:
        return []
    
    
    i = j = 0
    i_end = j_end = square_size - 1
    while i_end < matrix_len:
        
        while j_end < matrix_len:
            result.append([[i,j],[i,j_end],[i_end,j],[i_end, j_end]])
            j = j + 1
            j_end = j_end + 1
        j = 0
        j_end = square_size - 1
        i = i + 1
        i_end = i_end + 1
    
    return result

if __name__ == "__main__":
     matrix = [[1,1,1,4,5],[1,1,1,4,1],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
     result = generateCoordinates(matrix)
     for x in result:
        res = all(matrix[p[0]][p[1]] == 1 for p in x)
        #print(res)
        if res:
            print(x)