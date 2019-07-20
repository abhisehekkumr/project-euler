'''
number = 28124

arr = [0]*28125

i = 12
arr[i] = 1
while(i < number):

	j = i

	if(arr[i] == 1):
		while(j < number):
			arr[j] = 1
			j = j + i
	i = i +1

sum = 0
for i in range(1,number):

	if(arr[i] == 0):
		print(i)

print(sum)
'''

i = 1
a = 0
b = 1
c = 0
print(a," ", i)
while True:
	c = a + b
	print(c," ",i)
	a = b
	b = c
	i = i + 1