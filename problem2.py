a = 1
b = 2
sum = 0
result = 2
while sum <= 4000000:
	sum = a + b
	a = b
	b = sum
	print(sum)
	if sum%2 == 0:
		result = result + sum
print("result is ",result)