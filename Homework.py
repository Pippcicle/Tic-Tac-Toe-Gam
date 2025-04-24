M1 = [[4,3,1],[7,6,8], [7,2,8]]
M2 = [[3,7,9],[5,9,3], [0,4,8]]
added_matrix = []
for i in range(3): 
    matrix_row = []
    for w in range(3):
        matrix_row.append(M1[i][w] + M2[i][w])
    added_matrix.append(matrix_row)
print(added_matrix)