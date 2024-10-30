




assign_number = 5  

def check_number():
    while True:
        try:
            user_input = int(input("Enter a number: "))
            if user_input == assign_number:
                print("Correct!")
                break
            elif user_input > assign_number:
                print("Too high!")
            else:
                print("Too low!")
        except ValueError:
            print("Invalid input. Please enter a number.")

check_number()



