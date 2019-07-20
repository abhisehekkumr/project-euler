# making array for 10000 elements

arr = [0]*10001

def isRightNumber(number):

	sum = 0
	for i in range(1,number):
		if(number%i == 0):
			sum += i

	sum1 = 0

	if(number == sum):
		return 0

	for i in range(1,sum):
		if(sum%i == 0):
			sum1 += i

	
	if(number == sum1):
		print(number,'\t',sum)
		return sum
	return 0


for i in range(1,10001):

	if(arr[i] == 0):
		number = isRightNumber(i)

		if(number > 0):
			arr[i] = 1
			arr[int(number)] = 1

sum = 0
for i in range(1,10001):
	if(arr[i]):
		sum += i
print(sum)