passed = 0
failed = 0
count = 1
for result in range(15):
	result = int(input("enter number:"))
if result < 15:
	failed  += 1
if result >= 45:
	passed = passed + 1
print("Passed: ", passed)
print("Failed: ", failed)

count += 1