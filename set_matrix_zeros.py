def set_matrix_zeros(matrix):


    rows,columns=len(matrix),len(matrix[0])

    #Inorder to keep track which rows and columns are having zeros
    zero_rows,zero_columns=[False]*rows,[False]*columns

    #For identifying which rows and columns should be zero
    for row in range(rows):
        for column in range(columns):
            if matrix[row][column]==0:
                zero_rows[row],zero_columns[column]=True,True  

    #set zero based on the tracking using zero_rows and zero_columns

    for row in range(rows):
        for column in range(columns):
            if zero_rows[row] or zero_columns[column]:
                matrix[row][column]=0
    return matrix

if __name__=="__main__":
    print(set_matrix_zeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))