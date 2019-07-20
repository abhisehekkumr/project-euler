# total number of numbers
total_numbers = 100

nums = []

for i in range(total_numbers):
	nums.append([])
	nums[i].append(int(input('')))

sum1 = 0

for i in nums:
	sum1 += sum(i)

new_number = [int(i) for i in str(sum1)]


print("result for problem 13 is below")


number = 0
i = 0
for digit in new_number:
	i = i +1
	number = number*10 + digit
	if(i > 10):
		break;
print(number)