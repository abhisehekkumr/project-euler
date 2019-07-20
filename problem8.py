arr2d = [[j for j in input().split()] for i in range(20)]

count = 0

for k in range(0,21):
	print("new line")
	for i in range(0,18):
		print("list")
		for j in  range(i,i+4):
			print(arr2d[k][i+j])