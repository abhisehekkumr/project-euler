def isPrime(number):
	import math as mt
	num = int(mt.sqrt(number))+1

	if number%2 == 0:
		return False

	for i in range(3,num+1,2):
		if number%i == 0:
			return False
	return True

sum = 2
i = 0
for i in range(3,2000001,2):
	if isPrime(i):
		sum = sum + i
		print(i)
print("sum is:",sum)