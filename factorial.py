size_of_matrix = 160
factorial = 100

matrix = [0]*size_of_matrix

matrix[size_of_matrix-1] = 1

for i in range(2,factorial+1):
	product = matrix[size_of_matrix-1]*i
	j = size_of_matrix-1
	while(j!= 0):
		matrix[j] = product%10
		product = product//10
		product = product + matrix[j-1]*i
		j =  j-1
print(matrix)

sum = 0
for i in range(0,len(matrix)):
	sum += matrix[i]
print('the is : ',sum)