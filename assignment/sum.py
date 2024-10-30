while True:
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

       
        sum = num1 + num2

       
        print(f"{num1} + {num2} = {sum}")

        
        response = input("Do you want to add again? (y/n): ")

       
        if response.lower() != 'y':
            break

addition_program()

