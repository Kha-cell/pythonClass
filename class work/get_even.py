def get_even(number:list)-> int:
	total = 0
	for count in number:
		if count % 2 == 0:
			total += count
	return total

print(get_even([2,7,9,17,19,2,8,10]))