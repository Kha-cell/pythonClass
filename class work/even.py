def get_even(number:list)-> int:
	total = 0
	for count in number:
		if count % 2 == 0:
			total += count
	return total

print(get_even([1, 2, 3, 4, 5,]))