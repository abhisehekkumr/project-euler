matrix_size = 310
range_of_power = 1000
matrix = [0]*matrix_size
matrix[matrix_size-1] = 1


for i in range(0,range_of_power):
	j = matrix_size-1
	product = matrix[matrix_size-1]*2
	#print(matrix)
	while(j != 0):
		matrix[j] = product%10
		product = product//10
		product = product + matrix[j-1]*2
		j = j-1

print(matrix)
sum = 0
for i in range(0,matrix_size):
	sum += matrix[i]

print('sum of matrix is: ',sum)