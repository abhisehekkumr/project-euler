# following program demostrate how to create 2D array

columns  = []

# creating number of rows
for i in range(0,3):
	columns.append([])

# adding row wise values in matrix 
for i in range(0,3):
	for j in range(0,5):
		columns[i].append(int(input('enter number: ')))
# printing the resultant matrix
for i in range(0,3):
	for j in range(0,5):
		print(columns[i][j],' ',end = ' ')
	print()