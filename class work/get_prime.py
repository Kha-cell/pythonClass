def get_prime(number:list)-> int:
	total = 0
	for count in number:
		if count % 1 or number == 0:
			total += count
	return total
print(get_prime([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
