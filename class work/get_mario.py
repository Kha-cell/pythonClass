def get_even(number:list)-> int:
	total = 0
	for count in number:
		if count % 2 == 0:
			total += 1
	return total

print(get_even([1,5,7,3,2,9,8,10]))
