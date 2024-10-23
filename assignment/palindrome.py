def is_palindrome():
num = int(input("Enter a three-digit
integer: "))
1 = abs (num) # Convert negative to
positive
# Extract digits
digit1 = num // 100
digit2 = (num / / 10) % 10
digit3 = num % 10
# Check if palindrome
if digit1 == digit3:
print(f"{num} is a palindrome
integer.")
else:
print(f"{num} is not a palindrome
integer.")
is_ palindrome ()