num1 = int(input('enter fisrt number:'))
num2 = int(input('enter second number:'))
num3 = int(input('enter third number:'))

sum = num1 + num2 + num3
product =  num1 * num2 * num3
average = sum / 3

smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)

print("/nResult")
print("Sum:", sum)
print("Smallest:",smallest)
print("Largest:", largest)
print("Average:", average)