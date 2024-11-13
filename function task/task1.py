
def get_number_of_vowels(vowels):
	counter=0

	for word in vowels:
		if word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u' or word == 'A' or word == 'E' or word == 'I' or word == 'O' or word == 'U':
			counter += 1
		else:
			print = ("there is no vowel in this word")
	return counter
		
sentence = input("enter word: ")

print(get_number_of_vowels(sentence))