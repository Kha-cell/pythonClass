import random
userInput = int(input("Guess the sum of two numbers:"))
random_number = random.randint(1 , 100)
sum_of_random_number = random_number + random_number

if userInput == sum_of_random_number:
	print("True")
else:
	print("False")






#prompt user to enter number  within the range of 1-100 
#collect 
#save as userInput
#create a variable to store the guessed number
#store as random_number
#create a variable to store the sum of the random_number
#store as sum_of_random_number
#determine if the userInput == sum_of_random_number
#print "True"
#else
#print "False"



