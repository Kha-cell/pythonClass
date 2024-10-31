
def weekday_generator():
    weekdays = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
    num = input("Enter a number (1-7): ")
    
    try:
        num = int(num)
        if 1 <= num <= 7:
            print(f"{num} corresponds to {weekdays[num]}")
        else:
            print("Invalid input. Please enter a number between 1 and 7.")
    def main():
    print("Weekday Generator")
    print("Enter number corresponding to weekday:")
    print("1. Monday")
    print("2. Tuesday")
    print("3. Wednesday")
    print("4. Thursday")
    print("5. Friday")
    print("6. Saturday")
    print("7. Sunday")
    
    weekday_generator()

if __name__ == "__main__":
    main()

