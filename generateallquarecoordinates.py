def generateCoordinates(matrix):

    #for a nxn matrix...generate the coordinates of all the square
    #example 5x5 matrix will have only 1 square with length 5
    #but multiple squares of length 4, 3 and 2
    # this will generate all coordinates
    
    matrix_len = len(matrix)
    if matrix_len < 2:
        return []
    
    result = []
    i = matrix_len
    
    while i > 1:
        getCoordinates(i, matrix_len, matrix, result)
        i = i - 1
    
    print(result)
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
    
    tmp_missing = []
    #corner coordinates are in [(x,y),(x,ymax),(xmax,y),(xmax,ymax)] format
    x = result[len(result) - 1]
    h_x = x[0][0]
    h_maxx = x[2][0]
    v_y = x[0][1]
    v_maxy = x[1][1]
    tmp = v_y + 1
    while tmp <  v_maxy:
        tmp_missing.append([h_x,tmp])
        tmp_missing.append([h_maxx,tmp])
        tmp = tmp + 1
    tmp_x = h_x + 1
    while tmp_x <  h_maxx:
        tmp_missing.append([tmp_x,v_y])
        tmp_missing.append([tmp_x,v_maxy])
        tmp_x = tmp_x + 1
    
    print('before tmp add' ,result[len(result) - 1])
    print('tmp_missing :', tmp_missing )
    result[len(result) - 1].append(tmp_missing)
    print('after tmp add', result[len(result) - 1])

    return result

if __name__ == "__main__":
     matrix = [[1,1,1,1,5],[1,1,1,1,1],[1,1,1,1,5],[1,2,3,4,5],[1,2,3,4,5]]
     result = generateCoordinates(matrix)
     for x in result:
        res = all(matrix[p[0]][p[1]] == 1 for p in x)
        #print(res)
        if res:
            print(x)
            #generate the missing coordinates
            # tmp_missing = []
            # #corner coordinates are in [(x,y),(x,ymax),(xmax,y),(xmax,ymax)] format
            # h_x = x[0][0]
            # h_maxx = x[2][0]
            # v_y = x[0][1]
            # v_maxy = x[1][1]
            # tmp = v_y + 1
            # while tmp <  v_maxy:
            #     tmp_missing.append([h_x,tmp])
            #     tmp_missing.append([h_maxx,tmp])
            #     tmp = tmp + 1
            # tmp_x = h_x + 1
            # while tmp_x <  h_maxx:
            #     tmp_missing.append([tmp_x,v_y])
            #     tmp_missing.append([tmp_x,v_maxy])
            #     tmp_x = tmp_x + 1
            
            # tmp_res = all(matrix[p[0]][p[1]] == 1 for p in tmp_missing)
            # if tmp_res:
            #     print(x,tmp_missing)

        