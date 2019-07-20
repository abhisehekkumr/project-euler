matrix = []

for i in range(0,20):
	row = input().split()
	matrix.append(row)

print(matrix)

forward = 1
below = 1
forrwad_dia = 1
backward_dia = 1
max = 0

for i in range(0,17):
	for j in range(0,17):
		
		forward = forward * int(matrix[i][j]) * int(matrix[i][j+1]) * int(matrix[i][j+2]) * int(matrix[i][j+3])
		below = below * int(matrix[i][j]) * int(matrix[i+1][j]) * int(matrix[i+2][j]) * int(matrix[i+3][j])
		forrwad_dia = forrwad_dia * int(matrix[i][j]) * int(matrix[i+1][j+1]) * int(matrix[i+2][j+2]) * int(matrix[i+3][j+3])
		backward_dia = backward_dia * int(matrix[i+3][j]) * int(matrix[i+2][j+1]) * int(matrix[i+1][j+2]) * int(matrix[i][j+3])

		if(forward > max):
			max = forward
		if(below > max):
			max = below
		if(forrwad_dia > max):
			max = forrwad_dia
		if(backward_dia > max):
			max = backward_dia

		forward = 1
		below = 1
		forrwad_dia = 1
		backward_dia = 1

print(max)