def odd_number_count(number:list):
    return [x**2 for x in number if x%2!=  0]

print(odd_number_count([10,3,7,1,9,4,2,8,5,6]))