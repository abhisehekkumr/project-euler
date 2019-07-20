a = 0
b = 0
c = 0

for i in range(1,21):
	for j in range(i+1,21):
		a = j*j - i*i
		b = 2*i*j
		c = j*j + i*i

		if(a+b+c == 1000):
			print(a,b,c)
			print(a*b*c)