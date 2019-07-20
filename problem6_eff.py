#	sum of natural number can be determined by
#	
#	sum = n(n+1)
#	____________
#		2
#	sum of square of natural number can be determined by 
#	
#	n(n+1)(2n+1)
#	____________
#		6

n = 100

natural_sum = (n*(n+1))//2
square_sum = (n*(n+1)*(2*n+1))//6
print(natural_sum*natural_sum -square_sum) 