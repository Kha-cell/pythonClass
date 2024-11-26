def get_even(number:list):
	holder = list()
	if type(number) is list:
		for count in number:
			if count % 2 == 0:
				holder.append(True)
			else:
				holder.append(False)
		return holder
	raise TypeError("Not a list object")