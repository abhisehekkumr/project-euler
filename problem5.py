flag = False
k = 2

while True:
	for i in range(2,21):
		if(k%i != 0):
			flag = True
			print(k)
			break;
	if flag:
		k = k+1
		flag = False
	else:
		print(k)
		break