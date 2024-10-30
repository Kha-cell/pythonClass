

def largest_smallest_program():
    numbers = []
    
    while True:
        user_input = input("Enter a number (or 'q' to quit): ")
        
        if user_input.lower() == 'q':
            break
        
        try:
            num = float(user_input)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if numbers:
        print(f"Largest number: {max(numbers)}")
        print(f"Smallest number: {min(numbers)}")
    else:
        print("No numbers entered.")

largest_smallest_program()

