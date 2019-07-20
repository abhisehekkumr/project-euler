def isPalindrome(number):
	exp = 0
	num = number
	while number > 0:
		exp = exp*10 + number%10
		number = number//10

	if exp == number:
		print(number)
		return True
	return False


def reverseNumber(number , partial = 0):
	if number == 0:
		return partial
	return reverseNumber(number // 10, partial*10 + number%10)


product = 1;
for i in range(999,900,-1):
	for j in range(999,900,-1):
		if reverseNumber(i*j) == i*j:
			if(product < i*j):
				product = i*j

print(product)