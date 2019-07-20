def isPrime(number):
	import math as mt
	num = int(mt.sqrt(number))+1

	if number%2 == 0:
		return False

	for i in range(3,num+1,2):
		if number%i == 0:
			return False
	return True

count = 1
i = 3
while count < 10001:
	if isPrime(i):
		print(i)
		count = count +1
	i = i+2
print(count,i-2)