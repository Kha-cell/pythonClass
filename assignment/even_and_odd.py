

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

num = int(input("Enter a number: "))
print(f"{num} is {'even' if num % 2 == 0 else 'odd'}.") 