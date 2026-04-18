"""
matrix = [
            [ 0 , 0 ,0]
            [ 0 , 0 ,0]
            [ 0 , 1 ,0]
         ]

at matrix[x][y] you have to mark to hide the money
where x and y are positions , and not indexes 
e.g position 3,2 is marked in the matrix as 1
(hint x-1 , y-1 for indexing)

"""
# matrix = [[0,0,0],[0,0,0],[0,0,0]]
# print(matrix)  

row1 = ['😊','😊','😊']
row2 = ['😊','😊','😊']
row3 = ['😊','😊','😊']

matrix = [row1,row2,row3 ]

print(f"{row1}\n{row2}\n{row3} ")

#row = int(input("Enter row position "))
#col = int(input("Enter col position "))

digit = input("Enter a tw0 digit number: ")
row = int(digit[0])
col = int(digit[1])
matrix[row-1][col-1] = '💵'
print(f"{row1}\n{row2}\n{row3} ")
