def isPrime(number):
	import math as mt
	for i in range(2,int(mt.sqrt(number))+1):
		if number%i == 0:
			return False
	return True


prime_number = 1
number = int(input('Enter number: '))
flag = False
for i in range(2,int(number/2)+1):
	if(isPrime(i)):
		temp = number/i
		while temp.is_integer():
			number = number/i
			temp = number/i
			prime_number = i
			print(prime_number)
			if int(number) == 1:
				flag = True
		print("prime ",i)
	if flag:
		break
print("largest prime factor is ",prime_number)