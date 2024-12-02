def get_even(number:list)-> int:
	true = 0
	for count in number:
		if count % 2 == 0:
			true += 1
	return true

print(get_even([1,5,7,3,2,9,8,10,20,40,42,20,20]))
