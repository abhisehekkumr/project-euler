matrix = []

size_of_matrix = 20


# creating number of rows
for i in range(0,size_of_matrix):
	matrix.append([])

# creating number of columns
for i in range(0,size_of_matrix):
	for j in range(0,size_of_matrix):
		matrix[i].append(int(0))

# intializing matrix to intial values
k = 3
matrix[0][0] = 2
for i in range(1,size_of_matrix):
	matrix[i][0] = k
	matrix[0][i] = k
	k = k +1

# finding the total number of paths
for i in range(1,size_of_matrix):
	for j in range(1,size_of_matrix):
		matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

# printig the results
for i in range(0,size_of_matrix):
	for j in range(0,size_of_matrix):
		print(matrix[i][j],' ',end =' ')
	print()

print('\n\n\n\n')
print('total number of paths are: ',matrix[size_of_matrix-1][size_of_matrix-1])
