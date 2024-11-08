number = int(input("Enter number:"))
for number in range(1,number+1):
  for row in range(1,number,1):
    print(row,end=" ")
  print(number)