sum = 0;
square = 0;

for i in range(1,101):
	square += i*i
	sum += i
print((sum*sum) -square)