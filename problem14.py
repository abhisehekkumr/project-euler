max = 0
max_number = 0
count = 1
i = 0

for i in range(2,1000000+1):
	num = i

	while num != 1:
		count = count+1
		if num%2 == 0:
			num = int(num/2)
		else:
			num = 3*num+1

	if count > max:
		max_number = i
		max = count
	print(i,' : ',count)
	count = 1

print('maximum longest sequesnce',max_number,':',max)