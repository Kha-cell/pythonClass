#prompt user to enter number  within the range of 1-100
#collect number from user
#save number for later use 
#store as random_number
#create a variable to store the sum of the random_number
#store as sum_of_random_number
#determine if the number collected from user == sum_of_random_number
#print "True"
#else
#print "False"









import random
userInput = int(input("Guess the sum of two numbers:"))
random_number = random.randint(1 , 100)
sum_of_random_number = random_number + random_number

if userInput == sum_of_random_number:
	print("True")
else:
	print("False")