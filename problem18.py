size_of_matrix = 15
matrix = []

#creating number of rows
for i in range(0,size_of_matrix):
	matrix.append([])

#creating matrix of values
for i in range(0,size_of_matrix):
	my_list = input('').split(' ')
	for j in range(0,i+1):
		matrix[i].append(int(my_list[j]))


# start from second last row find the maximum of two adjacent below numbers and add it to the current number
# repeat till first row which will contain our result
for i in range(size_of_matrix-2,-1,-1):
	for j in range(0,i+1):
		if(matrix[i+1][j] > matrix[i+1][j+1]):
			matrix[i][j] = matrix[i][j]+matrix[i+1][j]
		else:
			matrix[i][j] = matrix[i][j]+matrix[i+1][j+1]

# fucking solved it
print(matrix[0][0])