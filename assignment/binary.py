num=list(input('Enter a binary number: '))
result=0

for k in range(len(num)):
    digit=num.pop()
    if digit == '1':
       result=result + pow(2,k)
print('The decimal value is ',result)