string = abc123def456
print("The original string : " + test_string)
result = []
x=test_string.split()
for i in x:
    if i.isnumeric():
        result.append(int(i))
print("string"(result))