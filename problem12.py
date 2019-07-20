'''
def prineDevisor(number):
	hash_map = [1]*(number+1)

	prime = 2

	while((prime * prime) < number):
		if hash_map[prime] == 1:
			for i in range(2*prime, number,prime):
				hash_map[i] = 0
		prime += 1

	total = 1

	for prime in range(2,number+1):
		if(hash_map[prime] == 1):
			count = 0
			if(number%prime == 0):
				while(number%prime == 0):
					number = int(number/prime)
					count = count + 1
				total = total*(count+1)
	return total
'''

def primeCalculation(number):
	import math

	num = int(math.sqrt(number))
	divisor = 0
	for i in range(1,num+1):
		if number%i == 0:
			divisor += 2

	if num * num == number:
		divisor -= 1
	return divisor


divisor_count = 0
i = 1
k = 1
while divisor_count < 500:
	divisor_count = primeCalculation(k)
	i = i + 1
	k = k + i
print(k)