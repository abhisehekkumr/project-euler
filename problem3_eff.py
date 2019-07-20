number = int(input('Enter number: '))

prime_number = 2

for i in range(2,int(number/2)+1):
	while (number/i).is_integer():
		number = number/i
		prime_number = i

	if int(number) == 1:
		break
print(prime_number)