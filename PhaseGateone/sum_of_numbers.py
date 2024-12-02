user_input = int(input("Enter number between 0 - 1000:"))
first_number = user_input // 1000
first_reminder = user_input % 1000
second_number = first_reminder // 100
second_reminder = first_reminder % 100
third_number = second_reminder // 10
third_reminder = second_reminder % 10
sum_of_numbers = first_number + second_number + third_number + third_reminder
print(sum_of_numbers)





# write a program that generate two integers within the range of 1-1000
# and add all the digit in the integer entered by the user 
#display sum of digit 
	#stage 1 prompt user ro enter an integer between the range of 1-1000
	#add up all digit in the integers 
	# display the result
